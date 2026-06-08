$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pidFile = Join-Path (Join-Path $scriptDir "agent-inbox") "runner.pid"

if (-not (Test-Path -LiteralPath $pidFile)) {
  Write-Output "No runner.pid file found."
  exit 0
}

$runnerPid = Get-Content -LiteralPath $pidFile -ErrorAction SilentlyContinue
if (-not $runnerPid) {
  Remove-Item -LiteralPath $pidFile -Force -ErrorAction SilentlyContinue
  Write-Output "Removed empty runner.pid file."
  exit 0
}

$process = Get-Process -Id $runnerPid -ErrorAction SilentlyContinue
if ($process) {
  Stop-Process -Id $runnerPid -Force
  Write-Output "Stopped MindChuk agent runner PID $runnerPid."
} else {
  Write-Output "No running process found for PID $runnerPid."
}

Remove-Item -LiteralPath $pidFile -Force -ErrorAction SilentlyContinue
