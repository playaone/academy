# Engineering Journey Academy Progress

Last updated: 2026-07-27T01:01:10+01:00

## Current Status

Project name: Engineering Portfolio Platform

Requested repository name: `engineering-journey-platform`

Verified local Git repository: `/home/magic/Documents/my_dev_journey/academy`

- Current active class: Flask testing with pytest.
- Last completed class: Class 002 - Git workflow.
- Latest commit: `5bb199dc486bf8594fc6851877af8b50020db760`
- Latest commit subject: `refactor: centralize API error handling`
- Branch: `master`
- Overall status: Backend tests now exist and the plain pytest suite passes. Coverage is currently reported at 93%, but the coverage command exits with a teardown error, so the testing class should remain in progress until the coverage run is clean.

Verification rules:

- Update this file whenever a class is completed.
- Do not mark a class complete unless its files or commands are verified.
- Do not mark a major feature complete unless implementation exists, relevant tests exist, tests pass, required migrations are applied, architecture matches the course, and this file is updated.
- If evidence is present but not tied to a numbered class, list it as verified work, not a completed class.

## Completed Work

Features implemented in source:

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

Completed assignments:

| Class | Assignment file | Verified status |
| --- | --- | --- |
| Class 002 | `assignments/class-002.md` | Completed answers present |

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

Files created or modified in the current working tree:

- Deleted from root: `.env.example`, `.gitignore`, `README.md`, `requirements.txt`.
- Added under backend: `portfolio/backend/.env.example`, `portfolio/backend/.gitignore`, `portfolio/backend/README.md`.
- Modified backend files: `portfolio/backend/app/__init__.py`, `portfolio/backend/app/config.py`, `portfolio/backend/app/models/project.py`, `portfolio/backend/requirements.txt`.
- Added tests: `portfolio/backend/tests/__init__.py`, `portfolio/backend/tests/conftest.py`, `portfolio/backend/tests/integration/__init__.py`, `portfolio/backend/tests/integration/test_health_routes.py`, `portfolio/backend/tests/integration/test_project_routes.py`, `portfolio/backend/tests/unit/__init__.py`, `portfolio/backend/tests/unit/test_project_service.py`.
- Added note: `notes/flask-testing-with-pytest.md`.
- Progress file updated: `PROGRESS.md`.

## Testing

Testing requirement:

- Testing is a core academy requirement.
- Major backend features should have automated tests before being marked complete.

Test framework:

- Python framework: `pytest`.
- Coverage tooling: `pytest-cov` and `coverage`.
- Flask testing: Flask test client via `portfolio/backend/tests/conftest.py`.
- Test database: SQLite in-memory database configured by `TestConfig`.

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
- Result: 30 collected, 30 passed in 8.74s.

Failing or blocked:

- `portfolio/backend/.venv/bin/python -m pytest --cov=app`
- Result: 30 tests passed, but command exited with 1 error during teardown.
- Error: `sqlalchemy.exc.OperationalError: (sqlite3.OperationalError) no such table: projects` while `db.drop_all()` ran in `tests/conftest.py`.

Current test coverage:

- Total reported coverage: 93%.
- Important caveat: this coverage number came from a coverage run that exited with an error, so it is useful as a current measurement but not yet a clean passing coverage result.

Coverage details from latest run:

| File | Coverage |
| --- | --- |
| `app/__init__.py` | 100% |
| `app/config.py` | 100% |
| `app/error_handlers.py` | 79% |
| `app/exceptions.py` | 100% |
| `app/extensions.py` | 100% |
| `app/models/__init__.py` | 100% |
| `app/models/project.py` | 100% |
| `app/repositories/__init__.py` | 100% |
| `app/repositories/project_repository.py` | 76% |
| `app/routes/__init__.py` | 100% |
| `app/routes/health.py` | 100% |
| `app/routes/home.py` | 80% |
| `app/routes/info.py` | 80% |
| `app/routes/project.py` | 97% |
| `app/services/__init__.py` | 100% |
| `app/services/project_service.py` | 97% |
| Total | 93% |

Commands run:

- `git status --short`
- `git log -1 --format=%H%n%h%n%ad%n%s --date=iso-strict`
- `find . -path './.git' -prune -o -path './portfolio/backend/.venv' -prune -o -type f \( -name 'test_*.py' -o -name '*_test.py' -o -name 'pytest.ini' -o -name 'pyproject.toml' -o -name 'setup.cfg' -o -name 'requirements*.txt' \) -print | sort`
- `portfolio/backend/.venv/bin/python -m pytest`
- `portfolio/backend/.venv/bin/python -m pytest --cov=app`
- `portfolio/backend/.venv/bin/alembic current`
- `portfolio/backend/.venv/bin/alembic heads`
- `date --iso-8601=seconds`
- `git diff --name-status`
- `git diff --cached --name-status`

## Database And Migrations

Database:

- Development database: SQLite at `portfolio/backend/instance/project.sql`.
- Test database: SQLite in-memory database from `TestConfig`.
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

Issue: Coverage command fails during teardown.

- Cause: `db.drop_all()` in `portfolio/backend/tests/conftest.py` attempted to drop `projects`, but SQLite reported `no such table: projects`.
- Suggested next action: Make the test database fixture lifecycle deterministic, then rerun `pytest --cov=app` until it exits successfully.

Issue: Coverage is measured but not clean.

- Cause: `pytest --cov=app` reported 93% total coverage but exited with status 1 because of the teardown error.
- Suggested next action: Treat 93% as the current reported coverage, not as a completed passing coverage gate.

Issue: Project service contains typo debt if still present after current edits.

- Cause: Previous inspection found `existiing_project` and error text `A priject with this title already exists` in `portfolio/backend/app/services/project_service.py`.
- Suggested next action: Verify the current file and cover duplicate-title update behavior with a service or API test.

Issue: No-op Alembic migration exists.

- Cause: `portfolio/backend/migrations/versions/7b11003d2c3a_.py` has message `empty message` and `pass` in upgrade/downgrade.
- Suggested next action: Leave it if already applied in shared history, but avoid creating empty migrations in future classes.

Issue: Generated artifacts are tracked or present.

- Cause: Git status shows tracked `__pycache__` changes, and local generated coverage artifacts exist under `portfolio/backend/.coverage` and `portfolio/backend/htmlcov/`.
- Suggested next action: Remove generated artifacts from Git tracking with a non-destructive index-only cleanup and ensure backend `.gitignore` excludes caches and coverage output.

## Technical Debt

- Coverage run is not clean yet.
- Repository tests for transaction rollback/database constraints are not yet visible in the current test files inspected.
- No CI workflow exists.
- Some generated artifacts are tracked or present in the working tree.
- The repository name in the academy instructions, `engineering-journey-platform`, does not match the verified local Git directory name, `academy`.

## Latest Git Commit

- Full SHA: `5bb199dc486bf8594fc6851877af8b50020db760`
- Short SHA: `5bb199d`
- Date: `2026-07-24T00:00:57+01:00`
- Subject: `refactor: centralize API error handling`

## Next Recommended Step

Next class:

- Finish Flask backend testing foundation.

Preparation required:

- Fix the coverage-run teardown error in `portfolio/backend/tests/conftest.py`.
- Rerun `portfolio/backend/.venv/bin/python -m pytest --cov=app`.
- Add focused tests for repository rollback/database constraints if they are part of the current class.
- Update this file after the coverage command exits successfully.
