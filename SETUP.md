# Setup

## 1. Create the GitHub profile repository

Create a **public repository named exactly `saranraj1`** under the `saranraj1` account. GitHub recognizes this as the special profile repository.

Copy the contents of this package into that repository and push `main`.

## 2. Check the profile

Open `https://github.com/saranraj1`. GitHub should render `README.md` as the profile page.

## 3. Enable the activity updater

The included GitHub Action runs daily and can also be started manually from **Actions → Update GitHub Activity → Run workflow**.

The workflow first tries `PROFILE_TOKEN` and falls back to the repository-provided `GITHUB_TOKEN`.

### Recommended token setup

If the Action's GraphQL request is rejected with an authentication/permission error, create a GitHub token that can read your user contribution data and save it as a repository secret named:

`PROFILE_TOKEN`

Do **not** hard-code the token in `generator/generate.mjs` or the workflow.

## 4. Change the account name

If you reuse this template for another account, update `GITHUB_LOGIN` in `.github/workflows/update-activity.yml`.

## 5. Local preview

The SVGs can be opened directly in a browser.

To regenerate activity locally:

```bash
npm install
GITHUB_TOKEN=YOUR_TOKEN GITHUB_LOGIN=saranraj1 npm run generate
```

On Windows PowerShell:

```powershell
$env:GITHUB_TOKEN="YOUR_TOKEN"
$env:GITHUB_LOGIN="saranraj1"
npm run generate
```

## Notes

- The hero graphics are intentionally static so the profile identity does not depend on an external service.
- The activity graphics are generated locally by the Action and committed back into the profile repository.
- The activity SVG includes a subtle recent-activity pulse; there is no JavaScript in the SVG.
- The README uses direct repository links for the flagship projects so visitors can inspect the actual implementations.
