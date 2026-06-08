param(
  [Parameter(Mandatory = $true)]
  [string]$Email,

  [Parameter(Mandatory = $true)]
  [string]$Password,

  [int]$PollSeconds = 60,

  [string]$ExecutionSandbox = "workspace-write",

  [string]$CodexPath = "",

  [switch]$DisableDangerFallback
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$runnerScript = Join-Path $scriptDir "run_mindchuk_agent_runner.ps1"
$agentInboxDir = Join-Path $scriptDir "agent-inbox"
$logsDir = Join-Path $agentInboxDir "logs"
$pidFile = Join-Path $agentInboxDir "runner.pid"
$timestamp = Get-Date -Format "yyyyMMdd-HHmmss"
$stdoutLog = Join-Path $logsDir "runner-$timestamp.stdout.log"
$stderrLog = Join-Path $logsDir "runner-$timestamp.stderr.log"

New-Item -ItemType Directory -Force -Path $logsDir | Out-Null

$nodeCommand = Get-Command node -ErrorAction SilentlyContinue
if (-not $nodeCommand) {
  throw "Node.js was not found on PATH. Install Node.js or set MINDCHUK_NODE_PATH before starting the runner."
}

$resolvedCodexPath = $CodexPath
if (-not $resolvedCodexPath) {
  $resolvedCodexPath = $env:MINDCHUK_CODEX_PATH
}
if (-not $resolvedCodexPath) {
  $defaultCodexPath = "C:\Users\shiva\.vscode\extensions\openai.chatgpt-26.527.31454-win32-x64\bin\windows-x86_64\codex.exe"
  if (Test-Path -LiteralPath $defaultCodexPath) {
    $resolvedCodexPath = $defaultCodexPath
  }
}
if (-not $resolvedCodexPath) {
  $codexCommand = Get-Command codex -ErrorAction SilentlyContinue
  if (-not $codexCommand) {
    throw "Codex was not found. Pass -CodexPath or set MINDCHUK_CODEX_PATH before starting the runner."
  }
  $resolvedCodexPath = $codexCommand.Source
}
if (-not (Test-Path -LiteralPath $resolvedCodexPath)) {
  throw "Codex executable was not found at $resolvedCodexPath."
}

$env:MINDCHUK_EMAIL = $Email
$env:MINDCHUK_PASSWORD = $Password
$env:MINDCHUK_AGENT_POLL_SECONDS = [string]$PollSeconds
$env:MINDCHUK_CODEX_SANDBOX = $ExecutionSandbox
$env:MINDCHUK_CODEX_ALLOW_DANGER_FALLBACK = if ($DisableDangerFallback) { "false" } else { "true" }
$env:MINDCHUK_NODE_PATH = $nodeCommand.Source
$env:MINDCHUK_CODEX_PATH = $resolvedCodexPath

$existing = $null
if (Test-Path -LiteralPath $pidFile) {
  $existing = Get-Content -LiteralPath $pidFile -ErrorAction SilentlyContinue
}

if ($existing) {
  $existingProc = Get-Process -Id $existing -ErrorAction SilentlyContinue
  if ($existingProc) {
    $existingCommandLine = ""
    try {
      $existingCommandLine = (Get-CimInstance Win32_Process -Filter "ProcessId = $existing").CommandLine
    } catch {
      $existingCommandLine = ""
    }

    if ($existingProc.ProcessName -like "powershell*" -and $existingCommandLine -like "*run_mindchuk_agent_runner.ps1*") {
      throw "Runner already appears to be running with PID $existing."
    }
  }

  Remove-Item -LiteralPath $pidFile -Force -ErrorAction SilentlyContinue
}

$process = Start-Process `
  -FilePath "powershell.exe" `
  -ArgumentList @(
    "-NoLogo",
    "-NoProfile",
    "-ExecutionPolicy", "Bypass",
    "-File", $runnerScript,
    "watch"
  ) `
  -WindowStyle Hidden `
  -PassThru `
  -RedirectStandardOutput $stdoutLog `
  -RedirectStandardError $stderrLog

Start-Sleep -Seconds 3
$running = Get-Process -Id $process.Id -ErrorAction SilentlyContinue
if (-not $running) {
  throw "Runner exited immediately. Check logs:`nstdout: $stdoutLog`nstderr: $stderrLog"
}

Set-Content -LiteralPath $pidFile -Value $process.Id

Write-Output "Started MindChuk agent runner."
Write-Output "PID: $($process.Id)"
Write-Output "stdout: $stdoutLog"
Write-Output "stderr: $stderrLog"
