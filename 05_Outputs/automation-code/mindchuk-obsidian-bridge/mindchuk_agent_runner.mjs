#!/usr/bin/env node

import { mkdir, readdir, readFile, rename, stat, writeFile } from "node:fs/promises";
import path from "node:path";
import { spawn } from "node:child_process";
import { fileURLToPath } from "node:url";

const scriptPath = fileURLToPath(import.meta.url);
const scriptDir = path.dirname(scriptPath);
const vaultRoot = path.resolve(scriptDir, "..", "..", "..");
const bridgeScript = path.join(scriptDir, "mindchuk_bridge.mjs");
const defaultCodexExecutable =
  "C:\\Users\\shiva\\.vscode\\extensions\\openai.chatgpt-26.527.31454-win32-x64\\bin\\windows-x86_64\\codex.exe";

const command = (process.argv[2] ?? "once").toLowerCase();
const extraArgs = process.argv.slice(3);

const config = {
  inboxDir: path.join(scriptDir, "agent-inbox"),
  pendingDir: path.join(scriptDir, "agent-inbox", "pending"),
  processingDir: path.join(scriptDir, "agent-inbox", "processing"),
  completedDir: path.join(scriptDir, "agent-inbox", "completed"),
  failedDir: path.join(scriptDir, "agent-inbox", "failed"),
  runsDir: path.join(scriptDir, "agent-inbox", "runs"),
  resultOutboxDir: path.join(scriptDir, "agent-inbox", "result-outbox"),
  pollSeconds: Number(process.env.MINDCHUK_AGENT_POLL_SECONDS ?? "60"),
  recoveryAgeSeconds: Number(process.env.MINDCHUK_AGENT_RECOVERY_AGE_SECONDS ?? "300"),
  runPull: !extraArgs.includes("--skip-pull"),
  reportResults: process.env.MINDCHUK_AGENT_REPORT_RESULTS !== "false",
  nodeExecutable: process.env.MINDCHUK_NODE_PATH ?? process.execPath,
  bridgePullTimeoutMs: Number(process.env.MINDCHUK_PULL_TIMEOUT_MS ?? "120000"),
  bridgePushTimeoutMs: Number(process.env.MINDCHUK_PUSH_TIMEOUT_MS ?? "120000"),
  codexTimeoutMs: Number(process.env.MINDCHUK_CODEX_TIMEOUT_MS ?? "900000"),
  refineSandbox: process.env.MINDCHUK_CODEX_REFINE_SANDBOX ?? "read-only",
  sandbox: process.env.MINDCHUK_CODEX_SANDBOX ?? "workspace-write",
  allowDangerFallback: process.env.MINDCHUK_CODEX_ALLOW_DANGER_FALLBACK !== "false",
  model: process.env.MINDCHUK_CODEX_MODEL ?? "",
  codexExecutable: process.env.MINDCHUK_CODEX_PATH ?? defaultCodexExecutable,
};

main().catch((error) => {
  console.error(error instanceof Error ? error.stack ?? error.message : String(error));
  process.exitCode = 1;
});

async function main() {
  if (command === "help" || command === "--help" || command === "-h") {
    printHelp();
    return;
  }

  if (!["once", "watch"].includes(command)) {
    throw new Error(`Unknown command '${command}'. Use 'help', 'once', or 'watch'.`);
  }

  await ensureDir(config.pendingDir);
  await ensureDir(config.processingDir);
  await ensureDir(config.completedDir);
  await ensureDir(config.failedDir);
  await ensureDir(config.runsDir);
  await ensureDir(config.resultOutboxDir);
  await validateConfiguredExecutables();

  if (command === "once") {
    const processed = await runCycle();
    console.log(`Processed ${processed} queued agent task(s).`);
    return;
  }

  console.log(`Watching ${config.pendingDir} every ${config.pollSeconds}s`);
  while (true) {
    try {
      const processed = await runCycle();
      if (processed > 0) {
        console.log(`Processed ${processed} queued agent task(s).`);
      }
    } catch (error) {
      console.error(error instanceof Error ? error.message : String(error));
    }
    await sleep(config.pollSeconds * 1000);
  }
}

function printHelp() {
  console.log(`
MindChuk Agent Runner

Usage:
  node mindchuk_agent_runner.mjs once
  node mindchuk_agent_runner.mjs watch

Options:
  --skip-pull   Process the local queue without refreshing from MindChuk first

Optional environment variables:
  MINDCHUK_AGENT_POLL_SECONDS
  MINDCHUK_AGENT_REPORT_RESULTS
  MINDCHUK_CODEX_REFINE_SANDBOX
  MINDCHUK_CODEX_SANDBOX
  MINDCHUK_CODEX_ALLOW_DANGER_FALLBACK
  MINDCHUK_CODEX_MODEL
  MINDCHUK_CODEX_PATH
  MINDCHUK_PUSH_TIMEOUT_MS

Notes:
  - If MINDCHUK_EMAIL and MINDCHUK_PASSWORD are set, the runner will pull new MindChuk items before processing.
  - By default, completed or failed runs also publish a result note back into MindChuk through agent-inbox/result-outbox.
  - Tasks must already exist in agent-inbox/pending or be generated there by the bridge.
`.trim());
}

