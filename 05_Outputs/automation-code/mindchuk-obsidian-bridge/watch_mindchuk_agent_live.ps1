param(
  [int]$RefreshSeconds = 2,
  [int]$MaxLines = 12,
  [int]$Iterations = 0
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$agentInboxDir = Join-Path $scriptDir "agent-inbox"
$pendingDir = Join-Path $agentInboxDir "pending"
$processingDir = Join-Path $agentInboxDir "processing"
$completedDir = Join-Path $agentInboxDir "completed"
$failedDir = Join-Path $agentInboxDir "failed"
$runsDir = Join-Path $agentInboxDir "runs"
$logsDir = Join-Path $agentInboxDir "logs"

function Get-SortedMarkdownFiles {
  param(
    [string]$Path
  )

  if (-not (Test-Path -LiteralPath $Path)) {
    return @()
  }

  return @(Get-ChildItem -LiteralPath $Path -Filter "*.md" -File -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending)
}

function Get-TaskMetadata {
  param(
    [string]$Path
  )

  $title = ""
  $preview = ""
  $inFrontmatter = $false
  $frontmatterStarted = $false

  foreach ($line in Get-Content -LiteralPath $Path -TotalCount 60 -ErrorAction SilentlyContinue) {
    if (-not $frontmatterStarted) {
      if ($line -eq "---") {
        $frontmatterStarted = $true
        $inFrontmatter = $true
        continue
      }
      break
    }

    if ($inFrontmatter -and $line -eq "---") {
      break
    }

    if ($line -match "^title:\s*(.+)$") {
      $title = $matches[1].Trim()
      continue
    }

    if ($line -match "^source_preview:\s*(.+)$") {
      $preview = $matches[1].Trim()
      continue
    }
  }

  return @{
    Title = $title
    Preview = $preview
  }
}

function Get-LatestRunDirectory {
  param(
    [string]$TaskId
  )

  if (-not $TaskId -or -not (Test-Path -LiteralPath $runsDir)) {
    return $null
  }

  return Get-ChildItem -LiteralPath $runsDir -Directory -ErrorAction SilentlyContinue |
    Where-Object { $_.Name -like "$TaskId--attempt-*" } |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1
}

function Get-LatestRunnerStdoutLog {
  if (-not (Test-Path -LiteralPath $logsDir)) {
    return $null
  }

  return Get-ChildItem -LiteralPath $logsDir -Filter "*.stdout.log" -File -ErrorAction SilentlyContinue |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1
}

function Get-RecentFileText {
  param(
    [string]$Path,
    [int]$TailLines = 12
  )

  if (-not (Test-Path -LiteralPath $Path)) {
    return @("(not written yet)")
  }

  $content = Get-Content -LiteralPath $Path -Tail $TailLines -ErrorAction SilentlyContinue
  if (-not $content) {
    return @("(empty)")
  }

  return @($content)
}

function Write-Section {
  param(
    [string]$Title,
    [string[]]$Lines
  )

  Write-Host ""
  Write-Host $Title -ForegroundColor Cyan
  Write-Host ("-" * $Title.Length) -ForegroundColor DarkCyan

  foreach ($line in $Lines) {
    Write-Host $line
  }
}

function Get-LatestTaskFile {
  $completed = Get-SortedMarkdownFiles -Path $completedDir | Select-Object -First 1
  $failed = Get-SortedMarkdownFiles -Path $failedDir | Select-Object -First 1

  if ($completed -and $failed) {
    if ($completed.LastWriteTime -ge $failed.LastWriteTime) {
      return @{ File = $completed; Status = "completed" }
    }

    return @{ File = $failed; Status = "failed" }
  }

  if ($completed) {
    return @{ File = $completed; Status = "completed" }
  }

  if ($failed) {
    return @{ File = $failed; Status = "failed" }
  }

  return $null
}

$completedIterations = 0

while ($true) {
  $pending = Get-SortedMarkdownFiles -Path $pendingDir
  $processing = Get-SortedMarkdownFiles -Path $processingDir
  $completed = Get-SortedMarkdownFiles -Path $completedDir
  $failed = Get-SortedMarkdownFiles -Path $failedDir

  $activeTask = $processing | Select-Object -First 1
  $activeStatus = "idle"
  $taskFile = $null

  if ($activeTask) {
    $taskFile = $activeTask
    $activeStatus = "processing"
  } else {
    $latestTask = Get-LatestTaskFile
    if ($latestTask) {
      $taskFile = $latestTask.File
      $activeStatus = $latestTask.Status
    }
  }

  $runDirectory = $null
  $taskMetadata = $null
  $taskId = ""

  if ($taskFile) {
    $taskId = [System.IO.Path]::GetFileNameWithoutExtension($taskFile.Name)
    $runDirectory = Get-LatestRunDirectory -TaskId $taskId
    $taskMetadata = Get-TaskMetadata -Path $taskFile.FullName
  }

  Clear-Host
  Write-Host "MindChuk Agent Live View" -ForegroundColor Green
  Write-Host "Updated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor DarkGray
  Write-Host "Press Ctrl+C to stop."

  Write-Section -Title "Queue" -Lines @(
    "Pending: $($pending.Count)",
    "Processing: $($processing.Count)",
    "Completed: $($completed.Count)",
    "Failed: $($failed.Count)"
  )

  $taskLines = @()
  if ($taskFile) {
    $taskLines += "Status: $activeStatus"
    $taskLines += "Task file: $($taskFile.Name)"
    if ($taskMetadata.Title) {
      $taskLines += "Title: $($taskMetadata.Title)"
    }
    if ($taskMetadata.Preview) {
      $taskLines += "Prompt preview: $($taskMetadata.Preview)"
    }
    $taskLines += "Last updated: $($taskFile.LastWriteTime)"
  } else {
    $taskLines += "No task files have been created yet."
  }
  Write-Section -Title "Task" -Lines $taskLines

  $runLines = @()
  if ($runDirectory) {
    $runLines += "Run directory: $($runDirectory.FullName)"
    $runLines += "Last updated: $($runDirectory.LastWriteTime)"
  } else {
    $runLines += "No run directory detected yet."
  }
  Write-Section -Title "Run" -Lines $runLines

  if ($runDirectory) {
    Write-Section -Title "Refine Output" -Lines (Get-RecentFileText -Path (Join-Path $runDirectory.FullName "refine-stdout.log") -TailLines $MaxLines)
    Write-Section -Title "Execute Output" -Lines (Get-RecentFileText -Path (Join-Path $runDirectory.FullName "execute-stdout.log") -TailLines $MaxLines)
    Write-Section -Title "Final Message" -Lines (Get-RecentFileText -Path (Join-Path $runDirectory.FullName "last-message.md") -TailLines $MaxLines)

    $successNote = Join-Path $runDirectory.FullName "success-note.md"
    $blockerNote = Join-Path $runDirectory.FullName "blocker-note.md"
    if (Test-Path -LiteralPath $successNote) {
      Write-Section -Title "Success Note" -Lines (Get-RecentFileText -Path $successNote -TailLines $MaxLines)
    } elseif (Test-Path -LiteralPath $blockerNote) {
      Write-Section -Title "Blocker Note" -Lines (Get-RecentFileText -Path $blockerNote -TailLines $MaxLines)
    }
  }

  $runnerLog = Get-LatestRunnerStdoutLog
  $runnerLines = @()
  if ($runnerLog) {
    $runnerLines += "Log file: $($runnerLog.FullName)"
    $runnerLines += ""
    $runnerLines += Get-RecentFileText -Path $runnerLog.FullName -TailLines $MaxLines
  } else {
    $runnerLines += "No runner stdout log exists yet."
  }
  Write-Section -Title "Runner Log" -Lines $runnerLines

  $completedIterations += 1
  if ($Iterations -gt 0 -and $completedIterations -ge $Iterations) {
    break
  }

  Start-Sleep -Seconds $RefreshSeconds
}
