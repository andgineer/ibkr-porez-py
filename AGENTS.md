# Repository Guidelines

## Project Structure & Module Organization
Core code lives in `src/ibkr_porez/`.
- CLI entrypoint and commands: `src/ibkr_porez/main.py` and `operation_*.py`.
- GUI (PySide6): `src/ibkr_porez/gui/`.
- Domain logic: tax/report/declaration/storage modules in `src/ibkr_porez/`.

Tests are in `tests/`, with fixtures in `tests/conftest.py` and sample inputs in `tests/resources/`.
Docs are under `docs/` (multilingual content in `docs/src/<lang>/`).
Automation scripts are in `scripts/`, and task shortcuts are in `tasks.py`.

## Build, Test, and Development Commands
Use Python 3.12+ and `uv`.
- `. ./activate.sh`: create/activate `.venv` and sync dependencies.
- `uv sync --frozen`: install exact locked dependencies.
- `uv run ibkr-porez`: run the app (GUI opens when no subcommand is given).
- `uv run python -m pytest tests/`: run full test suite.
- `uv run python -m pytest --cov=src --cov-report=term-missing:skip-covered tests/`: run tests with coverage (CI-equivalent).
- `pre-commit run --verbose --all-files` or `invoke pre`: run lint/format/type checks.
- `./scripts/build-docs.sh`: build documentation site.

## Coding Style & Naming Conventions
Follow existing Python style:
- 4-space indentation, type hints on new/changed public APIs, and concise docstrings where needed.
- Module/file names use `snake_case`; tests use `test_*.py`.
- Keep lines around the configured Ruff/Flake8 limit (about 100 chars).
- Run pre-commit before pushing; it enforces Ruff lint/format and pyrefly checks.

## Testing Guidelines
Pytest is the test framework (`pytest.ini` enables doctests).
Keep tests deterministic and isolated from user state; reuse `tests/conftest.py` fixtures and `tests/resources/` data files.
Naming patterns used here:
- unit/regression: `test_<feature>.py`, `test_*_unit.py`
- end-to-end: `test_e2e_*.py`

## Commit & Pull Request Guidelines
Recent history favors short, imperative commit messages (for example, `refactor status management`) and issue links when applicable.
For releases, maintainers use version bump commits (`Version vX.Y.Z ...`).

For PRs:
- explain user-visible changes and risk areas,
- link related issues,
- include screenshots for GUI changes (`src/ibkr_porez/gui/`),
- ensure CI passes (`pytest` + `pre-commit`) before requesting review.
