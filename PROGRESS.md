# Engineering Journey Academy Progress

Last updated: 2026-09-04

## Current Status

Project name: Engineering Portfolio Platform

Requested repository name: `engineering-journey-platform`

Verified local Git repository: `/home/magic/Documents/my_dev_journey/academy`

- Current class reported by learner: Class #019 - CI Foundations with GitHub Actions.
- Last fully verified completed class in academy records: Class #013 - Request Validation and Response Schemas with Marshmallow.
- Backfill verification needed: Classes #014-#018.
- Latest verified learning unit: Class #019 CI foundations assignment and backend GitHub Actions workflow.
- Latest commit: `baa0b754ef0d646b3014d29d8e3927d707ef23a6`
- Latest commit subject: `docs: completed my assignment for ci foundation class #019`
- Branch: `master`
- Overall status: Backend tests and coverage are healthy. Class #019 is active and reviewed, but not marked complete because the syllabus numbering mismatch must be resolved and Classes #014-#018 need class-by-class completion verification.
- Class closeout automation: `make class-check` exists and passed locally.

Verification rules:

- Update this file whenever a class is completed or the verified active class changes.
- Do not mark a class complete unless implementation, notes or assignment evidence, tests, coverage, and relevant migration state are verified.
- If migrations are involved, Alembic current must match head.
- Use repository evidence, tests, coverage, migration state, and Git history instead of stale memory.

## Completed Work

Officially verified completed classes:

- Class #001 - Thinking Like a Software Engineer.
- Class #002 - Setting Up Your Engineering Workspace Like a Professional.
- Class #003 - How Computers Execute Programs.
- Class #004 - Computer Networking for Backend Engineers.
- Class #005 - Building Your First Flask API.
- Class #006 - Flask Application Factory and Blueprints.
- Class #007 - Configuration Management with Environment Variables.
- Class #008 - Integrating SQLAlchemy and Building Your First Model.
- Class #009 - Database Migrations with Alembic.
- Class #010 - Repository Pattern.
- Class #011 - Service Layer.
- Class #012 - Global Error Handling and Safe Rollbacks.
- Class #013 - Request Validation and Response Schemas with Marshmallow.

Repository evidence after Class #013 that still needs class-by-class backfill verification:

- Layered test architecture and factories.
- Service, repository, route, schema-related, and error-handler tests.
- Coverage strategy notes.
- Backend CI workflow.
- Class #019 CI foundations notes.

Implemented backend capabilities verified in the repository:

- Flask application factory and blueprint registration in `portfolio/backend/app/__init__.py`.
- Environment-based Flask configuration, including `TestConfig`, in `portfolio/backend/app/config.py`.
- SQLAlchemy extension setup in `portfolio/backend/app/extensions.py`.
- Project model in `portfolio/backend/app/models/project.py`.
- Project repository in `portfolio/backend/app/repositories/project_repository.py`.
- Project service layer in `portfolio/backend/app/services/project_service.py`.
- Project CRUD API routes in `portfolio/backend/app/routes/project.py`.
- Health, home, and info routes.
- Centralized application and Marshmallow validation error handlers.
- Marshmallow create, update, and response schemas in `portfolio/backend/app/schemas/project_schema.py`.
- `technologies` field on projects.
- Alembic migration `d9a2cc141e6a_add_technologies_to_projects.py`.
- Backend pytest foundation with API, service, repository, and error-handler tests.
- Test factory helper in `portfolio/backend/tests/factories/project_factory.py`.
- Backend GitHub Actions workflow in `.github/workflows/backend-ci.yml`.
- Class closeout trigger instructions in `AGENTS.md`.
- Local closeout command in `Makefile` and `scripts/class_closeout_check.sh`.

Completed assignments / notes reviewed:

| Class / Topic | Evidence | Verified status |
| --- | --- | --- |
| Class #002 | `assignments/class-002.md`, `notes/git-workflow.md` | Completed answers present; reviewed in gradebook. |
| Flask testing subtopic | `notes/flask-testing-with-pytest.md`, `portfolio/backend/tests/` | Tests implemented and coverage verified. |
| Class #013 | `notes/request-response-schemas.md`, schema implementation, API coverage | Marshmallow learning objectives implemented and verified. |
| Class #019 active work | `notes/ci-foundations-github-actions.md`, `.github/workflows/backend-ci.yml` | Assignment reviewed and workflow checked locally; class remains active. |

