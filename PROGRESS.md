# Engineering Journey Academy Progress

Last updated: 2026-07-27T01:53:07+01:00

## Current Status

Project name: Engineering Portfolio Platform

Requested repository name: `engineering-journey-platform`

Verified local Git repository: `/home/magic/Documents/my_dev_journey/academy`

- Current active class: Class #014 - Request Validation and Serialization with Marshmallow.
- Last completed class: Class #013 - Testing Flask Applications with Pytest.
- Latest verified learning unit: Flask testing with pytest.
- Latest commit: `d36134b3d732832e4327472981642b1a42779515`
- Latest commit subject: `chore: stop tracking virtual environment`
- Branch: `master`
- Overall status: Flask backend testing foundation is complete. Tests pass. Coverage passes. Ready for Class #014.

Verification rules:

- Update this file whenever a class is completed.
- Do not mark a class complete unless its files or commands are verified.
- Do not mark a major feature complete unless implementation exists, relevant tests exist, tests pass, required migrations are applied, architecture matches the course, and this file is updated.
- If evidence is present but not tied to a numbered class, list it as verified work, not a completed numbered class.

## Completed Work

Completed classes:

- Class #002 - Git workflow.
- Class #013 - Testing Flask Applications with Pytest.

Features implemented and currently covered by passing tests:

- Flask application factory and blueprint registration in `portfolio/backend/app/__init__.py`.
- Environment-based Flask configuration, including `TestConfig`, in `portfolio/backend/app/config.py`.
- SQLAlchemy extension setup in `portfolio/backend/app/extensions.py`.
- Project model in `portfolio/backend/app/models/project.py`.
- Project repository in `portfolio/backend/app/repositories/project_repository.py`.
- Project service layer in `portfolio/backend/app/services/project_service.py`.
- Project CRUD API routes in `portfolio/backend/app/routes/project.py`.
- Health, home, and info routes in `portfolio/backend/app/routes/health.py`, `portfolio/backend/app/routes/home.py`, and `portfolio/backend/app/routes/info.py`.
- Centralized application errors and error handlers in `portfolio/backend/app/exceptions.py` and `portfolio/backend/app/error_handlers.py`.
- Alembic environment and migrations in `portfolio/backend/migrations`.
- Backend pytest foundation in `portfolio/backend/tests/`.
- Generated virtual environment, cache, and coverage artifacts are not tracked by Git.
- Project service duplicate-title typo cleanup in `portfolio/backend/app/services/project_service.py`.

Completed assignments:

| Class | Assignment / evidence | Verified status |
| --- | --- | --- |
| Class #002 | `assignments/class-002.md` | Completed answers present; Git history supports Git workflow work. |
| Class #013 | `notes/flask-testing-with-pytest.md`, `portfolio/backend/tests/` | Testing learning objectives implemented and verified by passing tests and coverage. |

Incomplete assignments:

- No incomplete assignment files were found.
- No assignment file beyond `assignments/class-002.md` was found.

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

Experiments verified:

- `experiments/execution/hello.py`
- `experiments/execution/hello.go`
- `experiments/networking/http_request.py`

Files created or modified in this progress update:

- `PROGRESS.md`
- `GRADEBOOK.md`
- `portfolio/backend/app/services/project_service.py` contains the verified typo cleanup.

Working tree status during this progress update:

- `PROGRESS.md` modified.
- `GRADEBOOK.md` added.
- `portfolio/backend/app/services/project_service.py` modified.

## Testing

Testing requirement:

- Testing is a core academy requirement.
- Major backend features should have automated tests before being marked complete.

Test framework:

- Python framework: `pytest`.
- Coverage tooling: `pytest-cov` and `coverage`.
- Flask testing: Flask test client via `portfolio/backend/tests/conftest.py`.
- Test database: per-test temporary SQLite database file created through `tmp_path`.

Test files:

- `portfolio/backend/tests/conftest.py`
- `portfolio/backend/tests/integration/test_health_routes.py`
- `portfolio/backend/tests/integration/test_project_routes.py`
- `portfolio/backend/tests/unit/test_project_service.py`

Unit tests:

- 13 service-layer tests in `portfolio/backend/tests/unit/test_project_service.py`.

Integration/API tests:

- 3 health route tests in `portfolio/backend/tests/integration/test_health_routes.py`.
- 14 project route/API tests in `portfolio/backend/tests/integration/test_project_routes.py`.

End-to-end tests:

- None found.

Passing:

- `portfolio/backend/.venv/bin/python -m pytest`
  - Result: 30 collected, 30 passed in 6.21s.
- `portfolio/backend/.venv/bin/python -m pytest --cov=app --cov-report=term-missing`
  - Result: 30 collected, 30 passed in 6.77s.

