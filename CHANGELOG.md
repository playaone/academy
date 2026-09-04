# Engineering Journey Academy — Curriculum Changelog

All notable curriculum changes are recorded here.

## [Unreleased] — 2026-09-04

### Changed

- Updated course tracking to reflect the learner's current position at Class #019.
- Recorded that Classes #014-#018 need backfill verification before being marked complete.
- Added Class #019 CI foundations review evidence.

### Added

- Added `AGENTS.md` with class closeout trigger phrases and completion rules for future coding-agent sessions.
- Added `make class-check` and `scripts/class_closeout_check.sh` to run the standard after-class verification workflow.
- Added root `.gitignore` rules for Python cache, pytest, coverage, virtual environment, and local database artifacts.

### Fixed

- Corrected the backend CI pull request path filter for `.github/workflows/backend-ci.yml`.

### Known mismatch

- `MASTER_SYLLABUS.md` still lists Class #019 as Code Quality Tooling and Class #020 as Continuous Integration, while the latest learner work identifies Class #019 as CI Foundations with GitHub Actions.

## [1.0.0] — 2026-08-03

### Added

- Semantic curriculum versioning
- Full reconstructed master syllabus through Class #200
- Roadmap phases covering:
  - Engineering foundations
  - Flask
  - Databases
  - FastAPI
  - Go
  - C# and ASP.NET Core
  - React and Next.js
  - React Native and Flutter
  - DevOps and deployment
  - AI engineering and RAG
  - System design
  - Career preparation and capstone
- Course continuation rules
- Project-state tracking
- Continuous testing requirements

### Preserved

- Learner-authoritative Classes #001–#013
- Current position at Class #014
- Existing pytest knowledge as an unnumbered earlier sub-topic

### Corrected

- Removed the inaccurate assumption that Class #014 should introduce pytest.
- Marked incomplete historical chat content as unavailable rather than reconstructing it as fact.