Notes verified:

- `notes/how-programs-run.md`
- `notes/git-workflow.md`
- `notes/networking-fundamentals.md`
- `notes/flask-first-api.md`
- `notes/flask-application-factory.md`
- `notes/flask-configuration.md`
- `notes/sqlalchemy-introduction.md`
- `notes/alembic-migrations.md`
- `notes/repository-pattern.md`
- `notes/service-layer.md`
- `notes/global-error-handling.md`
- `notes/flask-testing-with-pytest.md`
- `notes/request-response-schemas.md`
- `notes/repository-integration-testing.md`
- `notes/test-architecture-and-factories.md`
- `notes/schema-and-error-handler-testing.md`
- `notes/coverage-strategy-and-test-quality.md`
- `notes/ci-foundations-github-actions.md`

## Testing

Test framework:

- Python framework: `pytest`.
- Coverage tooling: `pytest-cov` and `coverage`.
- Flask testing: Flask test client via `portfolio/backend/tests/conftest.py`.
- Test database: per-test temporary SQLite database file created through `tmp_path`.

Test files:

- `portfolio/backend/tests/conftest.py`
- `portfolio/backend/tests/factories/project_factory.py`
- `portfolio/backend/tests/integration/test_health_routes.py`
- `portfolio/backend/tests/integration/test_project_routes.py`
- `portfolio/backend/tests/repositories/test_error_handlers.py`
- `portfolio/backend/tests/repositories/test_project_repository.py`
- `portfolio/backend/tests/services/test_project_service.py`
- `portfolio/backend/tests/unit/test_project_service.py`

Passing:

- `portfolio/backend/.venv/bin/python -m pytest`
  - Result: 72 collected, 72 passed in 5.56s.
- `portfolio/backend/.venv/bin/python -m pytest --cov=app --cov-report=term-missing`
  - Result: 72 collected, 72 passed in 8.18s.
- From `portfolio/backend`: `.venv/bin/python -m pytest --cov=app --cov-branch --cov-report=term-missing --cov-fail-under=80`
  - Result: 72 collected, 72 passed in 6.11s; required coverage floor reached.
- `make class-check`
  - Result: passed; ran document presence checks, Git status/history, generated artifact scan, whitespace check, backend pytest, coverage, CI-equivalent coverage, and Alembic current/head.

Warnings:

- 70 warnings from SQLAlchemy/Python deprecation: `datetime.datetime.utcnow()` is deprecated; use timezone-aware UTC values.

Failing or blocked:

- The root-level commands `portfolio/backend/.venv/bin/python -m alembic current` and `portfolio/backend/.venv/bin/python -m alembic heads` failed with `No 'script_location' key found in configuration` because Alembic was invoked from the academy root without using the backend `alembic.ini`.
- The commands passed when rerun from `portfolio/backend`.

Current coverage:

- Line coverage: 96%.
- Branch-aware CI-equivalent coverage: 95.02%.

Branch-aware coverage details from latest CI-equivalent run:

| File | Coverage | Missing |
| --- | ---: | --- |
| `app/repositories/project_repository.py` | 85% | 41-43, 50-52 |
| `app/routes/home.py` | 80% | 7 |
| `app/routes/info.py` | 80% | 8 |
| `app/routes/project.py` | 95% | 65 |
| `app/schemas/project_schema.py` | 93% | 47->44, 51, 100->94, 104 |
| Total | 95% | 11 missed statements, 5 partial branches |

## Database And Migrations

Database:

- Development database: SQLite at `portfolio/backend/instance/project.sql`.
- Test database: per-test temporary SQLite database file.
- SQLAlchemy URI is built in `portfolio/backend/app/config.py`.

Database migrations created:

