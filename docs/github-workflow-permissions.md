# GitHub Workflow Permissions Configuration

## Problem
The `github:api` action is not available in Backstage's `@backstage/plugin-scaffolder-backend-module-github` package version 0.9.2, which caused template creation errors when trying to configure workflow permissions programmatically.

## Solution
There are two recommended approaches to handle GitHub Actions workflow permissions:

### Option 1: Organization-Level Configuration (Recommended)
Configure default workflow permissions at the GitHub organization level:

1. Go to GitHub Organization Settings → Actions → General
2. Under "Workflow permissions", select:
   - **Read and write permissions** (to allow workflows to push to GHCR, create tags, etc.)
   - Optionally enable "Allow GitHub Actions to create and approve pull requests"

This applies to all repositories in the organization and eliminates the need to configure it per-repository.

### Option 2: Workflow-Level Configuration
Define permissions explicitly in each workflow file. Add this to your workflow YAML:

```yaml
permissions:
  contents: write          # For pushing changes, creating tags
  packages: write          # For pushing to GitHub Container Registry (GHCR)
  pull-requests: write     # For creating/updating PRs
  issues: write            # For creating/updating issues
  id-token: write          # For OIDC authentication (if using)
```

**Example** (in `.github/workflows/ci-cd.yml`):

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main]

permissions:
  contents: write
  packages: write

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      # Your workflow steps here
```

### Option 3: Template Skeleton Configuration
Include the necessary permissions in your template skeleton's workflow files. This ensures that any repository created from the template has the correct permissions configured from the start.

Add to `skeleton/.github/workflows/ci-cd.yml`:

```yaml
permissions:
  contents: write
  packages: write
```

## Why This Happened
The `github:api` action was being used to make a direct API call to GitHub to configure workflow permissions:

```yaml
- id: configure-permissions
  name: Configure Workflow Permissions
  action: github:api  # ❌ Not available in current version
  input:
    url: '/repos/.../actions/permissions/workflow'
    method: PUT
```

This action is not registered in the current version of the GitHub scaffolder module.

## Future Considerations
If you need the `github:api` action for other use cases:

1. **Upgrade the package**: Check if newer versions of `@backstage/plugin-scaffolder-backend-module-github` include this action
2. **Create a custom action**: Implement a custom scaffolder action that uses the GitHub API directly
3. **Use a different approach**: Leverage existing actions like `publish:github` with additional configurations

## References
- [Backstage Built-in Actions](https://backstage.io/docs/features/software-templates/builtin-actions/)
- [GitHub Actions Permissions](https://docs.github.com/en/actions/using-jobs/assigning-permissions-to-jobs)
- [GitHub Organization Settings](https://docs.github.com/en/organizations/managing-organization-settings/disabling-or-limiting-github-actions-for-your-organization)
