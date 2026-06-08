#!/usr/bin/env node

import { mkdir, readdir, readFile, rm, stat, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const SUPABASE_URL = "https://edeshyvopammjmnzjyog.supabase.co";
const SUPABASE_ANON_KEY =
  "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVkZXNoeXZvcGFtbWptbnpqeW9nIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc5OTkxNjUsImV4cCI6MjA5MzU3NTE2NX0.Pa0ojZFM-COB-PLs1s3Lq0pgmJji4A3Vud7JF5gBAAE";
const PAGE_SIZE = 1000;
const AGENT_TAG = "AGENT";
const CODEX_RESULT_TAG = "CODEXRESULT";
const TAG_COLOR = "slate";

const scriptPath = fileURLToPath(import.meta.url);
const scriptDir = path.dirname(scriptPath);
const defaultMirrorDir = path.join(scriptDir, "mirror");
const defaultOutboxDir = path.join(scriptDir, "outbox");
const defaultAgentDir = path.join(scriptDir, "agent-inbox");

const command = (process.argv[2] ?? "help").toLowerCase();
const extraArgs = process.argv.slice(3);
const dryRun = extraArgs.includes("--dry-run");

const config = {
  email: process.env.MINDCHUK_EMAIL ?? "",
  password: process.env.MINDCHUK_PASSWORD ?? "",
  mirrorDir: path.resolve(process.env.MINDCHUK_TARGET_DIR ?? defaultMirrorDir),
  outboxDir: path.resolve(process.env.MINDCHUK_OUTBOX_DIR ?? defaultOutboxDir),
  agentDir: path.resolve(process.env.MINDCHUK_AGENT_DIR ?? defaultAgentDir),
  dryRun,
};

main().catch((error) => {
  console.error(error instanceof Error ? error.message : String(error));
  process.exitCode = 1;
});

async function main() {
  if (command === "help" || command === "--help" || command === "-h") {
    printHelp();
    return;
  }

  if (!["pull", "push", "sync"].includes(command)) {
    throw new Error(`Unknown command '${command}'. Use 'help', 'pull', 'push', or 'sync'.`);
  }

  if (!config.email || !config.password) {
    throw new Error("Set MINDCHUK_EMAIL and MINDCHUK_PASSWORD before running the bridge.");
  }

  await ensureDir(config.mirrorDir);
  await ensureDir(config.outboxDir);
  await ensureDir(config.agentDir);
  await ensureDir(path.join(config.agentDir, "pending"));
  await ensureDir(path.join(config.agentDir, "processing"));
  await ensureDir(path.join(config.agentDir, "completed"));
  await ensureDir(path.join(config.agentDir, "failed"));
  await ensureDir(path.join(config.agentDir, "runs"));

  const session = await signInWithPassword(config.email, config.password);
  const userId = session.user.id;

  let pullSummary = null;
  let pushSummary = null;

  if (command === "pull" || command === "sync") {
    pullSummary = await pullIntoVault({
      accessToken: session.access_token,
      userId,
      dryRun: config.dryRun,
    });
  }

  if (command === "push" || command === "sync") {
    pushSummary = await pushOutbox({
      accessToken: session.access_token,
      userId,
      dryRun: config.dryRun,
    });
  }

  printSummary(pullSummary, pushSummary, config.dryRun);
}

function printHelp() {
  console.log(`
MindChuk Obsidian Bridge

Usage:
  node mindchuk_bridge.mjs help
  node mindchuk_bridge.mjs pull
  node mindchuk_bridge.mjs push
  node mindchuk_bridge.mjs sync

Required environment variables:
  MINDCHUK_EMAIL
  MINDCHUK_PASSWORD

Optional environment variables:
  MINDCHUK_TARGET_DIR
  MINDCHUK_OUTBOX_DIR
  MINDCHUK_AGENT_DIR

Flags:
  --dry-run   Preview actions without writing files or posting new notes
`.trim());
}

function printSummary(pullSummary, pushSummary, isDryRun) {
  const prefix = isDryRun ? "[dry-run] " : "";
  if (pullSummary) {
    console.log(
      `${prefix}Pulled ${pullSummary.messages} messages, ${pullSummary.reminders} reminders, ${pullSummary.tags} tags, and ${pullSummary.agentCommands} agent-command candidates.`,
    );
  }

  if (pushSummary) {
    console.log(
      `${prefix}Pushed ${pushSummary.messagesCreated} new messages, ${pushSummary.remindersCreated} reminders, and updated ${pushSummary.filesUpdated} outbox files.`,
    );
  }
}

async function pullIntoVault({ accessToken, userId, dryRun }) {
  const [profile, messages, reminders, tags, messageTags] = await Promise.all([
    fetchMaybeOne("users_profile", { id: `eq.${userId}`, select: "*" }, accessToken),
    fetchAllRows("messages", { user_id: `eq.${userId}`, select: "*", order: "sent_at.asc" }, accessToken),
    fetchAllRows("reminders", { user_id: `eq.${userId}`, select: "*", order: "remind_at.asc" }, accessToken),
    fetchAllRows("tags", { user_id: `eq.${userId}`, select: "*", order: "created_at.asc" }, accessToken),
    fetchAllRows(
      "message_tags",
      {
        select: "message_id,tag_id,messages!inner(user_id)",
        "messages.user_id": `eq.${userId}`,
      },
      accessToken,
    ),
  ]);

  const tagMap = new Map(tags.map((tag) => [tag.id, tag]));
  const tagsByMessageId = new Map();
  for (const row of messageTags) {
    if (!tagsByMessageId.has(row.message_id)) {
      tagsByMessageId.set(row.message_id, []);
    }
    const tag = tagMap.get(row.tag_id);
    if (tag) {
      tagsByMessageId.get(row.message_id).push(tag);
    }
  }

  const expectedMessageFiles = new Set();
  const expectedReminderFiles = new Set();
  const agentMessages = [];
  const knownAgentTasks = await collectKnownAgentTasks(config.agentDir);

  for (const message of messages) {
    const messageTagsForRow = tagsByMessageId.get(message.id) ?? [];
    const relativePath = messageRelativePath(message);
    expectedMessageFiles.add(path.relative(path.join(config.mirrorDir, "messages"), path.join(config.mirrorDir, relativePath)));

    const absolutePath = path.join(config.mirrorDir, relativePath);
    const markdown = buildMessageMarkdown(message, messageTagsForRow);
    if (!dryRun) {
      await ensureDir(path.dirname(absolutePath));
      await writeFile(absolutePath, markdown, "utf8");
    }

    if (isAgentCommand(message, messageTagsForRow)) {
      agentMessages.push({ message, tags: messageTagsForRow, relativePath });
      if (!knownAgentTasks.allIds.has(String(message.id))) {
        const agentRelativePath = agentRelativeFile(message);
        const absoluteAgentPath = path.join(config.agentDir, agentRelativePath);
        if (!dryRun) {
          await ensureDir(path.dirname(absoluteAgentPath));
          await writeFile(absoluteAgentPath, buildAgentMarkdown(message, messageTagsForRow), "utf8");
        }
      }
    }
  }

  for (const reminder of reminders) {
    const relativePath = reminderRelativePath(reminder);
    expectedReminderFiles.add(path.relative(path.join(config.mirrorDir, "reminders"), path.join(config.mirrorDir, relativePath)));
    const absolutePath = path.join(config.mirrorDir, relativePath);
    if (!dryRun) {
      await ensureDir(path.dirname(absolutePath));
      await writeFile(absolutePath, buildReminderMarkdown(reminder), "utf8");
    }
  }

  if (!dryRun) {
    await cleanGeneratedMarkdown(path.join(config.mirrorDir, "messages"), expectedMessageFiles);
    await cleanGeneratedMarkdown(path.join(config.mirrorDir, "reminders"), expectedReminderFiles);

    await writeFile(
      path.join(config.mirrorDir, "_index.md"),
      buildMirrorIndex({ profile, messages, reminders, agentMessages }),
      "utf8",
    );
    await writeFile(
      path.join(config.agentDir, "_index.md"),
      await buildAgentIndex(config.agentDir),
      "utf8",
    );
  }

  return {
    messages: messages.length,
    reminders: reminders.length,
    tags: tags.length,
    agentCommands: agentMessages.length,
  };
}

async function pushOutbox({ accessToken, userId, dryRun }) {
  const outboxFiles = await listMarkdownFiles(config.outboxDir);
  const candidateFiles = outboxFiles.filter((filePath) => {
    const base = path.basename(filePath).toLowerCase();
    return !["_template.md", "_index.md"].includes(base);
  });

  const existingTags = await fetchAllRows(
    "tags",
    { user_id: `eq.${userId}`, select: "*", order: "created_at.asc" },
    accessToken,
  );
  const tagsByName = new Map(existingTags.map((tag) => [normalizeTagName(tag.name), tag]));

  let messagesCreated = 0;
  let remindersCreated = 0;
  let filesUpdated = 0;

  for (const filePath of candidateFiles) {
    const parsed = parseMarkdown(await readFile(filePath, "utf8"));
    if (parsed.frontmatter.mindchuk_id || parsed.frontmatter.mindchuk_pushed_at) {
      continue;
    }

    const tags = parseTagList(parsed.frontmatter.mindchuk_tags ?? parsed.frontmatter.tags);
    const normalizedTags = [...new Set(tags.map(normalizeTagName).filter(Boolean))];
    const remindAt = parseOptionalDate(parsed.frontmatter.remind_at);
    const todoItems = parseTodoItems(parsed.body);
    const contentType =
      normalizeContentType(parsed.frontmatter.content_type) ??
      (todoItems.length > 0 ? "todo" : "note");
    const body = extractMessageBody(parsed.body, todoItems);

    if (!body && todoItems.length === 0 && !remindAt) {
      continue;
    }

    if (dryRun) {
      messagesCreated += body || todoItems.length > 0 ? 1 : 0;
      remindersCreated += remindAt ? 1 : 0;
      continue;
    }

    let insertedMessage = null;
    if (body || todoItems.length > 0) {
      insertedMessage = await insertMessage({
        accessToken,
        userId,
        body,
        contentType,
        todoItems,
      });
      messagesCreated += 1;

      for (const tagName of normalizedTags) {
        let tag = tagsByName.get(tagName);
        if (!tag) {
          tag = await createTag({ accessToken, userId, name: tagName, color: TAG_COLOR });
          tagsByName.set(tagName, tag);
        }
        await insertMessageTag({ accessToken, messageId: insertedMessage.id, tagId: tag.id });
      }
    }

    if (remindAt) {
      await insertReminder({
        accessToken,
        userId,
        body: body || buildReminderFallback(parsed.body),
        remindAt,
      });
      remindersCreated += 1;
    }

    const nextFrontmatter = {
      ...parsed.frontmatter,
      mindchuk_id: insertedMessage?.id ?? "",
      mindchuk_sent_at: insertedMessage?.sent_at ?? "",
      mindchuk_pushed_at: new Date().toISOString(),
      content_type: contentType,
    };

    await writeFile(filePath, serializeMarkdown(nextFrontmatter, parsed.body), "utf8");
    filesUpdated += 1;
  }

  return {
    messagesCreated,
    remindersCreated,
    filesUpdated,
  };
}

async function signInWithPassword(email, password) {
  const url = `${SUPABASE_URL}/auth/v1/token?grant_type=password`;
  const response = await requestJson(url, {
    method: "POST",
    headers: {
      apikey: SUPABASE_ANON_KEY,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ email, password }),
  });

  if (!response.access_token || !response.user?.id) {
    throw new Error("MindChuk login succeeded without a usable session.");
  }

  return response;
}