| Revision | Description | Status |
| --- | --- | --- |
| `8da7995c28d1` | create projects table | Migration file exists |
| `8e24b32091bb` | add timestamps to projects | Migration file exists |
| `7b11003d2c3a` | empty message | Migration file exists, but upgrade/downgrade are no-op |
| `f87dbe6a3890` | add website url to projects | Migration file exists |
| `d9a2cc141e6a` | add technologies to projects | Migration file exists and is current head |

Alembic current:

- From `portfolio/backend`: `d9a2cc141e6a (head)`

Alembic head:

- From `portfolio/backend`: `d9a2cc141e6a (head)`

Pending migrations:

- None detected when Alembic is run from the backend directory; current revision matches head.

## Commands Run In Latest Verification

- `git status --short`
- `git log --oneline --decorate -10`
- `git ls-files | grep -E '\.venv|__pycache__|\.pytest_cache|htmlcov|\.coverage'`
- `portfolio/backend/.venv/bin/python -m pytest`
- `portfolio/backend/.venv/bin/python -m pytest --cov=app --cov-report=term-missing`
- `portfolio/backend/.venv/bin/python -m alembic current`
- `portfolio/backend/.venv/bin/python -m alembic heads`
- From `portfolio/backend`: `.venv/bin/python -m alembic current`
- From `portfolio/backend`: `.venv/bin/python -m alembic heads`
- From `portfolio/backend`: `.venv/bin/python -m pytest --cov=app --cov-branch --cov-report=term-missing --cov-fail-under=80`
- Repository inspection commands using `sed`, `find`, `rg`, `nl`, and `git show`
- `make class-check`

## Unresolved Issues

Issue: Root-level `.coverage` is tracked by Git.

- Evidence: `git ls-files | grep -E '\.venv|__pycache__|\.pytest_cache|htmlcov|\.coverage'` returned `.coverage`.
- Impact: Running coverage from the academy root modifies a tracked generated file.
- Suggested next action: Remove it from Git tracking with an index-only cleanup and keep coverage artifacts ignored.

Issue: Class numbering mismatch.

- Evidence: `MASTER_SYLLABUS.md` lists Class #019 as Code Quality Tooling and Class #020 as Continuous Integration, but the learner reports Class #019 and the latest note is CI Foundations with GitHub Actions.
- Suggested next action: Decide whether to revise `MASTER_SYLLABUS.md` or renumber the CI foundations note/workflow evidence.

Issue: No-op Alembic migration exists.

- Evidence: `portfolio/backend/migrations/versions/7b11003d2c3a_.py` has message `empty message` and no-op upgrade/downgrade functions.
- Suggested next action: Leave it if already applied in shared history, but avoid creating empty migrations in future classes.

Issue: Deprecation warnings in test run.

- Evidence: `datetime.datetime.utcnow()` is used by SQLAlchemy defaults in `app/models/project.py`.
- Suggested next action: Move to timezone-aware UTC timestamps, then rerun tests and Alembic checks.

## Technical Debt

- `ProjectUpdateSchema.validate_and_normalize()` still contains debug `print()` output.
- Direct schema unit tests for `ProjectCreateSchema`, `ProjectUpdateSchema`, and `ProjectResponseSchema` are not clearly present as standalone tests.
- Lower coverage remains in repository failure branches, home/info routes, and one project route branch.
- The local repository directory name `academy` does not match the requested repository name `engineering-journey-platform`.

## Latest Git History

- `baa0b75 (HEAD -> master, origin/master) docs: completed my assignment for ci foundation class #019`
- `28a3b5d ci: add backend test workflow`
- `3b3d938 ci: add backend test workflow`
- `36f0d26 refactor: organize test architecture and factories`
- `7d60846 test: strengthen project service unit tests`
- `9974dd1 docs: Graded for class #014`
- `c1e6b6e test: added tests for project_repository`
- `615af46 feat: add project request and response schemas`
- `db317b4 chore: upgraded codex to a teaching assistant.`
- `d36134b chore: stop tracking virtual environment`

## Next Recommended Step

Continue Class #019 by resolving the syllabus numbering mismatch, then commit the CI workflow typo fix, class closeout automation, and Class #019 review/state updates.
