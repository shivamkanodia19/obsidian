# felt.bet TikTok Carousel Handoff

## Exports

- `felt_tiktok_slide_1.png`
- `felt_tiktok_slide_2.png`
- `felt_tiktok_slide_3.png`
- `felt_tiktok_slide_4.png`
- `felt_tiktok_slide_5.png`

All exports are `1080 x 1920` PNGs.

## Screenshot inventory

- Slide 1:
  - `felt_lobby_host_panel.png`
  - `felt_lobby_mobile_390x844.png`
  - `felt_guided_table_mobile_390x844.png`
- Slide 2:
  - `felt_lobby_mobile_390x844.png`
- Slide 3:
  - `felt_lobby_host_panel.png`
  - `felt_guided_table_mobile_390x844.png`
- Slide 4:
  - `felt_guided_table_mobile_feedback_390x844.png`
  - `felt_training_mobile_430x932.png`
- Slide 5:
  - `felt_home_mobile_390x844.png`
  - `felt_guided_table_mobile_390x844.png`

## Inaccessible or limited states

- Creating a live hosted table returned a signed-out / function error state instead of a completed table creation flow.
- No Supabase MCP was exposed in this session, so I did not seed any demo data.
- Figma web capture worked for source-page imports, but direct Figma page-building writes did not persist reliably in this environment. Final slide composition and export were therefore completed locally from live screenshots.

## Figma reference

- Source capture file:
  - `https://www.figma.com/design/OZheUfTR35cBGT8vuHzLkO`
- Captured source nodes added there:
  - `1:2` homepage mobile capture
  - `2:2` lobby mobile capture
  - `3:2` training mobile capture
  - `4:2` guided feedback mobile capture
  - `5:2` guided table mobile capture
  - `6:2` host panel desktop capture

## Local composition file

- `felt_tiktok_carousel.html`

