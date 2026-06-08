param(
  [string]$HtmlFile = "clinicalhours_tiktok_carousel.html",
  [string]$VersionSuffix = "v1",
  [switch]$RunQa,
  [switch]$GenerateQaShots
)

$ErrorActionPreference = "Stop"

$baseDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectDir = Split-Path -Parent $baseDir
$htmlPath = Join-Path $baseDir $HtmlFile

$browserCandidates = @(
  "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
  "C:\Program Files\Microsoft\Edge\Application\msedge.exe",
  "C:\Program Files\Google\Chrome\Application\chrome.exe",
  "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
)

$browserPath = $browserCandidates | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $browserPath) {
  throw "No supported headless browser found."
}

$copyAuditScript = Join-Path $baseDir "audit_clinicalhours_tiktok_copy.ps1"
$auditProfile = $null
if (Test-Path $copyAuditScript) {
  $htmlBaseName = [System.IO.Path]::GetFileNameWithoutExtension($htmlPath)
  $auditProfile = if ($htmlBaseName -match "^clinicalhours_tiktok_student_") {
    "bright_student"
  } elseif ($htmlBaseName -match "^clinicalhours_tiktok_(carousel|clinic_)") {
    "clinic_ops_primary"
  } else {
    "generic"
  }
  Write-Host "Running copy and asset audit ($auditProfile)"
  & $copyAuditScript -HtmlFile $htmlPath -Profile $auditProfile
}

$baseUri = ([System.Uri]$htmlPath).AbsoluteUri
$tempDir = Join-Path $baseDir ".render-temp"
$outputDir = Join-Path $projectDir ("exports\\{0}" -f $VersionSuffix)
$qaShotDir = Join-Path $projectDir "qa\\screenshots"
$reviewBundleDir = Join-Path $projectDir "qa\\review_bundles"
New-Item -ItemType Directory -Force -Path $tempDir | Out-Null
New-Item -ItemType Directory -Force -Path $outputDir | Out-Null
New-Item -ItemType Directory -Force -Path $qaShotDir | Out-Null
New-Item -ItemType Directory -Force -Path $reviewBundleDir | Out-Null

$slideArtifacts = @()

Write-Host "Rendering carousel from $htmlPath"
Write-Host "Using browser: $browserPath"