async function runCycle() {
  await recoverStaleProcessingTasks();

  if (config.runPull && process.env.MINDCHUK_EMAIL && process.env.MINDCHUK_PASSWORD) {
    try {
      await runBridgePull();
    } catch (error) {
      console.error(error instanceof Error ? error.message : String(error));
    }
  }

  const pendingFiles = await listMarkdownFiles(config.pendingDir);
  let processed = 0;

  for (const pendingFile of pendingFiles.sort()) {
    await processTaskFile(pendingFile);
    processed += 1;
  }

  await refreshAgentInboxIndex();
  return processed;
}

async function runBridgePull() {
  return runBridgeCommand("pull", {
    timeoutMs: config.bridgePullTimeoutMs,
    label: "MindChuk pull",
    stage: "pull",
  });
}

async function runBridgePush(outboxDir) {
  return runBridgeCommand("push", {
    timeoutMs: config.bridgePushTimeoutMs,
    label: "MindChuk push",
    stage: "push",
    envOverrides: outboxDir
      ? {
          MINDCHUK_OUTBOX_DIR: outboxDir,
        }
      : {},
  });
}

async function runBridgeCommand(bridgeCommand, options = {}) {
  const child = spawn(config.nodeExecutable, [bridgeScript, bridgeCommand], {
    cwd: vaultRoot,
    stdio: ["ignore", "pipe", "pipe"],
    env: {
      ...process.env,
      ...(options.envOverrides ?? {}),
    },
    windowsHide: true,
  });

  const stdout = [];
  const stderr = [];
  child.stdout.on("data", (chunk) => stdout.push(chunk));
  child.stderr.on("data", (chunk) => stderr.push(chunk));

  const exitCode = await waitForExit(child, {
    timeoutMs: options.timeoutMs ?? config.bridgePullTimeoutMs,
    label: options.label ?? `MindChuk ${bridgeCommand}`,
    stage: options.stage ?? bridgeCommand,
  });
  if (exitCode !== 0) {
    throw new Error(
      `MindChuk ${bridgeCommand} failed with exit code ${exitCode}.\n${Buffer.concat(stderr).toString("utf8") || Buffer.concat(stdout).toString("utf8")}`,
    );
  }

  return {
    exitCode,
    stdout: Buffer.concat(stdout).toString("utf8"),
    stderr: Buffer.concat(stderr).toString("utf8"),
  };
}

async function recoverStaleProcessingTasks() {
  const processingFiles = await listMarkdownFiles(config.processingDir);
  if (processingFiles.length === 0) {
    return;
  }

  const now = Date.now();
  const recoveryThresholdMs = Math.max(config.recoveryAgeSeconds * 1000, config.codexTimeoutMs + 30000);
  let recovered = 0;

  for (const processingFile of processingFiles) {
    const content = await readFile(processingFile, "utf8");
    const parsed = parseMarkdown(content);
    const startedAt = Date.parse(String(parsed.frontmatter.runner_started_at ?? ""));
    const ageMs = Number.isNaN(startedAt) ? Number.POSITIVE_INFINITY : now - startedAt;

    if (ageMs < recoveryThresholdMs) {
      continue;
    }

    const requeuedFrontmatter = {
      ...parsed.frontmatter,
      status: "pending",
      runner_recovered_at: new Date().toISOString(),
    };
    const requeuedBody = upsertRunnerSection(parsed.body, {
      status: "pending",
      startedAt: "",
      completedAt: "",
      exitCode: "",
      runId: "",
      runDir: "",
      resultSummary: "Recovered after a previous runner interruption.",
    });
    const destination = path.join(config.pendingDir, path.basename(processingFile));
    await archiveExistingTaskFile(destination);
    await rename(processingFile, destination);
    await writeFile(destination, serializeMarkdown(requeuedFrontmatter, requeuedBody), "utf8");
    recovered += 1;
  }

  if (recovered > 0) {
    console.warn(`Recovered ${recovered} stale processing task(s) back to pending.`);
  }
}

