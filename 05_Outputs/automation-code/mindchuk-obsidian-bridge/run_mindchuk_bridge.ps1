param(
  [ValidateSet("help", "pull", "push", "sync")]
  [string]$Command = "sync"
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$scriptPath = Join-Path $scriptDir "mindchuk_bridge.mjs"
$nodePath = $env:MINDCHUK_NODE_PATH

if (-not $nodePath) {
  $nodeCommand = Get-Command node -ErrorAction SilentlyContinue
  if (-not $nodeCommand) {
    throw "Node.js was not found on PATH. Set MINDCHUK_NODE_PATH or install Node.js."
  }
  $nodePath = $nodeCommand.Source
}

& $nodePath $scriptPath $Command @args