async function fetchAllRows(table, params, accessToken) {
  const rows = [];
  let offset = 0;

  while (true) {
    const search = new URLSearchParams();
    for (const [key, value] of Object.entries(params)) {
      search.set(key, value);
    }
    search.set("limit", String(PAGE_SIZE));
    search.set("offset", String(offset));

    const page = await requestJson(`${SUPABASE_URL}/rest/v1/${table}?${search.toString()}`, {
      headers: buildRestHeaders(accessToken),
    });

    rows.push(...page);
    if (page.length < PAGE_SIZE) {
      break;
    }
    offset += PAGE_SIZE;
  }

  return rows;
}

async function fetchMaybeOne(table, params, accessToken) {
  const search = new URLSearchParams();
  for (const [key, value] of Object.entries(params)) {
    search.set(key, value);
  }
  search.set("limit", "1");

  const rows = await requestJson(`${SUPABASE_URL}/rest/v1/${table}?${search.toString()}`, {
    headers: buildRestHeaders(accessToken),
  });

  return rows[0] ?? null;
}

async function insertMessage({ accessToken, userId, body, contentType, todoItems }) {
  const urls = extractUrls(body);
  const payload = {
    user_id: userId,
    body,
    contains_url: urls.length > 0,
    extracted_url: urls[0] ?? null,
    extracted_urls: urls.length > 0 ? urls : null,
    content_type: contentType,
    todo_items: todoItems.length > 0 ? todoItems : null,
  };

  const rows = await requestJson(`${SUPABASE_URL}/rest/v1/messages`, {
    method: "POST",
    headers: {
      ...buildRestHeaders(accessToken),
      Prefer: "return=representation",
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!Array.isArray(rows) || !rows[0]?.id) {
    throw new Error("MindChuk did not return the inserted message.");
  }

  return rows[0];
}

async function createTag({ accessToken, userId, name, color }) {
  const rows = await requestJson(`${SUPABASE_URL}/rest/v1/tags`, {
    method: "POST",
    headers: {
      ...buildRestHeaders(accessToken),
      Prefer: "return=representation",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      user_id: userId,
      name,
      color,
      parent_tag_id: null,
    }),
  });

  if (!Array.isArray(rows) || !rows[0]?.id) {
    throw new Error(`MindChuk did not return the inserted tag '${name}'.`);
  }

  return rows[0];
}

async function insertMessageTag({ accessToken, messageId, tagId }) {
  await requestJson(`${SUPABASE_URL}/rest/v1/message_tags`, {
    method: "POST",
    headers: {
      ...buildRestHeaders(accessToken),
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message_id: messageId, tag_id: tagId }),
  });
}