async function processTaskFile(pendingFile) {
  const taskFileName = path.basename(pendingFile);
  const taskId = path.basename(pendingFile, ".md");
  const processingFile = path.join(config.processingDir, taskFileName);
  let currentFile = pendingFile;
  let sourceContent = "";
  let parsed = { frontmatter: {}, body: "" };
  let startedAt = new Date().toISOString();
  let runId = `${taskId}--attempt-${compactTimestamp(startedAt)}`;
  let runDir = path.join(config.runsDir, runId);
  let taskFrontmatter = {};

  try {
    sourceContent = await readFile(pendingFile, "utf8");
    parsed = parseMarkdown(sourceContent);
    startedAt = new Date().toISOString();
    runId = `${taskId}--attempt-${compactTimestamp(startedAt)}`;
    runDir = path.join(config.runsDir, runId);
    await ensureDir(runDir);

    const rawPrompt = extractPromptFromTask(parsed.body);
    const sourceMessageId = String(parsed.frontmatter.source_message_id ?? "");
    taskFrontmatter = {
      ...parsed.frontmatter,
      status: "processing",
      run_id: runId,
      runner_started_at: startedAt,
      runner_mode: "codex-refine-then-execute",
    };

    const processingBody = upsertRunnerSection(parsed.body, {
      status: "processing",
      startedAt,
      completedAt: "",
      exitCode: "",
      runId,
      runDir,
      resultSummary: "",
    });

    await rename(pendingFile, processingFile);
    currentFile = processingFile;
    await writeFile(processingFile, serializeMarkdown(taskFrontmatter, processingBody), "utf8");
    await writeFile(path.join(runDir, "source-task.md"), sourceContent, "utf8");
    await writeFile(path.join(runDir, "raw-prompt.txt"), rawPrompt, "utf8");

    const refinementPrompt = buildRefinementPrompt({
      rawPrompt,
      processingFile,
      runDir,
    });
    const refineResult = await runCodexExec(refinementPrompt, {
      sandbox: config.refineSandbox,
      stage: "refine",
    });

    const refinedPrompt = refineResult.ok && refineResult.lastMessage ? refineResult.lastMessage.trim() : rawPrompt.trim();
    await writeFile(path.join(runDir, "refine-stdout.log"), refineResult.stdout, "utf8");
    await writeFile(path.join(runDir, "refine-stderr.log"), refineResult.stderr, "utf8");
    await writeFile(path.join(runDir, "refine-events.jsonl"), refineResult.jsonLines.join("\n"), "utf8");
    await writeFile(path.join(runDir, "refined-prompt.md"), `${refinedPrompt}\n`, "utf8");

    const executionPrompt = buildExecutionPrompt({
      refinedPrompt,
      processingFile,
      runDir,
      sourceMessageId,
    });

    let execResult = await runCodexExec(executionPrompt, {
      sandbox: config.sandbox,
      stage: "execute-primary",
    });
    let executionSandboxUsed = config.sandbox;
    let usedDangerFallback = false;

    if (
      config.allowDangerFallback &&
      config.sandbox !== "danger-full-access" &&
      execResult.encounteredWindowsSandboxRefresh
    ) {
      usedDangerFallback = true;
      await archiveRunArtifact(path.join(runDir, "blocker-note.md"), "primary-attempt-blocker-note");
      await archiveRunArtifact(path.join(runDir, "success-note.md"), "primary-attempt-success-note");
      execResult = await runCodexExec(executionPrompt, {
        sandbox: "danger-full-access",
        stage: "execute-danger-fallback",
      });
      executionSandboxUsed = "danger-full-access";
    }

    const completedAt = new Date().toISOString();

    await writeFile(path.join(runDir, "execute-stdout.log"), execResult.stdout, "utf8");
    await writeFile(path.join(runDir, "execute-stderr.log"), execResult.stderr, "utf8");
    await writeFile(path.join(runDir, "execute-events.jsonl"), execResult.jsonLines.join("\n"), "utf8");
    await writeFile(path.join(runDir, "last-message.md"), `${execResult.lastMessage}\n`, "utf8");

    const finalOutcome = await finalizeRunArtifacts(runDir, execResult);
    const nextStatus = finalOutcome.status;
    const resultKind =
      nextStatus === "completed"
        ? usedDangerFallback
          ? "completed_with_fallback"
          : "completed"
        : finalOutcome.resultKind === "blocked"
          ? "blocked"
          : execResult.encounteredWindowsSandboxRefresh
            ? "sandbox_failure"
            : finalOutcome.resultKind;

    await writeFile(
      path.join(runDir, "run-summary.json"),
      JSON.stringify(
        {
          refinement: {
            exitCode: refineResult.exitCode,
            ok: refineResult.ok,
            sandbox: config.refineSandbox,
            commandCount: refineResult.commandCount,
            failedCommandCount: refineResult.failedCommandCount,
          },
          execution: {
            exitCode: execResult.exitCode,
            ok: execResult.ok,
            sandbox: executionSandboxUsed,
            usedDangerFallback,
            commandCount: execResult.commandCount,
            failedCommandCount: execResult.failedCommandCount,
            encounteredWindowsSandboxRefresh: execResult.encounteredWindowsSandboxRefresh,
          },
          exitCode: execResult.exitCode,
          ok: execResult.ok,
          finalStatus: nextStatus,
          resultKind,
          startedAt,
          completedAt,
          sourceMessageId,
          processingFile,
          runDir,
        },
        null,
        2,
      ),
      "utf8",
    );

    const destinationFile = path.join(
      nextStatus === "completed" ? config.completedDir : config.failedDir,
      taskFileName,
    );
    await archiveExistingTaskFile(destinationFile);

    const finalFrontmatter = {
      ...taskFrontmatter,
      status: nextStatus,
      runner_completed_at: completedAt,
      refined_prompt_file: path.join(runDir, "refined-prompt.md"),
      execution_sandbox: executionSandboxUsed,
      used_danger_fallback: usedDangerFallback,
      codex_exit_code: execResult.exitCode,
      result_kind: resultKind,
    };

    const finalBody = upsertRunnerSection(parsed.body, {
      status: nextStatus,
      startedAt,
      completedAt,
      exitCode: String(execResult.exitCode),
      runId,
      runDir,
      resultSummary: excerpt(execResult.lastMessage, 160),
    });

    await rename(processingFile, destinationFile);
    currentFile = destinationFile;
    await writeFile(destinationFile, serializeMarkdown(finalFrontmatter, finalBody), "utf8");

    const publishResult = await maybePublishResultToMindChuk({
      taskId,
      taskFileName,
      taskFilePath: destinationFile,
      sourceMessageId,
      rawPrompt,
      status: nextStatus,
      resultKind,
      runDir,
      finalMessage: execResult.lastMessage,
    });
    if (publishResult) {
      const updatedFrontmatter = {
        ...finalFrontmatter,
        mindchuk_result_outbox_file: publishResult.outboxFile,
        mindchuk_result_message_id: publishResult.messageId,
        mindchuk_result_sent_at: publishResult.sentAt,
      };
      await writeFile(destinationFile, serializeMarkdown(updatedFrontmatter, finalBody), "utf8");
    }
  } catch (error) {
    const completedAt = new Date().toISOString();
    const errorText = error instanceof Error ? error.stack ?? error.message : String(error);
    const isTimeout = error instanceof Error && error.code === "PROCESS_TIMEOUT";
    await ensureDir(runDir);
    await writeFile(path.join(runDir, "runner-error.log"), `${errorText}\n`, "utf8");

    const blockerPath = path.join(runDir, "blocker-note.md");
    if (!(await pathExists(blockerPath))) {
      await writeFile(
        blockerPath,
        [
          isTimeout ? "The runner timed out before the task could finish." : "The runner hit an unhandled error before the task could finish.",
          "",
          "Error:",
          errorText,
        ].join("\n"),
        "utf8",
      );
    }

    let failureSource = sourceContent;
    if (!failureSource && (await pathExists(currentFile))) {
      failureSource = await readFile(currentFile, "utf8");
    }

    const failureParsed = failureSource ? parseMarkdown(failureSource) : parsed;
    const finalFrontmatter = {
      ...failureParsed.frontmatter,
      status: "failed",
      run_id: runId,
      runner_started_at: startedAt,
      runner_completed_at: completedAt,
      runner_mode: "codex-refine-then-execute",
      codex_exit_code: "",
      result_kind: isTimeout ? "timed_out" : "runner_error",
    };
    const finalBody = upsertRunnerSection(failureParsed.body, {
      status: "failed",
      startedAt,
      completedAt,
      exitCode: "",
      runId,
      runDir,
      resultSummary: excerpt(errorText, 160),
    });

    const sourcePath = (await pathExists(processingFile))
      ? processingFile
      : (await pathExists(pendingFile))
        ? pendingFile
        : null;
    const destinationFile = path.join(config.failedDir, taskFileName);
    await archiveExistingTaskFile(destinationFile);

    if (sourcePath && sourcePath !== destinationFile) {
      await rename(sourcePath, destinationFile);
    }

    await writeFile(destinationFile, serializeMarkdown(finalFrontmatter, finalBody), "utf8");
    const failurePrompt = failureParsed.body ? extractPromptFromTask(failureParsed.body) : "";
    const publishResult = await maybePublishResultToMindChuk({
      taskId,
      taskFileName,
      taskFilePath: destinationFile,
      sourceMessageId: String(failureParsed.frontmatter.source_message_id ?? ""),
      rawPrompt: failurePrompt,
      status: "failed",
      resultKind: isTimeout ? "timed_out" : "runner_error",
      runDir,
      finalMessage: errorText,
    });
    if (publishResult) {
      const updatedFrontmatter = {
        ...finalFrontmatter,
        mindchuk_result_outbox_file: publishResult.outboxFile,
        mindchuk_result_message_id: publishResult.messageId,
        mindchuk_result_sent_at: publishResult.sentAt,
      };
      await writeFile(destinationFile, serializeMarkdown(updatedFrontmatter, finalBody), "utf8");
    }
    console.error(`Task ${taskFileName} failed: ${errorText}`);
  }
}

