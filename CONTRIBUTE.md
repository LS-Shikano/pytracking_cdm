## Contribution

### Git Branch Policies and CI
Merging with main requires a pull request that has to pass a check defined in the ci.yml github workflow. The check ensures the code is formatted, linted, docstrings exist and are styles correctly and run tests. You can't push directly to main. Create a branch, then open a PR for merging with main. Tip: [You can create branches directly from issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/creating-a-branch-for-an-issue).  

### Dev Setup

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

### Commit messages
Follow these guidelines: https://www.conventionalcommits.org/en/v1.0.0/
- A fix commit is a PATCH. Example: 0.0.2 -> 0.0.3
- A feat commit is a MINOR. Example: 0.1.0 -> 0.2.0
- A commit with BREAKING CHANGE or ! is a MAJOR. 1.0.0 -> 2.0.0

### IDE requirements
Install [Black](https://github.com/psf/black) for formatting tooltips and [Ruff](https://github.com/charliermarsh/ruff) for linting tooltips in your IDE.

### Code documentation
This project uses [pydocstyle](https://github.com/PyCQA/pydocstyle) to enforce the existance and style of docstrings. [NumPys style guidelines](https://numpydoc.readthedocs.io/en/latest/format.html#docstring-standard) is used. To check whether your docstrings are consistent with these guidelines, run:
```bash
poetry run pydocstyle ./pytracking_cdm
```

### Testing 
To test ensure the package functions as intended after making changes, run:
```bash
poetry run pytest -svv     
```
Tests are defined in `./tests/test_pytracking_cdm.py`

### Versioning
https://johschmidt42.medium.com/setting-up-python-projects-part-v-206df3c1e3d3