async function insertReminder({ accessToken, userId, body, remindAt }) {
  await requestJson(`${SUPABASE_URL}/rest/v1/reminders`, {
    method: "POST",
    headers: {
      ...buildRestHeaders(accessToken),
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      user_id: userId,
      body,
      remind_at: remindAt.toISOString(),
    }),
  });
}

function buildRestHeaders(accessToken) {
  return {
    apikey: SUPABASE_ANON_KEY,
    Authorization: `Bearer ${accessToken}`,
  };
}

async function requestJson(url, options = {}) {
  const response = await fetch(url, options);
  const text = await response.text();
  const data = text ? safeJsonParse(text) : null;

  if (!response.ok) {
    const message =
      (data && typeof data === "object" && (data.message || data.error_description || data.error)) ||
      `${response.status} ${response.statusText}`;
    throw new Error(`Request failed for ${url}: ${message}`);
  }

  return data ?? [];
}

function safeJsonParse(text) {
  try {
    return JSON.parse(text);
  } catch {
    return text;
  }
}

function buildMessageMarkdown(message, tags) {
  const frontmatter = {
    title: `MindChuk Message ${timestampLabel(message.sent_at)}`,
    source: "mindchuk",
    mindchuk_kind: "message",
    mindchuk_id: message.id,
    sent_at: message.sent_at,
    content_type: message.content_type ?? "note",
    done: Boolean(message.done),
    pinned: Boolean(message.pinned),
    pinned_at: message.pinned_at ?? "",
    tags: tags.map((tag) => tag.name),
    sms_keywords: message.sms_keywords ?? [],
    contains_url: Boolean(message.contains_url),
    extracted_urls: message.extracted_urls ?? (message.extracted_url ? [message.extracted_url] : []),
    media_url: message.media_url ?? "",
    media_content_type: message.media_content_type ?? "",
  };

  const sections = [];
  if (message.body) {
    sections.push(message.body.trim());
  }

  if (Array.isArray(message.todo_items) && message.todo_items.length > 0) {
    sections.push(
      [
        "## Todo Items",
        ...message.todo_items.map((item) => `- [${item.checked ? "x" : " "}] ${item.text}`),
      ].join("\n"),
    );
  }

  if (tags.length > 0) {
    sections.push(["## Tags", ...tags.map((tag) => `- ${tag.name}`)].join("\n"));
  }

  const urls = frontmatter.extracted_urls;
  if (urls.length > 0) {
    sections.push(["## Links", ...urls.map((url) => `- ${url}`)].join("\n"));
  }

  if (message.media_url) {
    sections.push(["## Media", `- ${message.media_url}`].join("\n"));
  }

  return serializeMarkdown(frontmatter, sections.join("\n\n"));
}

