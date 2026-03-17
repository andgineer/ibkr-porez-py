> **⚠️ This project has been superseded by the [Rust version](https://github.com/andgineer/ibkr-porez).**
> **The Rust version is significantly smaller in install/binary size and is actively maintained.**
>
> This Python version remains functional and database-compatible, but is no longer actively developed.
> If you prefer this Python version, feel free to fork or contribute -- PRs are accepted.

[![Build Status](https://github.com/andgineer/ibkr-porez-py/workflows/CI/badge.svg)](https://github.com/andgineer/ibkr-porez-py/actions)
[![Coverage](https://raw.githubusercontent.com/andgineer/ibkr-porez-py/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/andgineer/ibkr-porez-py/blob/python-coverage-comment-action-data/htmlcov/index.html)
# ibkr-porez (Python)

Automated PPDG-3R and PP-OPO tax reports generation for Interactive Brokers.
It automatically fetches your data and generates a ready-to-upload XML files with all prices converted to RSD.

# Quick Start

Graphical installers are available for Windows and macOS - see [releases](https://github.com/andgineer/ibkr-porez-py/releases)
but they are large.

The recommended lightweight installation method is [`uv tool`](https://docs.astral.sh/uv/getting-started/installation/):

```bash
uv tool install ibkr-porez
ibkr-porez  # without arguments launches the graphical interface; for CLI see `--help`
```

If you use the graphical interface, configure your data (the `Config` button),
then just use `Sync` to refresh data and create declarations.

If CLI is your native language (AI agents and brave humans) see [ibkr-porez docs](https://andgineer.github.io/ibkr-porez-py/).

---

# Developers

Do not forget to run `. ./activate.sh`.

For work it need [uv](https://github.com/astral-sh/uv) installed.

Use [pre-commit](https://pre-commit.com/#install) hooks for code quality:

    pre-commit install

## Allure test report

* [Allure report](https://andgineer.github.io/ibkr-porez-py/builds/tests/)

# Scripts

Install [invoke](https://docs.pyinvoke.org/en/stable/) preferably with [uv tool](https://docs.astral.sh/uv/):

    uv tool install invoke

For a list of available scripts run:

    invoke --list

For more information about a script run:

    invoke <script> --help


## Coverage report
* [Codecov](https://app.codecov.io/gh/andgineer/ibkr-porez-py/tree/main/src%2Fibkr_porez)
* [Coveralls](https://coveralls.io/github/andgineer/ibkr-porez-py)

> Created with cookiecutter using [template](https://github.com/andgineer/cookiecutter-python-package)
