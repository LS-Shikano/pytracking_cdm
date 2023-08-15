# Contribution

### Git Branch Policies and CI
Merging with main requires a pull request that has to pass a check defined in the ci.yml github workflow. The check ensures the code is formatted, linted, docstrings exist and are styles correctly and run tests. You can't push directly to main. Create a branch, then open a PR for merging with main. Tip: [You can create branches directly from issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-a-branch-for-an-issue).  

## Dev Setup

This package is developed with poetry. Find installation instructions [here](https://python-poetry.org/docs/)
1. Clone Repo
2. Install dependencies: 
```bash
poetry install
```
3. Set up pre-commit hooks:
```bash
poetry run pre-commit install --hook-type commit-msg
```
This will ensure the code is formatted, linted, docstrings exist and are styled correctly and run tests. 

### IDE requirements
Install [Black](https://github.com/psf/black) for formatting tooltips and [Ruff](https://github.com/charliermarsh/ruff) for linting tooltips in your IDE.

## Dev Workflow
We are using the GitHub Flow specified [here](https://docs.github.com/en/get-started/quickstart/github-flow).

### Commit messages
- Basic [git commit message guidelines](https://ec.europa.eu/component-library/v1.15.0/eu/docs/conventions/git/) apply
- Additionally, follow the [Conventional Commits specification](https://www.conventionalcommits.org/en/v1.0.0/)
- A fix commit is a PATCH. Example: 0.0.21 -> 0.0.22
- A feat commit is a MINOR. Example: 0.1.0 -> 0.2.0
- A commit with BREAKING CHANGE or ! is a MAJOR. 1.0.0 -> 2.0.0

### Versioning
- We are following this specification for versioning: [SemVer](https://semver.org/)

### Code documentation
This project uses [pydocstyle](https://github.com/PyCQA/pydocstyle) to enforce the existance and style of docstrings. [Googles style guidelines](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) are used. To check whether your docstrings are consistent with these guidelines, run:
```bash
poetry run pydocstyle ./pytracking_cdm
```
### Testing 
To test ensure the package functions as intended after making changes, run:
```bash
poetry run pytest -svv     
```
Tests are defined in `./tests/test_pytracking_cdm.py`


#### Sources
- https://johschmidt42.medium.com/setting-up-python-projects-part-v-206df3c1e3d3
- https://mestrak.com/blog/semantic-release-with-python-poetry-github-actions-20nn
- https://nakamasato.medium.com/create-and-publish-your-first-python-package-a0af8a3b5e55