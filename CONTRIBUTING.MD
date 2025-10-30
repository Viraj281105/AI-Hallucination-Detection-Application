# How to Contribute

This is a solo-developer portfolio project, but it follows a professional Git workflow for all new features and fixes.

## 1. Setting Up
1.  Fork and clone the repository.
2.  Follow the setup steps in `README.md` to create your `venv` and install dependencies.
3.  Run `python ingest.py` to build your local database.
4.  Run `pytest` to ensure all tests pass.

## 2. Branching & Commits
This project follows a simple `develop` -> `feature` branch workflow.

* **`main`**: This branch is for stable, deployed code. Do not commit here directly.
* **`develop`**: This is the main integration branch for new features. All Pull Requests should target `develop`.
* **`feature/...` or `fix/...`**: All work must be done on a feature or fix branch.

**Workflow:**
1.  Pull the latest from `develop`:
    ```bash
    git checkout develop
    git pull
    ```
2.  Create your new feature branch (referencing a GitHub Issue # if possible):
    ```bash
    git checkout -b feature/1-my-new-feature
    ```
3.  Write your code and **make sure `pytest` passes** before pushing.

## 3. Commit Message Convention
Please use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) for your commit messages. This helps keep the project history clean.

* `feat:` A new feature (e.g., `feat: Add Mistral judge logic`)
* `fix:` A bug fix (e.g., `fix: Correct NLI probability indexing`)
* `docs:` Documentation changes (e.g., `docs: Update README with setup guide`)
* `refactor:` Code changes that neither fix a bug nor add a feature
* `test:` Adding or fixing tests
* `ci:` Changes to GitHub Actions or Docker files

**Example Commit:**
```bash
git commit -m "feat(api): Add /history endpoint
>
> Implements the /history GET endpoint to retrieve all
> verified claims from the sqlite database."

## 4. Submitting a Pull Request

1.  Push your feature branch to your fork.
2.  Open a Pull Request (PR) from your branch to the main repo's `develop` branch.
3.  Ensure the GitHub Actions (CI) tests pass.
4.  Link the PR to the GitHub Issue it resolves (e.g., "Closes \#1").

<!-- end list -->
