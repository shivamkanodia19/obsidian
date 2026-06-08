param(
  [Parameter(Mandatory = $true)]
  [string]$HtmlFile,
  [string]$Profile = "generic"
)

$ErrorActionPreference = "Stop"

$baseDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$htmlPath = if ([System.IO.Path]::IsPathRooted($HtmlFile)) {
  $HtmlFile
} else {
  Join-Path $baseDir $HtmlFile
}

if (-not (Test-Path $htmlPath)) {
  throw "HTML file not found: $htmlPath"
}

$lines = Get-Content $htmlPath
$issues = New-Object System.Collections.Generic.List[string]

$bannedPhraseRules = @(
  @{ Pattern = 'best student proof'; Reason = 'internal strategy language leaked into audience-facing copy' },
  @{ Pattern = 'prove this is'; Reason = 'defensive explanation instead of user-facing value' },
  @{ Pattern = 'visual payoff'; Reason = 'creative-brief language should not appear in the deck' },
  @{ Pattern = 'preview-style proof'; Reason = 'evaluation language should not appear in the deck' },
  @{ Pattern = 'without forcing a login'; Reason = 'internal conversion framing should be rewritten for the audience' },
  @{ Pattern = 'cold traffic'; Reason = 'media-buying jargon should not appear in audience-facing copy' },
  @{ Pattern = 'calm close'; Reason = 'internal CTA label should not appear in the creative' },
  @{ Pattern = 'why this works'; Reason = 'internal rationale should not appear in the deck' },
  @{ Pattern = 'why it lands'; Reason = 'strategy-note phrasing should not appear in the deck' },
  @{ Pattern = 'why it exists'; Reason = 'strategy-note phrasing should not appear in the deck' },
  @{ Pattern = 'after the preview'; Reason = 'internal sequencing label should not appear in the deck' },
  @{ Pattern = 'after the first shift'; Reason = 'internal sequencing label should not appear in the deck' },
  @{ Pattern = 'better story'; Reason = 'editorial note should not appear in the deck' },
  @{ Pattern = 'instant visual payoff'; Reason = 'creative-brief language should not appear in the deck' },
  @{ Pattern = 'in-feed'; Reason = 'channel-planning jargon should not appear in the deck' }
)

$clinicOpsPhraseRules = @(
  @{ Pattern = 'operating layer'; Reason = 'broad platform language outruns the narrower clinic-ops proof this lane can currently defend' },
  @{ Pattern = 'supply in one lane'; Reason = 'supply-wide platform copy outruns the current validated workflow wedge' },
  @{ Pattern = 'credentialing, and supply'; Reason = 'paired supply claims are broader than the current clinic-ops default should promise' }
)

$bannedAssetRules = @(
  @{
    Pattern = 'clinicalhours_home_mobile_430x932_live\.png'
    Reason = 'raw home mobile hero includes a generic slogan; use a derived crop or alternate proof asset'
  },
  @{
    Pattern = 'clinicalhours_auth_signin_card_auth_live_v3\.png'
    Reason = 'raw auth card includes weak onboarding filler; use a tighter derived crop'
  },
  @{
    Pattern = 'clinicalhours_dashboard_overview_auth_live_v3\.png'
    Reason = 'raw dashboard overview includes empty-state filler; use a stronger crop or alternate proof asset'
  },
  @{
    Pattern = 'clinicalhours_journal_section_auth_live_v3\.png'
    Reason = 'raw journal section includes low-signal empty-state text; use toolbar or CTA crops instead'
  }
)

$useBrightStudentAssetRules = $Profile -eq "bright_student" -or $htmlPath -match "clinicalhours_tiktok_student_"
$useClinicOpsPhraseRules = $Profile -eq "clinic_ops_primary" -or $htmlPath -match "clinicalhours_tiktok_(carousel|clinic_onboarding_visibility|clinic_expiring_clearances)\.html$"

for ($index = 0; $index -lt $lines.Count; $index += 1) {
  $line = $lines[$index]
  $lineNumber = $index + 1

  foreach ($rule in $bannedPhraseRules) {
    if ($line -match $rule.Pattern) {
      $issues.Add(("Line {0}: banned phrase '{1}' - {2}" -f $lineNumber, $Matches[0], $rule.Reason))
    }
  }

  if ($useClinicOpsPhraseRules) {
    foreach ($rule in $clinicOpsPhraseRules) {
      if ($line -match $rule.Pattern) {
        $issues.Add(("Line {0}: clinic-ops overclaim phrase '{1}' - {2}" -f $lineNumber, $Matches[0], $rule.Reason))
      }
    }
  }

  if ($useBrightStudentAssetRules) {
    foreach ($rule in $bannedAssetRules) {
      if ($line -match $rule.Pattern) {
        $issues.Add(("Line {0}: banned raw asset '{1}' - {2}" -f $lineNumber, $Matches[0], $rule.Reason))
      }
    }
  }
}

$opportunityCountMatches = [regex]::Matches(($lines -join "`n"), '(?<count>\d{1,3}(?:,\d{3})\+?)\s*(?:visible opportunities|openings)')
if ($opportunityCountMatches.Count -gt 1) {
  $normalizedCounts = @(
    $opportunityCountMatches |
      ForEach-Object { $_.Groups["count"].Value -replace '\+', '' } |
      Select-Object -Unique
  )

  if ($normalizedCounts.Count -gt 1) {
    $issues.Add(("Conflicting opportunity counts detected: {0}" -f ($normalizedCounts -join ", ")))
  }
}

if ($issues.Count -gt 0) {
  Write-Host "COPY AUDIT WARN"
  foreach ($issue in $issues) {
    Write-Host "- $issue"
  }
  exit 1
}

Write-Host "COPY AUDIT PASS"
