pretty standard setup that you get from `npm i playwright`

```json
{
  "scripts": {
    "playwright": "DEBUG=pw:webserver npx playwright test flow/open-account-regular ",
  }
}
```
added the DEBUG env var to see logging of the wds server startup while running playwright

the WDS setup is in [web-dev-server.md]

```typescript
import { defineConfig, devices } from '@playwright/test';

/**
 * Read environment variables from file.
 * https://github.com/motdotla/dotenv
 */
// require('dotenv').config();

/**
 * See https://playwright.dev/docs/test-configuration.
 */
export default defineConfig({
  testDir: './playwright-tests',
  /* Run tests in files in parallel */
  fullyParallel: false,
  /* Fail the build on CI if you accidentally left test.only in the source code. */
  forbidOnly: !!process.env.CI,
  /* Retry on CI only */
  retries: process.env.CI ? 2 : 0,
  /* Opt out of parallel tests on CI. */
  workers: process.env.CI ? 1 : undefined,
  /* Reporter to use. See https://playwright.dev/docs/test-reporters */
  reporter: 'html',
  use: {
    // baseURL: '',

    /* Collect trace when retrying the failed test. See https://playwright.dev/docs/trace-viewer */
    trace: 'on-first-retry',
  },

  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
  ],

  webServer: {
    command: 'wds -c web-demo-server.config.mjs',
    url: 'http://127.0.0.1:8000/demo',
    reuseExistingServer: false,
  },
});
```
