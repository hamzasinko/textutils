# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-11-13

### Added

- `word_count` and `character_count` helpers.
- `reverse` and `capitalize_words` helpers, with type hints and NumPy-style docstrings.
- `slugify` helper for URL-friendly slugs ([#2](https://github.com/hamzasinko/textutils/pull/2)).
- Public API exported from `textutils` via `__all__`, with tests covering the surface.
- Input validation that raises `TypeError` for non-string input.
- Test suite with pytest and coverage configuration.
- Packaging metadata in `pyproject.toml`, README, and MIT license.
- pre-commit hooks and GitHub Actions CI ([#3](https://github.com/hamzasinko/textutils/pull/3)).

### Changed

- Split the helpers into `counting` and `transform` modules.
- Moved tests to a top-level `tests/` directory mirroring the modules.
- Formatted the code with Black and fixed Ruff lint issues.
- Converted docstrings to NumPy style.

### Fixed

- Corrected the `capitalize_words` docstring example.

[0.1.0]: https://github.com/hamzasinko/textutils/releases/tag/v0.1.0
