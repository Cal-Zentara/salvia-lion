const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto('https://salvialion.com/', { waitUntil: 'networkidle', timeout: 30000 });
  await page.waitForTimeout(2000);
  await page.evaluate(() => document.querySelector('#services').scrollIntoView());
  await page.waitForTimeout(800);
  await page.screenshot({ path: 'C:/Users/Aesth/Desktop/mob-services-new.png' });
  await browser.close();
  console.log('Done');
})();