for ($slide = 1; $slide -le 5; $slide++) {
  $outputPath = Join-Path $outputDir ("clinicalhours_tiktok_slide_{0}_{1}.png" -f $slide, $VersionSuffix)
  $url = "${baseUri}?slide=$slide&export=1"
  $stdoutPath = Join-Path $tempDir ("render-slide-{0}-stdout.txt" -f $slide)
  $stderrPath = Join-Path $tempDir ("render-slide-{0}-stderr.txt" -f $slide)

  if (Test-Path $stdoutPath) { Remove-Item $stdoutPath -Force }
  if (Test-Path $stderrPath) { Remove-Item $stderrPath -Force }

  $renderProc = Start-Process -FilePath $browserPath -ArgumentList @(
    "--headless",
    "--disable-gpu",
    "--hide-scrollbars",
    "--window-size=1080,1920",
    "--screenshot=$outputPath",
    $url
  ) -Wait -PassThru -NoNewWindow -RedirectStandardOutput $stdoutPath -RedirectStandardError $stderrPath

  if ($renderProc.ExitCode -ne 0) {
    throw "Render failed for slide $slide"
  }

  Write-Host "Rendered $outputPath"

  $qaUrl = "${url}&qa=1"
  $qaStdout = Join-Path $tempDir ("qa-slide-{0}-stdout.html" -f $slide)
  $qaStderr = Join-Path $tempDir ("qa-slide-{0}-stderr.txt" -f $slide)

  if (Test-Path $qaStdout) { Remove-Item $qaStdout -Force }
  if (Test-Path $qaStderr) { Remove-Item $qaStderr -Force }

  $qaProc = Start-Process -FilePath $browserPath -ArgumentList @(
    "--headless",
    "--disable-gpu",
    "--dump-dom",
    $qaUrl
  ) -Wait -PassThru -NoNewWindow -RedirectStandardOutput $qaStdout -RedirectStandardError $qaStderr

  $qaDom = ""
  if (Test-Path $qaStdout) {
    $qaDom += Get-Content $qaStdout -Raw
  }
  if (Test-Path $qaStderr) {
    $qaDom += "`n" + (Get-Content $qaStderr -Raw)
  }
  if (-not $qaDom) {
    throw "QA DOM dump failed for slide $slide"
  }

  $qaMatch = [regex]::Matches($qaDom, '<pre class="guide-report">([^<]+)</pre>') | Select-Object -First 1
  if (-not $qaMatch) {
    throw "QA report not found for slide $slide"
  }

  $qaLine = $qaMatch.Groups[1].Value
  $qaText = $qaLine -replace '\\n', [Environment]::NewLine

  if ($qaText -match "QA WARN") {
    throw "QA failed for slide $slide`n$qaText"
  }

  if ($RunQa) {
    Write-Host ""
    Write-Host "QA slide $slide"
    Write-Host $qaText
    Write-Host ""
  }

  if ($GenerateQaShots) {
    $qaShotPath = Join-Path $qaShotDir ("_qa_slide_{0}_{1}.png" -f $slide, $VersionSuffix)
    $qaShotStdout = Join-Path $tempDir ("qa-shot-slide-{0}-stdout.txt" -f $slide)
    $qaShotStderr = Join-Path $tempDir ("qa-shot-slide-{0}-stderr.txt" -f $slide)

    if (Test-Path $qaShotStdout) { Remove-Item $qaShotStdout -Force }
    if (Test-Path $qaShotStderr) { Remove-Item $qaShotStderr -Force }

    $qaShotProc = Start-Process -FilePath $browserPath -ArgumentList @(
      "--headless",
      "--disable-gpu",
      "--hide-scrollbars",
      "--window-size=1080,1920",
      "--screenshot=$qaShotPath",
      $qaUrl
    ) -Wait -PassThru -NoNewWindow -RedirectStandardOutput $qaShotStdout -RedirectStandardError $qaShotStderr

    if ($qaShotProc.ExitCode -ne 0) {
      throw "QA screenshot failed for slide $slide"
    }

    Write-Host "Rendered $qaShotPath"
  }
  else {
    $qaShotPath = $null
  }

  $slideArtifacts += [pscustomobject]@{
    slide = $slide
    exportPath = $outputPath
    exportUrl = $url
    qaUrl = $qaUrl
    qaReport = $qaText
    qaScreenshotPath = $qaShotPath
    width = $null
    height = $null
  }
}

if (Test-Path $tempDir) {
  Remove-Item $tempDir -Recurse -Force
}

Add-Type -AssemblyName System.Drawing
$exports = Get-ChildItem $outputDir -Filter ("clinicalhours_tiktok_slide_*_{0}.png" -f $VersionSuffix) | Sort-Object Name

Write-Host "Dimension check"
foreach ($file in $exports) {
  $img = [System.Drawing.Image]::FromFile($file.FullName)
  try {
    Write-Host ("- {0}: {1} x {2}" -f $file.Name, $img.Width, $img.Height)
    $artifact = $slideArtifacts | Where-Object { $_.exportPath -eq $file.FullName } | Select-Object -First 1
    if ($artifact) {
      $artifact.width = $img.Width
      $artifact.height = $img.Height
    }
    if ($img.Width -ne 1080 -or $img.Height -ne 1920) {
      throw "Dimension mismatch for $($file.Name)"
    }
  }
  finally {
    $img.Dispose()
  }
}

$reviewBundlePath = Join-Path $reviewBundleDir ("clinicalhours_tiktok_review_bundle_{0}.json" -f $VersionSuffix)
$reviewBundle = [pscustomobject]@{
  schemaVersion = "clinicalhours_tiktok/review_bundle/v1"
  generatedAt = (Get-Date).ToString("o")
  versionSuffix = $VersionSuffix
  htmlFile = $HtmlFile
  htmlPath = $htmlPath
  outputDir = $outputDir
  qaScreenshotDir = $qaShotDir
  runQa = [bool]$RunQa
  generatedQaShots = [bool]$GenerateQaShots
  copyAuditProfile = $auditProfile
  slides = $slideArtifacts
}
$reviewBundle | ConvertTo-Json -Depth 6 | Set-Content $reviewBundlePath -Encoding UTF8
Write-Host "Wrote $reviewBundlePath"

Write-Host "Render complete."