async function maybePublishResultToMindChuk({
  taskId,
  taskFileName,
  taskFilePath,
  sourceMessageId,
  rawPrompt,
  status,
  resultKind,
  runDir,
  finalMessage,
}) {
  if (!config.reportResults || !process.env.MINDCHUK_EMAIL || !process.env.MINDCHUK_PASSWORD) {
    return null;
  }

  try {
    const outboxFile = path.join(config.resultOutboxDir, `${taskId}--result.md`);
    const outboxMarkdown = await buildMindChukResultOutboxMarkdown({
      taskFileName,
      taskFilePath,
      sourceMessageId,
      rawPrompt,
      status,
      resultKind,
      runDir,
      finalMessage,
    });

    await writeFile(outboxFile, outboxMarkdown, "utf8");
    await runBridgePush(config.resultOutboxDir);

    const pushedFile = parseMarkdown(await readFile(outboxFile, "utf8"));
    return {
      outboxFile,
      messageId: String(pushedFile.frontmatter.mindchuk_id ?? ""),
      sentAt: String(pushedFile.frontmatter.mindchuk_sent_at ?? ""),
    };
  } catch (error) {
    console.error(`MindChuk result publish failed for ${taskFileName}: ${error instanceof Error ? error.message : String(error)}`);
    return null;
  }
}