function buildReminderMarkdown(reminder) {
  const frontmatter = {
    title: `MindChuk Reminder ${timestampLabel(reminder.remind_at)}`,
    source: "mindchuk",
    mindchuk_kind: "reminder",
    mindchuk_id: reminder.id,
    remind_at: reminder.remind_at,
  };

  return serializeMarkdown(frontmatter, reminder.body?.trim() ?? "");
}

function buildAgentMarkdown(message, tags) {
  const prompt = extractAgentPrompt(message.body ?? "");
  const frontmatter = {
    title: `MindChuk Agent Prompt ${timestampLabel(message.sent_at)}`,
    status: "pending",
    source: "mindchuk",
    mindchuk_kind: "agent_command",
    source_message_id: message.id,
    sent_at: message.sent_at,
    tags: tags.map((tag) => tag.name),
  };

  const sections = [
    "## Prompt",
    prompt || "(empty prompt)",
    "",
    "## Original Message",
    message.body?.trim() || "(empty body)",
  ];

  return serializeMarkdown(frontmatter, sections.join("\n"));
}

function buildMirrorIndex({ profile, messages, reminders, agentMessages }) {
  const lines = [
    "---",
    "title: MindChuk Mirror",
    "description: Generated mirror of MindChuk messages, reminders, and agent prompts",
    `last_updated: ${new Date().toISOString()}`,
    "---",
    "",
    "# MindChuk Mirror",
    "",
    `- Last sync: ${new Date().toLocaleString("en-US")}`,
    `- Messages: ${messages.length}`,
    `- Reminders: ${reminders.length}`,
    `- Agent command candidates: ${agentMessages.length}`,
  ];

  if (profile?.phone) {
    lines.push(`- MindChuk phone: ${profile.phone}`);
  }

  lines.push(
    "",
    "## Folders",
    "",
    "- [Messages](messages/)",
    "- [Reminders](reminders/)",
    "- [Agent Inbox](../agent-inbox/_index.md)",
  );

  if (messages.length > 0) {
    lines.push("", "## Recent Messages", "");
    for (const message of messages.slice(-10).reverse()) {
      lines.push(
        `- [${timestampLabel(message.sent_at)}](${toPosixPath(messageRelativePath(message))}) - ${excerpt(message.body)}`,
      );
    }
  }

  if (reminders.length > 0) {
    lines.push("", "## Upcoming Reminders", "");
    for (const reminder of reminders.slice(0, 10)) {
      lines.push(
        `- [${timestampLabel(reminder.remind_at)}](${toPosixPath(reminderRelativePath(reminder))}) - ${excerpt(reminder.body)}`,
      );
    }
  }

  return lines.join("\n") + "\n";
}

