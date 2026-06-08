param()

$ErrorActionPreference = "Stop"

Add-Type -AssemblyName System.Drawing

$baseDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$projectDir = Split-Path -Parent $baseDir
$captureDir = Join-Path $projectDir "captures"
$outputDir = Join-Path $captureDir "derived"

New-Item -ItemType Directory -Force -Path $outputDir | Out-Null

function New-CroppedImage {
  param(
    [string]$SourcePath,
    [string]$TargetPath,
    [int]$X,
    [int]$Y,
    [int]$Width,
    [int]$Height
  )

  $resolvedSource = Resolve-Path $SourcePath
  $bitmap = [System.Drawing.Bitmap]::FromFile($resolvedSource)

  try {
    if ($X -lt 0 -or $Y -lt 0 -or $Width -le 0 -or $Height -le 0) {
      throw "Invalid crop rectangle for $SourcePath"
    }

    if (($X + $Width) -gt $bitmap.Width -or ($Y + $Height) -gt $bitmap.Height) {
      throw "Crop rectangle exceeds source bounds for $SourcePath"
    }

    $target = New-Object System.Drawing.Bitmap($Width, $Height)
    try {
      $graphics = [System.Drawing.Graphics]::FromImage($target)
      try {
        $graphics.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
        $graphics.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::HighQuality
        $graphics.SmoothingMode = [System.Drawing.Drawing2D.SmoothingMode]::HighQuality
        $graphics.CompositingQuality = [System.Drawing.Drawing2D.CompositingQuality]::HighQuality
        $graphics.DrawImage(
          $bitmap,
          (New-Object System.Drawing.Rectangle(0, 0, $Width, $Height)),
          (New-Object System.Drawing.Rectangle($X, $Y, $Width, $Height)),
          [System.Drawing.GraphicsUnit]::Pixel
        )
      }
      finally {
        $graphics.Dispose()
      }

      $target.Save($TargetPath, [System.Drawing.Imaging.ImageFormat]::Png)
      Write-Host "Wrote $TargetPath"
    }
    finally {
      $target.Dispose()
    }
  }
  finally {
    $bitmap.Dispose()
  }
}