async function buildMindChukResultOutboxMarkdown({
  taskFileName,
  taskFilePath,
  sourceMessageId,
  rawPrompt,
  status,
  resultKind,
  runDir,
  finalMessage,
}) {
  const successNotePath = path.join(runDir, "success-note.md");
  const blockerNotePath = path.join(runDir, "blocker-note.md");

  let detailText = "";
  if (await pathExists(successNotePath)) {
    detailText = (await readFile(successNotePath, "utf8")).trim();
  } else if (await pathExists(blockerNotePath)) {
    detailText = (await readFile(blockerNotePath, "utf8")).trim();
  } else {
    detailText = String(finalMessage ?? "").trim();
  }

  const relativeTaskPath = toPosixPath(path.relative(vaultRoot, taskFilePath));
  const relativeRunPath = toPosixPath(path.relative(vaultRoot, runDir));
  const statusLabel = normalizeResultStatusLabel(status, resultKind);
  const requestPreview = excerpt(rawPrompt || "(empty request)", 280);
  const detailPreview = excerpt(detailText || "(no result details captured)", 1800);

  const body = [
    `[Codex result ${statusLabel}]`,
    "",
    `Request: ${requestPreview}`,
    "",
    "Result:",
    detailPreview,
    "",
    "Vault artifacts:",
    `- task: ${relativeTaskPath}`,
    `- run: ${relativeRunPath}`,
    sourceMessageId ? `- source message id: ${sourceMessageId}` : "",
  ]
    .filter(Boolean)
    .join("\n");

  return serializeMarkdown(
    {
      title: `Codex result ${statusLabel} ${taskFileName}`,
      content_type: "note",
      mindchuk_tags: ["CODEXRESULT", `CODEX${statusLabel.toUpperCase()}`],
    },
    body,
  );
}

function normalizeResultStatusLabel(status, resultKind) {
  if (status === "completed") {
    return "completed";
  }
  if (resultKind === "blocked") {
    return "blocked";
  }
  return "failed";
}

async function refreshAgentInboxIndex() {
  const pendingRecords = await listAgentTaskRecords(config.pendingDir);
  const processingRecords = await listAgentTaskRecords(config.processingDir);
  const completedRecords = await listAgentTaskRecords(config.completedDir);
  const failedRecords = await listAgentTaskRecords(config.failedDir);

  const lines = [
    "---",
    "title: MindChuk Agent Inbox",
    "description: Generated queue of MindChuk notes that look like agent prompts",
    `last_updated: ${new Date().toISOString()}`,
    "---",
    "",
    "# MindChuk Agent Inbox",
    "",
    "These files are generated from MindChuk notes tagged `AGENT` or starting with `/agent` or `/codex`.",
    "",
    "## Queue",
    "",
    `- Pending: ${pendingRecords.length}`,
    `- Processing: ${processingRecords.length}`,
    `- Completed: ${completedRecords.length}`,
    `- Failed: ${failedRecords.length}`,
    "",
    "## Reality Check",
    "",
    "This is local automation. The runner only works while this machine is on and `mindchuk_agent_runner.mjs` is running.",
  ];

  lines.push("", "## Pending", "");
  if (pendingRecords.length === 0) {
    lines.push("- No pending agent-style prompts were found on the last refresh.");
  } else {
    const pendingItems = await buildIndexItems(pendingRecords, config.inboxDir);
    for (const item of pendingItems) {
      lines.push(`- [${item.label}](${item.link}) - ${item.summary}`);
    }
  }

  lines.push("", "## Processing", "");
  if (processingRecords.length === 0) {
    lines.push("- No tasks are currently in processing.");
  } else {
    const processingItems = await buildIndexItems(processingRecords, config.inboxDir);
    for (const item of processingItems) {
      lines.push(`- [${item.label}](${item.link}) - ${item.summary}`);
    }
  }

  lines.push("", "## Recent Completed", "");
  if (completedRecords.length === 0) {
    lines.push("- No completed agent runs yet.");
  } else {
    const completedItems = await buildIndexItems(completedRecords.slice(0, 5), config.inboxDir);
    for (const item of completedItems) {
      lines.push(`- [${item.label}](${item.link}) - ${item.summary}`);
    }
  }

  lines.push("", "## Recent Failed", "");
  if (failedRecords.length === 0) {
    lines.push("- No failed agent runs yet.");
  } else {
    const failedItems = await buildIndexItems(failedRecords.slice(0, 5), config.inboxDir);
    for (const item of failedItems) {
      lines.push(`- [${item.label}](${item.link}) - ${item.summary}`);
    }
  }

  await writeFile(path.join(config.inboxDir, "_index.md"), `${lines.join("\n")}\n`, "utf8");
}