async function buildAgentIndex(agentDir) {
  const pendingRecords = await listAgentTaskRecords(path.join(agentDir, "pending"));
  const processingRecords = await listAgentTaskRecords(path.join(agentDir, "processing"));
  const completedRecords = await listAgentTaskRecords(path.join(agentDir, "completed"));
  const failedRecords = await listAgentTaskRecords(path.join(agentDir, "failed"));
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
    "This queue only becomes automatic when the local runner is active on this machine.",
  ];

  lines.push(...(await buildAgentIndexSection("Pending", pendingRecords, agentDir, "No pending agent-style prompts were found on the last refresh.")));
  lines.push(...(await buildAgentIndexSection("Processing", processingRecords, agentDir, "No agent tasks are currently in processing.")));
  lines.push(...(await buildAgentIndexSection("Recent Completed", completedRecords.slice(0, 5), agentDir, "No completed agent runs yet.")));
  lines.push(...(await buildAgentIndexSection("Recent Failed", failedRecords.slice(0, 5), agentDir, "No failed agent runs yet.")));

  return lines.join("\n") + "\n";
}

async function buildAgentIndexSection(title, records, baseDir, emptyMessage) {
  const lines = ["", `## ${title}`, ""];
  if (records.length === 0) {
    lines.push(`- ${emptyMessage}`);
    return lines;
  }

  for (const item of await buildAgentIndexItems(records, baseDir)) {
    lines.push(`- [${item.label}](${item.link}) - ${item.summary}`);
  }

  return lines;
}