Failing or blocked:

- None in the latest check.

Current test coverage:

- Total coverage: 93%.
- Coverage command status: passing.

Coverage details from latest clean run:

| File | Coverage | Missing lines |
| --- | ---: | --- |
| `app/__init__.py` | 100% | None |
| `app/config.py` | 100% | None |
| `app/error_handlers.py` | 79% | 26, 35-42 |
| `app/exceptions.py` | 100% | None |
| `app/extensions.py` | 100% | None |
| `app/models/__init__.py` | 100% | None |
| `app/models/project.py` | 100% | None |
| `app/repositories/__init__.py` | 100% | None |
| `app/repositories/project_repository.py` | 76% | 28-30, 41-43, 50-52 |
| `app/routes/__init__.py` | 100% | None |
| `app/routes/health.py` | 100% | None |
| `app/routes/home.py` | 80% | 7 |
| `app/routes/info.py` | 80% | 8 |
| `app/routes/project.py` | 97% | 57 |
| `app/services/__init__.py` | 100% | None |
| `app/services/project_service.py` | 97% | 76, 123 |
| Total | 93% | 18 missed statements |

Commands run:

- `git status --short`
- `git log --oneline --decorate -10`
- `git log -1 --format=%H%n%h%n%ad%n%s --date=iso-strict`
- `git ls-files | grep -E '\.venv|__pycache__|\.pytest_cache|htmlcov|\.coverage'`
- `find assignments notes experiments portfolio/backend/tests portfolio/backend/app -path '*/__pycache__' -prune -o -type f -print | sort`
- `sed -n '1,220p' assignments/class-002.md`
- `sed -n '1,260p' notes/flask-testing-with-pytest.md`
- `sed -n '1,260p' portfolio/backend/tests/conftest.py`
- `sed -n '1,260p' portfolio/backend/tests/unit/test_project_service.py`
- `sed -n '1,340p' portfolio/backend/tests/integration/test_project_routes.py`
- `rg -n "existiing|priject|TODO|FIXME" portfolio/backend/app portfolio/backend/tests notes -g '!**/__pycache__/**'`
- `portfolio/backend/.venv/bin/python -m pytest`
- `portfolio/backend/.venv/bin/python -m pytest --cov=app --cov-report=term-missing`
- `portfolio/backend/.venv/bin/python -m alembic current`
- `portfolio/backend/.venv/bin/python -m alembic heads`
- `date --iso-8601=seconds`

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

Alembic current:

- `f87dbe6a3890 (head)`

Alembic head:

- `f87dbe6a3890 (head)`

Pending migrations:

- None detected by `alembic current` and `alembic heads`; current revision matches head.

## Unresolved Issues

Issue: No-op Alembic migration exists.

- Cause: `portfolio/backend/migrations/versions/7b11003d2c3a_.py` has message `empty message` and `pass` in upgrade/downgrade.
- Suggested next action: Leave it if already applied in shared history, but avoid creating empty migrations in future classes.

## Technical Debt

- Repository rollback tests.
- Database constraint tests.
- Lower coverage in repository layer: `app/repositories/project_repository.py` is 76%.
- Lower coverage in error handlers: `app/error_handlers.py` is 79%.
- Lower coverage in home/info routes: `app/routes/home.py` and `app/routes/info.py` are 80%.
- CI pipeline.
- The repository name in the academy instructions, `engineering-journey-platform`, does not match the verified local Git directory name, `academy`.

## Latest Git Commit

- Full SHA: `d36134b3d732832e4327472981642b1a42779515`
- Short SHA: `d36134b`
- Date: `2026-07-27T01:39:52+01:00`
- Subject: `chore: stop tracking virtual environment`

Recent history:

- `d36134b (HEAD -> master) chore: stop tracking virtual environment`
- `1728398 test: add Flask service and API tests`
- `5bb199d refactor: centralize API error handling`
- `050fd7f feat: add project service layer and CRUD endpoints`
- `ef3fb28 feat: implement repository pattern for project data access`
- `e3a013a feat: configure Alembic and create initial database migrations`
- `80b7c1a feat: integrate SQLAlchemy and create first model`
- `934ec08 feat: add enviroment-based configuration`
- `ff905c3 refactor: adopt Flask Application Factory and Blueprints`
- `1aac55e feat: create first Flask API`

## Next Recommended Step

Next class:

- Class #014 - Request Validation and Serialization with Marshmallow.

Preparation required:

- Add Marshmallow to backend dependencies.
- Define project request/response schemas.
- Move request validation out of route/service ad hoc checks where appropriate.
- Add tests for required fields, invalid types, unknown fields, serialized response shape, and validation error bodies.
- Keep existing pytest and coverage gates passing.