async function buildIndexItems(records, baseDir) {
  const items = [];
  for (const record of records) {
    const { filePath, parsed } = record;
    const label = String(parsed.frontmatter.title ?? path.basename(filePath, ".md"));
    const summary = excerpt(extractPromptFromTask(parsed.body), 90) || excerpt(parsed.body, 90) || "(empty)";
    const link = toPosixPath(path.relative(baseDir, filePath));
    items.push({ label, summary, link });
  }
  return items;
}

async function runCodexExec(prompt, options = {}) {
  const args = [
    "-a",
    "never",
    "exec",
    "--json",
    "--color",
    "never",
    "--cd",
    vaultRoot,
    "--sandbox",
    options.sandbox ?? config.sandbox,
  ];

  if (config.model) {
    args.push("--model", config.model);
  }

  args.push("-");

  const child = spawn(config.codexExecutable, args, {
    cwd: vaultRoot,
    env: process.env,
    stdio: ["pipe", "pipe", "pipe"],
    windowsHide: true,
  });

  child.stdin.write(prompt);
  child.stdin.end();

  const stdoutChunks = [];
  const stderrChunks = [];
  child.stdout.on("data", (chunk) => stdoutChunks.push(Buffer.from(chunk)));
  child.stderr.on("data", (chunk) => stderrChunks.push(Buffer.from(chunk)));

  const exitCode = await waitForExit(child, {
    timeoutMs: config.codexTimeoutMs,
    label: `Codex ${options.stage ?? "exec"}`,
    stage: options.stage ?? "exec",
  });
  const stdout = Buffer.concat(stdoutChunks).toString("utf8");
  const stderr = Buffer.concat(stderrChunks).toString("utf8");

  const parsed = parseCodexJsonOutput(stdout);
  const lastMessage = parsed.lastMessage || "(no final message captured)";
  const encounteredWindowsSandboxRefresh = `${stdout}\n${stderr}`.includes("windows sandbox: spawn setup refresh");

  return {
    exitCode,
    ok: exitCode === 0,
    stdout,
    stderr,
    jsonLines: parsed.jsonLines,
    lastMessage,
    commandCount: parsed.commandCount,
    failedCommandCount: parsed.failedCommandCount,
    encounteredWindowsSandboxRefresh,
  };
}

function buildRefinementPrompt({ rawPrompt, processingFile, runDir }) {
  return [
    "You are refining a raw phone-captured task for a Codex execution agent.",
    "",
    `Source task file: ${processingFile}`,
    `Run directory: ${runDir}`,
    "",
    "Return only the refined execution prompt.",
    "Do not include explanations, headings, markdown fences, or commentary.",
    "Make the prompt concrete and actionable for work inside an Obsidian vault on Windows.",
    "If the task is vague, preserve the intent but add instructions telling the execution agent to create blocker-note.md instead of guessing broadly.",
    "",
    "Raw task:",
    rawPrompt.trim() || "(empty prompt)",
    "",
  ].join("\n");
}

function buildExecutionPrompt({ refinedPrompt, processingFile, runDir, sourceMessageId }) {
  return [
    "This task came from a phone-triggered MindChuk queue inside an Obsidian vault.",
    "",
    `Source task file: ${processingFile}`,
    `Run directory: ${runDir}`,
    `MindChuk source message id: ${sourceMessageId || "(unknown)"}`,
    "",
    "Requirements:",
    "- Work only inside the current vault unless the task explicitly requires something else.",
    "- Keep changes safe, minimal, and reversible.",
    "- Avoid shell commands when a direct file edit or reasoning-only answer is enough.",
    "- Before finishing, write exactly one of these files in the run directory:",
    "  - success-note.md if you completed the task or made legitimate progress",
    "  - blocker-note.md if you are blocked, the task is unsafe, or the request is too vague",
    "- If the request is ambiguous, do not guess broadly. Use blocker-note.md.",
    "- End with a short plain-language result summary.",
    "",
    "Execution prompt:",
    refinedPrompt.trim() || "(empty prompt)",
    "",
  ].join("\n");
}

function parseCodexJsonOutput(stdout) {
  const jsonLines = [];
  let lastMessage = "";
  let commandCount = 0;
  let failedCommandCount = 0;

  for (const line of stdout.split(/\r?\n/)) {
    const trimmed = line.trim();
    if (!trimmed.startsWith("{") || !trimmed.endsWith("}")) {
      continue;
    }

    try {
      const parsed = JSON.parse(trimmed);
      jsonLines.push(trimmed);
      if (parsed.type === "item.completed" && parsed.item?.type === "agent_message" && parsed.item?.text) {
        lastMessage = String(parsed.item.text);
      }
      if (parsed.type === "item.completed" && parsed.item?.type === "command_execution") {
        commandCount += 1;
        if (Number(parsed.item.exit_code) !== 0) {
          failedCommandCount += 1;
        }
      }
    } catch {
      continue;
    }
  }

  return { jsonLines, lastMessage, commandCount, failedCommandCount };
}

