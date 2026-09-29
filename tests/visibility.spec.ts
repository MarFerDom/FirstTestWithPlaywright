import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  // Recording...
  await page.goto('https://playwright.dev/');
  // Python option should not be visible
  await expect(page.getByRole('navigation', { name: 'Main' }).getByRole('link', { name: 'Python' })).not.toBeVisible();
  // Hover over Node.js and list should appear
  await page.getByRole('button', { name: 'Node.js' }).hover();
  // And now be visible
  await expect(page.getByRole('navigation', { name: 'Main' }).getByRole('link', { name: 'Python' })).toBeVisible();
  
  await page.getByRole('navigation', { name: 'Main' }).getByRole('link', { name: 'Python' }).click();
});