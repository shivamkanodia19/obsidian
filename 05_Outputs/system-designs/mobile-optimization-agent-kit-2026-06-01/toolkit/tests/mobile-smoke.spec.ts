import { expect, test } from '@playwright/test';

test.describe('mobile smoke audit', () => {
  test('homepage has no horizontal overflow', async ({ page }) => {
    await page.goto('/');
    await page.waitForLoadState('networkidle');

    const hasOverflow = await page.evaluate(() => {
      const root = document.documentElement;
      return root.scrollWidth > root.clientWidth;
    });

    expect(hasOverflow).toBeFalsy();
  });

  test('homepage exposes a viewport meta tag', async ({ page }) => {
    await page.goto('/');

    const viewportContent = await page
      .locator('meta[name="viewport"]')
      .getAttribute('content');

    expect(viewportContent).toContain('width=device-width');
  });

  test('homepage renders primary actions visibly', async ({ page }) => {
    await page.goto('/');
    await page.waitForLoadState('networkidle');

    const primaryAction = page.locator('a, button').filter({
      hasText: /get started|sign up|book|contact|learn more|start/i,
    }).first();

    await expect(primaryAction).toBeVisible();
  });

  test('homepage screenshot for manual review', async ({ page }, testInfo) => {
    await page.goto('/');
    await page.waitForLoadState('networkidle');

    await page.screenshot({
      path: testInfo.outputPath('homepage-mobile-full.png'),
      fullPage: true,
    });
  });
});