function extractPromptFromTask(body) {
  const normalized = body.replace(/\r\n/g, "\n");
  const match = /## Prompt\s*\n([\s\S]*?)(?:\n## |\s*$)/.exec(normalized);
  if (match?.[1]) {
    return match[1].trim();
  }
  return normalized.trim();
}

function upsertRunnerSection(body, metadata) {
  const normalized = body.replace(/\r\n/g, "\n").trim();
  const runnerBlock = [
    "## Runner",
    `- status: ${metadata.status}`,
    `- started_at: ${metadata.startedAt || ""}`,
    `- completed_at: ${metadata.completedAt || ""}`,
    `- exit_code: ${metadata.exitCode || ""}`,
    `- run_id: ${metadata.runId || ""}`,
    `- run_dir: ${metadata.runDir || ""}`,
    `- result_summary: ${metadata.resultSummary || ""}`,
  ].join("\n");

  if (/## Runner\s*\n[\s\S]*$/m.test(normalized)) {
    return normalized.replace(/## Runner\s*\n[\s\S]*$/m, runnerBlock);
  }

  return `${normalized}\n\n${runnerBlock}`.trim();
}

function parseMarkdown(content) {
  const normalized = content.replace(/\r\n/g, "\n");
  if (!normalized.startsWith("---\n")) {
    return { frontmatter: {}, body: normalized.trim() };
  }

  const endIndex = normalized.indexOf("\n---\n", 4);
  if (endIndex === -1) {
    return { frontmatter: {}, body: normalized.trim() };
  }

  const rawFrontmatter = normalized.slice(4, endIndex);
  const body = normalized.slice(endIndex + 5).trim();
  return {
    frontmatter: parseFrontmatterBlock(rawFrontmatter),
    body,
  };
}

function parseFrontmatterBlock(block) {
  const data = {};
  let currentArrayKey = null;

  for (const rawLine of block.split("\n")) {
    const line = rawLine.trimEnd();
    if (!line.trim()) {
      continue;
    }

    if (line.startsWith("  - ") && currentArrayKey) {
      data[currentArrayKey].push(parseYamlScalar(line.slice(4)));
      continue;
    }

    const match = /^([A-Za-z0-9_-]+):\s*(.*)$/.exec(line);
    if (!match) {
      continue;
    }

    const [, key, rawValue] = match;
    if (rawValue === "") {
      data[key] = [];
      currentArrayKey = key;
      continue;
    }

    data[key] = parseYamlScalar(rawValue);
    currentArrayKey = null;
  }

  return data;
}

function parseYamlScalar(rawValue) {
  const value = rawValue.trim();
  if (value === "true") return true;
  if (value === "false") return false;
  if (value === "[]") return [];
  if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
    return value.slice(1, -1).replace(/\\"/g, '"').replace(/\\\\/g, "\\");
  }
  return value;
}

function serializeMarkdown(frontmatter, body) {
  const lines = ["---"];
  for (const [key, value] of Object.entries(frontmatter)) {
    lines.push(...serializeYamlEntry(key, value));
  }
  lines.push("---", "", body.trim(), "");
  return lines.join("\n");
}

function serializeYamlEntry(key, value) {
  if (value == null) {
    return [`${key}: ""`];
  }

  if (Array.isArray(value)) {
    if (value.length === 0) {
      return [`${key}: []`];
    }
    return [`${key}:`, ...value.map((item) => `  - ${yamlScalar(item)}`)];
  }

  if (typeof value === "boolean" || typeof value === "number") {
    return [`${key}: ${String(value)}`];
  }

  return [`${key}: ${yamlScalar(value)}`];
}

function yamlScalar(value) {
  const stringValue = String(value ?? "");
  return `"${stringValue.replace(/\\/g, "\\\\").replace(/"/g, '\\"')}"`;
}

async function listMarkdownFiles(dir) {
  if (!(await pathExists(dir))) {
    return [];
  }

  const entries = await readdir(dir, { withFileTypes: true });
  const files = [];
  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...(await listMarkdownFiles(fullPath)));
    } else if (entry.isFile() && entry.name.toLowerCase().endsWith(".md")) {
      files.push(fullPath);
    }
  }
  return files;
}

async function listAgentTaskRecords(dir) {
  const files = await listMarkdownFiles(dir);
  const records = [];

  for (const filePath of files) {
    if (path.basename(filePath).toLowerCase() === "_index.md") {
      continue;
    }

    const parsed = parseMarkdown(await readFile(filePath, "utf8"));
    if (!isAgentTaskFrontmatter(parsed.frontmatter)) {
      continue;
    }

    records.push({
      filePath,
      parsed,
      sortKey: taskSortKey(parsed.frontmatter, filePath),
    });
  }

  records.sort((left, right) => right.sortKey.localeCompare(left.sortKey));
  return records;
}

async function ensureDir(dir) {
  await mkdir(dir, { recursive: true });
}

async function pathExists(target) {
  try {
    await stat(target);
    return true;
  } catch {
    return false;
  }
}