async function buildAgentIndexItems(records, baseDir) {
  const items = [];
  for (const record of records) {
    const { filePath, parsed } = record;
    const label = String(parsed.frontmatter.title ?? path.basename(filePath, ".md"));
    const summary = excerpt(extractAgentPrompt(extractPromptFromTask(parsed.body) || parsed.body), 90);
    const link = toPosixPath(path.relative(baseDir, filePath));
    items.push({ label, summary, link });
  }
  return items;
}

function serializeMarkdown(frontmatter, body) {
  const yaml = serializeFrontmatter(frontmatter);
  return `${yaml}\n${body.trim()}\n`;
}

function serializeFrontmatter(frontmatter) {
  const lines = ["---"];
  for (const [key, value] of Object.entries(frontmatter)) {
    lines.push(...serializeYamlEntry(key, value));
  }
  lines.push("---", "");
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
  if (value.startsWith("[") && value.endsWith("]")) {
    return value
      .slice(1, -1)
      .split(",")
      .map((item) => item.trim())
      .filter(Boolean)
      .map((item) => parseYamlScalar(item));
  }
  if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
    return value.slice(1, -1).replace(/\\"/g, '"').replace(/\\\\/g, "\\");
  }
  return value;
}

function parseTagList(value) {
  if (Array.isArray(value)) {
    return value.map(String);
  }
  if (typeof value === "string") {
    return value
      .split(",")
      .map((item) => item.trim())
      .filter(Boolean);
  }
  return [];
}

function parseOptionalDate(value) {
  if (!value || typeof value !== "string") {
    return null;
  }
  const parsed = new Date(value);
  return Number.isNaN(parsed.getTime()) ? null : parsed;
}

function parseTodoItems(body) {
  const items = [];
  for (const line of body.split(/\r?\n/)) {
    const match = /^-\s+\[([ xX])\]\s+(.*)$/.exec(line.trim());
    if (!match) {
      continue;
    }
    items.push({
      text: match[2].trim(),
      checked: match[1].toLowerCase() === "x",
    });
  }
  return items.filter((item) => item.text);
}

function extractMessageBody(body, todoItems) {
  if (todoItems.length === 0) {
    return body.trim();
  }

  const remainingLines = body
    .split(/\r?\n/)
    .filter((line) => !/^-\s+\[([ xX])\]\s+/.test(line.trim()))
    .join("\n")
    .trim();

  return remainingLines;
}

function buildReminderFallback(body) {
  const trimmed = body.trim();
  return trimmed || "Reminder from Obsidian outbox";
}

function normalizeContentType(value) {
  if (typeof value !== "string") {
    return null;
  }
  const normalized = value.trim().toLowerCase();
  return ["note", "todo"].includes(normalized) ? normalized : null;
}

