param(
  [string]$ConfigPath = (Join-Path $PSScriptRoot "felt_tiktok_pipeline_config.json"),
  [string]$SpecPath = (Join-Path $PSScriptRoot "specs\\felt_tiktok_v5_candidate_deck_spec.json"),
  [string]$VersionSuffix,
  [switch]$SkipRender,
  [switch]$PrepareEmail
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Get-ObsidianRoot {
  return (Resolve-Path (Join-Path $PSScriptRoot "..\\..\\..\\..")).Path
}

function Resolve-FromRoot {
  param(
    [string]$Root,
    [string]$RelativePath
  )

  return (Join-Path $Root ($RelativePath -replace "/", "\"))
}

function New-Directory {
  param([string]$Path)
  New-Item -ItemType Directory -Force -Path $Path | Out-Null
}

function Write-JsonFile {
  param(
    [string]$Path,
    $Data
  )

  $json = $Data | ConvertTo-Json -Depth 12
  Set-Content -Path $Path -Value $json -Encoding UTF8
}

function Get-WordCount {
  param([string]$Text)

  if (-not $Text) {
    return 0
  }

  $normalized = $Text.ToLower()
  $normalized = $normalized -replace "<br\s*/?>", " "
  $normalized = $normalized -replace "[^a-z0-9'\- ]", " "
  $words = $normalized.Split(" ", [System.StringSplitOptions]::RemoveEmptyEntries)
  return $words.Count
}

function Test-ContainsAny {
  param(
    [string]$Text,
    [string[]]$Terms
  )

  $lower = $Text.ToLower()
  foreach ($term in $Terms) {
    if ($lower.Contains($term.ToLower())) {
      return $true
    }
  }
  return $false
}

function Get-MatchedTerms {
  param(
    [string]$Text,
    [string[]]$Terms
  )

  $matches = @()
  $lower = $Text.ToLower()
  foreach ($term in $Terms) {
    if ($lower.Contains($term.ToLower())) {
      $matches += $term
    }
  }
  return @($matches)
}

function Clamp-Score {
  param([double]$Score)

  if ($Score -lt 1) { return 1 }
  if ($Score -gt 5) { return 5 }
  return [math]::Round($Score, 2)
}

function Get-ExpectedProofTokens {
  param([string]$Role)

  switch ($Role) {
    "friction" { return @("home") }
    "simplification" { return @("lobby", "join", "code") }
    "operational_proof" { return @("guided", "live", "table") }
    "mastery" { return @("training", "feedback", "review", "guided") }
    "return" { return @("home", "lobby", "return") }
    default { return @() }
  }
}

function Get-RoleKeywords {
  param([string]$Role)

  switch ($Role) {
    "friction" { return @("home", "mess", "night", "place") }
    "simplification" { return @("code", "crew", "host", "join", "rejoin") }
    "operational_proof" { return @("room", "turn", "stacks", "action", "clear") }
    "mastery" { return @("train", "review", "leaks", "spots", "progress") }
    "return" { return @("return", "home base", "invite", "crew", "reason to return") }
    default { return @() }
  }
}

function Test-RoleFit {
  param(
    [pscustomobject]$SlideSpec
  )

  $copyText = @($SlideSpec.eyebrow, $SlideSpec.headline, $SlideSpec.subtext) -join " "
  $keywordMatches = @(Get-MatchedTerms -Text $copyText -Terms (Get-RoleKeywords -Role $SlideSpec.intended_role))
  $proofTokens = Get-ExpectedProofTokens -Role $SlideSpec.intended_role
  $proofPaths = @($SlideSpec.hero_source) + @($SlideSpec.support_sources)
  $proofMatch = $false

  foreach ($proofPath in $proofPaths) {
    foreach ($token in $proofTokens) {
      if ($proofPath.ToLower().Contains($token.ToLower())) {
        $proofMatch = $true
      }
    }
  }

  return [pscustomobject]@{
    passed = (($keywordMatches.Count -gt 0) -or $proofMatch)
    keyword_matches = $keywordMatches
    proof_match = $proofMatch
  }
}

function Get-ImageDimensions {
  param([string]$Path)

  Add-Type -AssemblyName System.Drawing
  $img = [System.Drawing.Image]::FromFile($Path)
  try {
    return [pscustomobject]@{
      width = $img.Width
      height = $img.Height
    }
  }
  finally {
    $img.Dispose()
  }
}

function Get-StyleScore {
  param([string]$StyleProfile)

  switch ($StyleProfile) {
    "premium_dark_restrained" { return 5 }
    default { return 4 }
  }
}

function Get-SlideGrade {
  param(
    [pscustomobject]$SlideSpec,
    [string]$ImagePath,
    [pscustomobject]$Rubric,
    [bool]$RenderQaPassed,
    [pscustomobject]$Config
  )

  $copyText = @($SlideSpec.eyebrow, $SlideSpec.headline, $SlideSpec.subtext) -join " "
  $dims = Get-ImageDimensions -Path $ImagePath
  $bannedTerms = @($Rubric.hard_fail_rules.copy.banned_terms)
  $matchedBannedTerms = @(Get-MatchedTerms -Text $copyText -Terms $bannedTerms)
  $bannedLanguageOk = ($matchedBannedTerms.Count -eq 0)

  $proofPaths = @($SlideSpec.hero_source) + @($SlideSpec.support_sources)
  $truthfulSourcesOk = $true
  foreach ($proofPath in $proofPaths) {
    $lowerPath = $proofPath.ToLower()
    if ($lowerPath.Contains("error") -or $lowerPath.Contains("broken") -or $lowerPath.Contains("excluded")) {
      $truthfulSourcesOk = $false
    }
  }

  $roleFit = Test-RoleFit -SlideSpec $SlideSpec

  $hardGates = [ordered]@{
    dimensions_ok = ($dims.width -eq $Rubric.hard_fail_rules.technical.required_width -and $dims.height -eq $Rubric.hard_fail_rules.technical.required_height)
    render_qa_passed = $RenderQaPassed
    banned_language_ok = $bannedLanguageOk
    truthful_sources_ok = $truthfulSourcesOk
    role_fit_ok = $roleFit.passed
  }

  $compliance = 5.0
  if (-not $bannedLanguageOk) { $compliance = 1.0 }
  if ($copyText.ToLower().Contains("chips") -and -not ($copyText.ToLower().Contains("play chips only") -or $copyText.ToLower().Contains("virtual chips"))) {
    $compliance -= 1
  }
  if ($copyText.ToLower().Contains("poker") -and -not (Test-ContainsAny -Text $copyText -Terms @("private", "training", "play-money", "friends"))) {
    $compliance -= 1
  }
  if (-not $truthfulSourcesOk) {
    $compliance = [math]::Min($compliance, 2)
  }

  $headlineWords = Get-WordCount -Text $SlideSpec.headline
  $subtextWords = Get-WordCount -Text $SlideSpec.subtext
  $messageClarity = 5.0
  if ($headlineWords -gt 7) { $messageClarity -= 0.5 }
  if ($headlineWords -gt 10) { $messageClarity -= 1.0 }
  if ($subtextWords -gt 14) { $messageClarity -= 0.5 }
  if ($subtextWords -gt 18) { $messageClarity -= 1.0 }
  if (-not $roleFit.passed) { $messageClarity -= 1.0 }

  $productLedProof = 5.0
  if (-not $roleFit.proof_match) { $productLedProof -= 1.5 }
  if ((@($SlideSpec.support_sources)).Count -gt 2) { $productLedProof -= 0.5 }
  if (-not $truthfulSourcesOk) { $productLedProof = [math]::Min($productLedProof, 2.5) }

  $visualRestraint = Get-StyleScore -StyleProfile $SlideSpec.style_profile
  if ((@($SlideSpec.support_sources)).Count -gt 1) {
    $visualRestraint -= 0.25
  }

  $technicalExport = 5.0
  if (-not $hardGates.dimensions_ok) { $technicalExport = 1.0 }
  elseif (-not $RenderQaPassed) { $technicalExport = 2.5 }

  $scores = [ordered]@{
    compliance = Clamp-Score -Score $compliance
    message_clarity = Clamp-Score -Score $messageClarity
    product_led_proof = Clamp-Score -Score $productLedProof
    visual_restraint = Clamp-Score -Score $visualRestraint
    technical_export = Clamp-Score -Score $technicalExport
  }

  $weighted = (
    ($scores.compliance * [double]$Rubric.slide_scoring.weights.compliance) +
    ($scores.message_clarity * [double]$Rubric.slide_scoring.weights.message_clarity) +
    ($scores.product_led_proof * [double]$Rubric.slide_scoring.weights.product_led_proof) +
    ($scores.visual_restraint * [double]$Rubric.slide_scoring.weights.visual_restraint) +
    ($scores.technical_export * [double]$Rubric.slide_scoring.weights.technical_export)
  )
  $weighted = [math]::Round($weighted, 2)

  $reasons = New-Object System.Collections.Generic.List[string]
  $notes = New-Object System.Collections.Generic.List[string]

  if (-not $hardGates.dimensions_ok) { $reasons.Add("dimension_mismatch") }
  if (-not $hardGates.render_qa_passed) { $reasons.Add("render_qa_failed") }
  if (-not $hardGates.banned_language_ok) { $reasons.Add("banned_language: " + ($matchedBannedTerms -join ", ")) }
  if (-not $hardGates.truthful_sources_ok) { $reasons.Add("truthful_source_check_failed") }
  if (-not $hardGates.role_fit_ok) { $reasons.Add("role_fit_failed") }
  if ($scores.message_clarity -lt 4) { $reasons.Add("message_clarity_below_threshold") }
  if ($scores.product_led_proof -lt 4) { $reasons.Add("product_led_proof_below_threshold") }

  if ($roleFit.keyword_matches.Count -gt 0) {
    $notes.Add("Role keyword matches: " + ($roleFit.keyword_matches -join ", "))
  }
  if ($roleFit.proof_match) {
    $notes.Add("Hero or support proof path aligns with the intended role.")
  }

  $anyHardFail = -not ($hardGates.dimensions_ok -and $hardGates.render_qa_passed -and $hardGates.banned_language_ok -and $hardGates.truthful_sources_ok)
  $minCategory = ($scores.Values | Measure-Object -Minimum).Minimum

  if ($anyHardFail -or $weighted -lt [double]$Rubric.slide_scoring.reject_rule.weighted_score_below -or -not $hardGates.role_fit_ok) {
    $status = "rejected"
  }
  elseif ($weighted -ge [double]$Config.minimum_slide_score -and $minCategory -ge 4) {
    $status = "approved"
  }
  else {
    $status = "revise"
  }

  return [pscustomobject]@{
    hard_gates = $hardGates
    scores = $scores
    weighted_score = $weighted
    status = $status
    reasons = @($reasons)
    grader_notes = @($notes)
    dimensions = $dims
  }
}

function Get-DeckGrade {
  param(
    [pscustomobject[]]$SlideGrades,
    [pscustomobject]$Spec,
    [pscustomobject]$Rubric,
    [pscustomobject]$Config
  )

  $requiredRoles = @($Rubric.deck_assembly.required_role_order)
  $actualRoles = @($Spec.slides | Sort-Object slide_number | ForEach-Object { $_.intended_role })
  $allApproved = ((@($SlideGrades | Where-Object { $_.status -ne "approved" })).Count -eq 0)
  $roleOrderOk = (($actualRoles -join "|") -eq ($requiredRoles -join "|"))

  $roleCoverage = if ($roleOrderOk) { 5.0 } else { 1.0 }
  $narrativeFlow = if ($roleOrderOk) { 5.0 } else { 2.0 }
  if (-not $allApproved) { $narrativeFlow -= 1.0 }

  $sourceGroups = @($Spec.slides | ForEach-Object { Split-Path $_.hero_source -Parent })
  $distinctSourceGroups = (@($sourceGroups | Sort-Object -Unique)).Count
  $visualVariety = if ($distinctSourceGroups -ge 4) { 5.0 } elseif ($distinctSourceGroups -ge 3) { 4.0 } else { 3.0 }

  $proofProgression = if ($roleOrderOk) { 5.0 } else { 2.5 }
  if (-not $allApproved) { $proofProgression -= 1.0 }

  $returnSlide = $Spec.slides | Where-Object { $_.intended_role -eq "return" } | Select-Object -First 1
  $returnCopy = @($returnSlide.headline, $returnSlide.subtext) -join " "
  $returnCredibility = 5.0
  if (Test-ContainsAny -Text $returnCopy -Terms @("win", "cash", "jackpot")) {
    $returnCredibility = 1.0
  }
  elseif (-not (Test-ContainsAny -Text $returnCopy -Terms @("return", "crew", "home", "invite"))) {
    $returnCredibility = 3.5
  }

  $scores = [ordered]@{
    role_coverage_and_order = Clamp-Score -Score $roleCoverage
    narrative_flow = Clamp-Score -Score $narrativeFlow
    visual_variety = Clamp-Score -Score $visualVariety
    proof_progression = Clamp-Score -Score $proofProgression
    return_and_cta_credibility = Clamp-Score -Score $returnCredibility
  }

  $weighted = (
    ($scores.role_coverage_and_order * [double]$Rubric.deck_scoring.weights.role_coverage_and_order) +
    ($scores.narrative_flow * [double]$Rubric.deck_scoring.weights.narrative_flow) +
    ($scores.visual_variety * [double]$Rubric.deck_scoring.weights.visual_variety) +
    ($scores.proof_progression * [double]$Rubric.deck_scoring.weights.proof_progression) +
    ($scores.return_and_cta_credibility * [double]$Rubric.deck_scoring.weights.return_and_cta_credibility)
  )
  $weighted = [math]::Round($weighted, 2)

  $reasons = New-Object System.Collections.Generic.List[string]
  if (-not $roleOrderOk) { $reasons.Add("required_role_order_failed") }
  if (-not $allApproved) { $reasons.Add("not_all_slides_approved") }

  $minCategory = ($scores.Values | Measure-Object -Minimum).Minimum
  if ($allApproved -and $roleOrderOk -and $weighted -ge [double]$Config.minimum_deck_score -and $minCategory -ge 4) {
    $status = "approved"
  }
  elseif ($weighted -lt 3.0 -or -not $roleOrderOk) {
    $status = "rejected"
  }
  else {
    $status = "revise"
  }

  return [pscustomobject]@{
    status = $status
    scores = $scores
    weighted_score = $weighted
    reasons = @($reasons)
  }
}

$obsidianRoot = Get-ObsidianRoot
$config = Get-Content $ConfigPath -Raw | ConvertFrom-Json
$spec = Get-Content $SpecPath -Raw | ConvertFrom-Json
$rubricPath = Resolve-FromRoot -Root $obsidianRoot -RelativePath $config.rubric_json_relative
$rubric = Get-Content $rubricPath -Raw | ConvertFrom-Json

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
if (-not $VersionSuffix) {
  $VersionSuffix = "autograde_$timestamp"
}

$runId = $timestamp
$projectRoot = Resolve-FromRoot -Root $obsidianRoot -RelativePath $config.project_root_relative
$renderScript = Resolve-FromRoot -Root $obsidianRoot -RelativePath $config.render_script_relative
$runDir = Join-Path $PSScriptRoot ("runs\\" + $runId)
$approvedSlidesDir = Join-Path $runDir "approved\\slides"
$rejectedSlidesDir = Join-Path $runDir "rejected\\slides"
$approvedDeckDir = Join-Path $runDir "approved\\decks"
$rejectedDeckDir = Join-Path $runDir "rejected\\decks"
$logsDir = Join-Path $runDir "logs"
$manifestsDir = Join-Path $runDir "manifests"
$gradesDir = Join-Path $runDir "grades"

foreach ($dir in @($runDir, $approvedSlidesDir, $rejectedSlidesDir, $approvedDeckDir, $rejectedDeckDir, $logsDir, $manifestsDir, $gradesDir)) {
  New-Directory -Path $dir
}

$renderQaPassed = $false
$renderLogPath = Join-Path $logsDir "render.log"
if (-not $SkipRender -and $spec.render.enabled) {
  try {
    if ($spec.render.run_qa -and $spec.render.generate_qa_shots) {
      & $renderScript -VersionSuffix $VersionSuffix -RunQa -GenerateQaShots *>&1 | Tee-Object -FilePath $renderLogPath | Out-Null
    }
    elseif ($spec.render.run_qa) {
      & $renderScript -VersionSuffix $VersionSuffix -RunQa *>&1 | Tee-Object -FilePath $renderLogPath | Out-Null
    }
    elseif ($spec.render.generate_qa_shots) {
      & $renderScript -VersionSuffix $VersionSuffix -GenerateQaShots *>&1 | Tee-Object -FilePath $renderLogPath | Out-Null
    }
    else {
      & $renderScript -VersionSuffix $VersionSuffix *>&1 | Tee-Object -FilePath $renderLogPath | Out-Null
    }
    $renderQaPassed = $true
  }
  catch {
    ($_ | Out-String) | Set-Content -Path $renderLogPath -Encoding UTF8
    throw
  }
}
else {
  $renderQaPassed = $true
}

$exportDir = Join-Path $projectRoot ("exports\\" + $VersionSuffix)
if (-not (Test-Path $exportDir)) {
  throw "Expected export directory was not created: $exportDir"
}

$slideResults = @()

foreach ($slideSpec in ($spec.slides | Sort-Object slide_number)) {
  $fileName = "felt_tiktok_slide_{0}_{1}.png" -f $slideSpec.slide_number, $VersionSuffix
  $imagePath = Join-Path $exportDir $fileName
  if (-not (Test-Path $imagePath)) {
    throw "Missing rendered slide: $imagePath"
  }

  $assetId = "{0}_slide_{1:00}" -f $VersionSuffix, $slideSpec.slide_number
  $manifest = [ordered]@{
    schema_version = "felt_tiktok/slide_manifest/v1"
    asset_id = $assetId
    campaign = $spec.campaign
    run_id = $runId
    spec_id = $spec.spec_id
    version_suffix = $VersionSuffix
    slide_number = $slideSpec.slide_number
    intended_role = $slideSpec.intended_role
    image_path = $imagePath
    template_family = $spec.template_family
    copy = [ordered]@{
      eyebrow = $slideSpec.eyebrow
      headline = $slideSpec.headline
      subtext = $slideSpec.subtext
    }
    proof_sources = [ordered]@{
      hero_source = $slideSpec.hero_source
      support_sources = @($slideSpec.support_sources)
    }
    required_context_files = @($config.required_context_files)
    future_agent_rules = @($config.future_agent_rules)
    created_at = (Get-Date).ToString("o")
  }

  $gradeResult = Get-SlideGrade -SlideSpec $slideSpec -ImagePath $imagePath -Rubric $rubric -RenderQaPassed $renderQaPassed -Config $config
  $grade = [ordered]@{
    schema_version = "felt_tiktok/slide_grade/v1"
    asset_id = $assetId
    run_id = $runId
    status = $gradeResult.status
    hard_gates = $gradeResult.hard_gates
    scores = $gradeResult.scores
    weighted_score = $gradeResult.weighted_score
    reasons = @($gradeResult.reasons)
    grader_notes = @($gradeResult.grader_notes)
    graded_at = (Get-Date).ToString("o")
  }

  $manifestPath = Join-Path $manifestsDir ($assetId + ".manifest.json")
  $gradePath = Join-Path $gradesDir ($assetId + ".grade.json")
  Write-JsonFile -Path $manifestPath -Data $manifest
  Write-JsonFile -Path $gradePath -Data $grade

  $targetDir = if ($grade.status -eq "approved") { $approvedSlidesDir } else { $rejectedSlidesDir }
  Copy-Item -Path $imagePath -Destination (Join-Path $targetDir ([System.IO.Path]::GetFileName($imagePath))) -Force
  Copy-Item -Path $manifestPath -Destination (Join-Path $targetDir ([System.IO.Path]::GetFileName($manifestPath))) -Force
  Copy-Item -Path $gradePath -Destination (Join-Path $targetDir ([System.IO.Path]::GetFileName($gradePath))) -Force

  $slideResults += [pscustomobject]@{
    asset_id = $assetId
    slide_number = $slideSpec.slide_number
    intended_role = $slideSpec.intended_role
    status = $grade.status
    weighted_score = $grade.weighted_score
    image_path = $imagePath
  }
}

$deckId = "{0}_deck" -f $VersionSuffix
$deckManifest = [ordered]@{
  schema_version = "felt_tiktok/deck_manifest/v1"
  deck_id = $deckId
  campaign = $spec.campaign
  run_id = $runId
  spec_id = $spec.spec_id
  slide_asset_ids = @($slideResults | Sort-Object slide_number | ForEach-Object { $_.asset_id })
  role_order = @($spec.slides | Sort-Object slide_number | ForEach-Object { $_.intended_role })
  version_suffix = $VersionSuffix
  required_context_files = @($config.required_context_files)
  created_at = (Get-Date).ToString("o")
}

$deckGradeResult = Get-DeckGrade -SlideGrades ($slideResults | ForEach-Object {
  $gradeFile = Join-Path $gradesDir ($_.asset_id + ".grade.json")
  Get-Content $gradeFile -Raw | ConvertFrom-Json
}) -Spec $spec -Rubric $rubric -Config $config

$deckGrade = [ordered]@{
  schema_version = "felt_tiktok/deck_grade/v1"
  deck_id = $deckId
  run_id = $runId
  status = $deckGradeResult.status
  scores = $deckGradeResult.scores
  weighted_score = $deckGradeResult.weighted_score
  reasons = @($deckGradeResult.reasons)
  graded_at = (Get-Date).ToString("o")
}

$deckManifestPath = Join-Path $manifestsDir ($deckId + ".manifest.json")
$deckGradePath = Join-Path $gradesDir ($deckId + ".grade.json")
Write-JsonFile -Path $deckManifestPath -Data $deckManifest
Write-JsonFile -Path $deckGradePath -Data $deckGrade

$deckTargetRoot = if ($deckGrade.status -eq "approved") { $approvedDeckDir } else { $rejectedDeckDir }
$deckTargetDir = Join-Path $deckTargetRoot $deckId
New-Directory -Path $deckTargetDir
Copy-Item -Path $deckManifestPath -Destination (Join-Path $deckTargetDir ([System.IO.Path]::GetFileName($deckManifestPath))) -Force
Copy-Item -Path $deckGradePath -Destination (Join-Path $deckTargetDir ([System.IO.Path]::GetFileName($deckGradePath))) -Force

$approvedSlideImages = @($slideResults | Sort-Object slide_number | ForEach-Object { $_.image_path })
foreach ($slidePath in $approvedSlideImages) {
  Copy-Item -Path $slidePath -Destination (Join-Path $deckTargetDir ([System.IO.Path]::GetFileName($slidePath))) -Force
}

$emailPayloadPath = $null
if ($PrepareEmail -and $deckGrade.status -eq "approved") {
  $contextLines = ($config.required_context_files | ForEach-Object { "- $_" }) -join "`n"
  $bodyLines = @(
    "Approved Felt TikTok deck: $deckId",
    "",
    "- Campaign: $($spec.campaign)",
    "- Run ID: $runId",
    "- Deck score: $($deckGrade.weighted_score)",
    "- Slide statuses: approved deck attached for review",
    "",
    "Strategy context used:",
    $contextLines
  )
  $emailPayload = [ordered]@{
    schema_version = "felt_tiktok/email_payload/v1"
    deck_id = $deckId
    to = if ($spec.recipient_email) { $spec.recipient_email } else { $config.default_recipient_email }
    subject = "Felt TikTok deck approved - $VersionSuffix"
    body_markdown = ($bodyLines -join "`n")
    attachment_files = @($approvedSlideImages)
    emailed_at = $null
  }

  $emailPayloadPath = Join-Path $deckTargetDir ($deckId + ".email_payload.json")
  Write-JsonFile -Path $emailPayloadPath -Data $emailPayload
}

$runSummary = [ordered]@{
  schema_version = "felt_tiktok/pipeline_run/v1"
  run_id = $runId
  campaign = $spec.campaign
  spec_id = $spec.spec_id
  version_suffix = $VersionSuffix
  render_qa_passed = $renderQaPassed
  slide_results = @($slideResults)
  deck_result = $deckGrade
  email_payload_path = $emailPayloadPath
}

$runSummaryPath = Join-Path $runDir "run_summary.json"
Write-JsonFile -Path $runSummaryPath -Data $runSummary

Write-Host "Pipeline run complete."
Write-Host ("Run ID: {0}" -f $runId)
Write-Host ("Version suffix: {0}" -f $VersionSuffix)
Write-Host ("Approved slides: {0}" -f ((@($slideResults | Where-Object { $_.status -eq "approved" })).Count))
Write-Host ("Rejected or revise slides: {0}" -f ((@($slideResults | Where-Object { $_.status -ne "approved" })).Count))
Write-Host ("Deck status: {0} ({1})" -f $deckGrade.status, $deckGrade.weighted_score)
if ($emailPayloadPath) {
  Write-Host ("Email payload: {0}" -f $emailPayloadPath)
}