function isAgentTaskFrontmatter(frontmatter) {
  return (
    String(frontmatter.mindchuk_kind ?? "") === "agent_command" &&
    String(frontmatter.source_message_id ?? "").trim().length > 0
  );
}

function taskSortKey(frontmatter, filePath) {
  return String(
    frontmatter.runner_completed_at ??
      frontmatter.runner_started_at ??
      frontmatter.sent_at ??
      path.basename(filePath),
  );
}

async function validateConfiguredExecutables() {
  if (!(await pathExists(config.nodeExecutable))) {
    throw new Error(`Configured Node executable was not found: ${config.nodeExecutable}`);
  }

  if (!(await pathExists(config.codexExecutable))) {
    throw new Error(`Configured Codex executable was not found: ${config.codexExecutable}`);
  }
}

async function finalizeRunArtifacts(runDir, execResult) {
  const successPath = path.join(runDir, "success-note.md");
  const blockerPath = path.join(runDir, "blocker-note.md");
  const hasSuccessNote = await pathExists(successPath);
  const hasBlockerNote = await pathExists(blockerPath);

  if (hasSuccessNote && hasBlockerNote) {
    return { status: "failed", resultKind: "conflicting_outcome_notes" };
  }

  if (hasBlockerNote) {
    return { status: "failed", resultKind: "blocked" };
  }

  if (hasSuccessNote) {
    return { status: "completed", resultKind: "completed" };
  }

  if (execResult.ok) {
    await writeFile(
      successPath,
      [
        "Task appears to have completed without a runner-written success note.",
        "",
        "Fallback summary:",
        execResult.lastMessage,
      ].join("\n"),
      "utf8",
    );
    return { status: "completed", resultKind: "completed" };
  }
  await writeFile(
    blockerPath,
    [
      "Task failed before a blocker note was written.",
      "",
      `Exit code: ${execResult.exitCode}`,
      "",
      "Last message:",
      execResult.lastMessage,
    ].join("\n"),
    "utf8",
  );
  return { status: "failed", resultKind: "failed" };
}

async function archiveRunArtifact(filePath, prefix) {
  if (!(await pathExists(filePath))) {
    return;
  }

  const directory = path.dirname(filePath);
  const extension = path.extname(filePath);
  const baseName = path.basename(filePath, extension);
  const archivedPath = path.join(directory, `${prefix}-${baseName}-${compactTimestamp(new Date().toISOString())}${extension}`);
  await rename(filePath, archivedPath);
}

async function archiveExistingTaskFile(filePath) {
  if (!(await pathExists(filePath))) {
    return;
  }

  const directory = path.dirname(filePath);
  const extension = path.extname(filePath);
  const baseName = path.basename(filePath, extension);
  const archivedPath = path.join(directory, `${baseName}--superseded-${compactTimestamp(new Date().toISOString())}${extension}`);
  await rename(filePath, archivedPath);
}

function waitForExit(child, options = {}) {
  return new Promise((resolve, reject) => {
    let finished = false;
    const timeoutMs = options.timeoutMs ?? 0;
    let timer = null;
    let timeoutError = null;

    const complete = (callback) => (value) => {
      if (finished) {
        return;
      }
      finished = true;
      if (timer) {
        clearTimeout(timer);
      }
      callback(value);
    };

    if (timeoutMs > 0) {
      timer = setTimeout(async () => {
        timeoutError = new Error(`${options.label ?? "Child process"} timed out after ${timeoutMs}ms.`);
        timeoutError.code = "PROCESS_TIMEOUT";
        timeoutError.stage = options.stage ?? "";
        timeoutError.timeoutMs = timeoutMs;
        await terminateChildProcessTree(child);
      }, timeoutMs);
    }

    child.on("error", complete(reject));
    child.on(
      "close",
      complete((code) => {
        if (timeoutError) {
          reject(timeoutError);
          return;
        }
        resolve(code);
      }),
    );
  });
}

function compactTimestamp(value) {
  const parsed = new Date(value);
  const iso = Number.isNaN(parsed.getTime()) ? new Date().toISOString() : parsed.toISOString();
  return iso.replace(/[:.]/g, "-");
}

async function terminateChildProcessTree(child) {
  if (!child.pid) {
    return;
  }

  if (process.platform === "win32") {
    await new Promise((resolve) => {
      const killer = spawn("taskkill", ["/PID", String(child.pid), "/T", "/F"], {
        windowsHide: true,
        stdio: "ignore",
      });
      killer.on("error", () => resolve());
      killer.on("close", () => resolve());
    });
    return;
  }

  try {
    child.kill("SIGKILL");
  } catch {
    // Ignore kill errors during timeout cleanup.
  }
}

function excerpt(value, length = 120) {
  const source = String(value ?? "").replace(/\s+/g, " ").trim();
  if (!source) {
    return "";
  }
  if (source.length <= length) {
    return source;
  }
  return `${source.slice(0, length - 3)}...`;
}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

function toPosixPath(value) {
  return value.split(path.sep).join("/");
}