function normalizeTagName(value) {
  return String(value ?? "")
    .toUpperCase()
    .replace(/[^A-Z0-9]/g, "")
    .trim();
}

function extractUrls(text) {
  return [...new Set((text.match(/https?:\/\/[^\s)]+/g) ?? []).map((url) => url.trim()))];
}

function isAgentCommand(message, tags) {
  const tagNames = new Set(tags.map((tag) => normalizeTagName(tag.name)));
  if (tagNames.has(CODEX_RESULT_TAG)) {
    return false;
  }
  if (tagNames.has(AGENT_TAG)) {
    return true;
  }
  const trimmedBody = (message.body ?? "").trim();
  if (/^\[codex\s+(agent|result)\b/i.test(trimmedBody)) {
    return false;
  }
  return /^\/(agent|codex)\b/i.test(trimmedBody);
}

function extractAgentPrompt(body) {
  return body
    .trim()
    .replace(/^\/(agent|codex)\s*/i, "")
    .trim();
}

function messageRelativePath(message) {
  const stamp = safeTimestamp(message.sent_at ?? new Date().toISOString());
  const year = stamp.slice(0, 4);
  const month = stamp.slice(5, 7);
  return path.join("messages", year, month, `${stamp}--${message.id}.md`);
}

function reminderRelativePath(reminder) {
  const stamp = safeTimestamp(reminder.remind_at ?? new Date().toISOString());
  const year = stamp.slice(0, 4);
  const month = stamp.slice(5, 7);
  return path.join("reminders", year, month, `${stamp}--${reminder.id}.md`);
}

function agentRelativeFile(message) {
  return path.join("pending", `${safeTimestamp(message.sent_at ?? new Date().toISOString())}--${message.id}.md`);
}

function safeTimestamp(value) {
  const parsed = new Date(value);
  const iso = Number.isNaN(parsed.getTime()) ? new Date().toISOString() : parsed.toISOString();
  return iso.replace(/:/g, "-");
}

function timestampLabel(value) {
  const parsed = new Date(value);
  if (Number.isNaN(parsed.getTime())) {
    return String(value ?? "");
  }
  return parsed.toLocaleString("en-US");
}

function excerpt(value, length = 90) {
  const source = String(value ?? "").replace(/\s+/g, " ").trim();
  if (!source) {
    return "(empty)";
  }
  if (source.length <= length) {
    return source;
  }
  return `${source.slice(0, length - 3)}...`;
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

async function collectKnownAgentTasks(agentDir) {
  const allIds = new Set();
  for (const folder of ["pending", "processing", "completed", "failed"]) {
    const targetDir = path.join(agentDir, folder);
    const records = await listAgentTaskRecords(targetDir);
    for (const record of records) {
      const sourceMessageId = String(record.parsed.frontmatter.source_message_id ?? "").trim();
      if (sourceMessageId) {
        allIds.add(sourceMessageId);
      }
    }
  }
  return { allIds };
}

function extractPromptFromTask(body) {
  const normalized = body.replace(/\r\n/g, "\n");
  const match = /## Prompt\s*\n([\s\S]*?)(?:\n## |\s*$)/.exec(normalized);
  if (match?.[1]) {
    return match[1].trim();
  }
  return normalized.trim();
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

async function cleanGeneratedMarkdown(baseDir, expectedRelativePaths) {
  if (!(await pathExists(baseDir))) {
    return;
  }

  const files = await listMarkdownFiles(baseDir);
  for (const filePath of files) {
    const relativePath = path.relative(baseDir, filePath);
    if (path.basename(filePath) === "_index.md") {
      continue;
    }
    if (!expectedRelativePaths.has(relativePath)) {
      await rm(filePath, { force: true });
    }
  }
}

async function ensureDir(dirPath) {
  await mkdir(dirPath, { recursive: true });
}

async function pathExists(targetPath) {
  try {
    await stat(targetPath);
    return true;
  } catch {
    return false;
  }
}

function toPosixPath(value) {
  return value.split(path.sep).join("/");
}