$jobs = @(
  @{
    Source = Join-Path $captureDir "map\clinicalhours_map_desktop_1440x1200_live.png"
    Target = Join-Path $outputDir "clinicalhours_map_tall_controls_focus_v1.png"
    X = 0; Y = 0; Width = 460; Height = 1200
  },
  @{
    Source = Join-Path $captureDir "home\clinicalhours_home_mobile_430x932_live.png"
    Target = Join-Path $outputDir "clinicalhours_home_mobile_start_focus_v1.png"
    X = 71; Y = 150; Width = 289; Height = 782
  },
  @{
    Source = Join-Path $captureDir "home\clinicalhours_home_hero_section_live.png"
    Target = Join-Path $outputDir "clinicalhours_home_mobile_button_focus_v1.png"
    X = 18; Y = 180; Width = 330; Height = 60
  },
  @{
    Source = Join-Path $captureDir "map\clinicalhours_map_full_live.png"
    Target = Join-Path $outputDir "clinicalhours_map_focus_v1.png"
    X = 0; Y = 10; Width = 1240; Height = 1190
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_dashboard_overview_auth_live_v3.png"
    Target = Join-Path $outputDir "clinicalhours_dashboard_tall_focus_v2.png"
    X = 215; Y = 0; Width = 950; Height = 1240
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_dashboard_overview_auth_live_v3.png"
    Target = Join-Path $outputDir "clinicalhours_dashboard_preview_landscape_v1.png"
    X = 160; Y = 60; Width = 1080; Height = 920
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_dashboard_overview_auth_live_v3.png"
    Target = Join-Path $outputDir "clinicalhours_dashboard_workflow_band_v1.png"
    X = 0; Y = 305; Width = 1375; Height = 490
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_dashboard_overview_auth_live_v3.png"
    Target = Join-Path $outputDir "clinicalhours_dashboard_workflow_band_v2.png"
    X = 0; Y = 305; Width = 1375; Height = 437
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_journal_activity_auth_live_v2.png"
    Target = Join-Path $outputDir "clinicalhours_journal_toolbar_focus_v1.png"
    X = 0; Y = 0; Width = 1368; Height = 220
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_journal_activity_auth_live_v2.png"
    Target = Join-Path $outputDir "clinicalhours_journal_toolbar_tile_v1.png"
    X = 0; Y = 0; Width = 1116; Height = 400
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_journal_activity_auth_live_v2.png"
    Target = Join-Path $outputDir "clinicalhours_journal_toolbar_tile_v2.png"
    X = 0; Y = 0; Width = 1116; Height = 260
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_journal_activity_auth_live_v2.png"
    Target = Join-Path $outputDir "clinicalhours_journal_cta_focus_v2.png"
    X = 360; Y = 108; Width = 620; Height = 280
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_journal_activity_auth_live_v2.png"
    Target = Join-Path $outputDir "clinicalhours_journal_cta_tile_v1.png"
    X = 375; Y = 95; Width = 620; Height = 323
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_journal_top_auth_live_v2.png"
    Target = Join-Path $outputDir "clinicalhours_journal_header_band_v1.png"
    X = 0; Y = 0; Width = 1368; Height = 60
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_dashboard_overview_auth_live_v3.png"
    Target = Join-Path $outputDir "clinicalhours_dashboard_reflections_focus_v1.png"
    X = 0; Y = 1088; Width = 1375; Height = 157
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_dashboard_overview_auth_live_v3.png"
    Target = Join-Path $outputDir "clinicalhours_dashboard_records_band_v1.png"
    X = 351; Y = 130; Width = 675; Height = 225
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_dashboard_overview_auth_live_v3.png"
    Target = Join-Path $outputDir "clinicalhours_dashboard_experiences_card_v1.png"
    X = 700; Y = 130; Width = 323; Height = 225
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_journal_activity_auth_live_v2.png"
    Target = Join-Path $outputDir "clinicalhours_journal_controls_band_v1.png"
    X = 0; Y = 92; Width = 1368; Height = 160
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_journal_activity_auth_live_v2.png"
    Target = Join-Path $outputDir "clinicalhours_journal_prompt_focus_v1.png"
    X = 440; Y = 188; Width = 490; Height = 190
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_auth_signin_card_auth_live_v3.png"
    Target = Join-Path $outputDir "clinicalhours_auth_actions_focus_v1.png"
    X = 101; Y = 140; Width = 515; Height = 870
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_auth_signin_card_auth_live_v3.png"
    Target = Join-Path $outputDir "clinicalhours_auth_actions_focus_v2.png"
    X = 120; Y = 190; Width = 470; Height = 790
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_auth_signin_card_auth_live_v3.png"
    Target = Join-Path $outputDir "clinicalhours_auth_guest_actions_v1.png"
    X = 52; Y = 170; Width = 612; Height = 360
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_auth_signin_card_auth_live_v3.png"
    Target = Join-Path $outputDir "clinicalhours_auth_guest_browse_focus_v2.png"
    X = 96; Y = 278; Width = 520; Height = 220
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_auth_full_live_v2.png"
    Target = Join-Path $outputDir "clinicalhours_auth_signin_tall_focus_v1.png"
    X = 420; Y = 220; Width = 600; Height = 1180
  },
  @{
    Source = Join-Path $captureDir "auth\clinicalhours_dashboard_hero_auth_live_v2.png"
    Target = Join-Path $outputDir "clinicalhours_dashboard_welcome_panel_v1.png"
    X = 0; Y = 0; Width = 620; Height = 444
  },
  @{
    Source = Join-Path $captureDir "official\clinicalhours_opportunities_official_2026-05-31.png"
    Target = Join-Path $outputDir "clinicalhours_opportunity_header_focus_v1.png"
    X = 360; Y = 190; Width = 1800; Height = 600
  },
  @{
    Source = Join-Path $captureDir "official\clinicalhours_opportunities_official_2026-05-31.png"
    Target = Join-Path $outputDir "clinicalhours_opportunity_search_focus_v1.png"
    X = 460; Y = 420; Width = 2640; Height = 360
  },
  @{
    Source = Join-Path $captureDir "official\clinicalhours_opportunities_official_2026-05-31.png"
    Target = Join-Path $outputDir "clinicalhours_opportunity_row_focus_v1.png"
    X = 460; Y = 620; Width = 2640; Height = 470
  },
  @{
    Source = Join-Path $captureDir "official\clinicalhours_opportunities_official_2026-05-31.png"
    Target = Join-Path $outputDir "clinicalhours_opportunity_row_focus_v2.png"
    X = 460; Y = 1510; Width = 2640; Height = 430
  },
  @{
    Source = Join-Path $captureDir "official\clinicalhours_opportunities_official_2026-05-31.png"
    Target = Join-Path $outputDir "clinicalhours_opportunity_listing_focus_v1.png"
    X = 430; Y = 1675; Width = 1260; Height = 300
  },
  @{
    Source = Join-Path $captureDir "official\clinicalhours_opportunities_official_2026-05-31.png"
    Target = Join-Path $outputDir "clinicalhours_opportunity_actions_focus_v1.png"
    X = 2520; Y = 1648; Width = 820; Height = 340
  },
  @{
    Source = Join-Path $captureDir "official\clinicalhours_opportunities_houston_methodist_live_2026-05-30.png"
    Target = Join-Path $outputDir "clinicalhours_opportunity_houston_result_focus_v1.png"
    X = 110; Y = 85; Width = 1050; Height = 300
  },
  @{
    Source = Join-Path $captureDir "official\clinicalhours_houston_methodist_save_dashboard_live_2026-05-30.png"
    Target = Join-Path $outputDir "clinicalhours_houston_save_panel_focus_v1.png"
    X = 470; Y = 555; Width = 500; Height = 380
  },
  @{
    Source = Join-Path $captureDir "official\clinicalhours_opportunities_official_2026-05-31.png"
    Target = Join-Path $outputDir "clinicalhours_opportunity_row_focus_v3.png"
    X = 450; Y = 1450; Width = 2800; Height = 620
  }
)

foreach ($job in $jobs) {
  New-CroppedImage -SourcePath $job.Source -TargetPath $job.Target -X $job.X -Y $job.Y -Width $job.Width -Height $job.Height
}

Write-Host "Crop derivative build complete."
