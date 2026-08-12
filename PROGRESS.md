# Engineering Journey Academy Progress

Last updated: 2026-08-12T01:58:27+01:00

## Current Status

Project name: Engineering Portfolio Platform

Requested repository name: `engineering-journey-platform`

Verified local Git repository: `/home/magic/Documents/my_dev_journey/academy`

- Current active class: Class #014 - Testing the Layered Flask Architecture.
- Last completed class: Class #013 - Request Validation and Response Schemas with Marshmallow.
- Latest verified learning unit: repository integration testing work inside Class #014.
- Latest commit: `c1e6b6e`
- Latest commit subject: `test: added tests for project_repository`
- Branch: `master`
- Overall status: Class #013 Marshmallow work is complete and verified. Class #014 is active; repository tests were added and the test suite passes, but schema and error-handler test gaps remain.

Verification rules:

- Update this file whenever a class is completed.
- Do not mark a class complete unless its files or commands are verified.
- Do not mark a major feature complete unless implementation exists, relevant tests exist, tests pass, required migrations are applied, architecture matches the course, and this file is updated.
- Use repository evidence, tests, coverage, migration state, and Git history instead of stale memory.

## Completed Work

Completed classes per `COURSE_TRACKER.md` and `MASTER_SYLLABUS.md`:

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
- Backend pytest foundation with API, service, and repository tests.
- Generated virtual environment, cache, and coverage artifacts are not tracked by Git.

Completed assignments / notes reviewed:

| Class / Topic | Evidence | Verified status |
| --- | --- | --- |
| Class #002 | `assignments/class-002.md`, `notes/git-workflow.md` | Completed answers present; reviewed in gradebook. |
| Flask testing subtopic | `notes/flask-testing-with-pytest.md`, `portfolio/backend/tests/` | Tests implemented and coverage verified. |
| Class #013 | `notes/request-response-schemas.md`, `app/schemas/project_schema.py`, route/schema tests through API coverage | Marshmallow learning objectives implemented and verified. |
| Class #014 active work | `notes/repository-integration-testing.md`, `tests/repositories/test_project_repository.py` | Repository tests added, but class remains active because layered test gaps remain. |

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

Experiments verified:

- `experiments/execution/hello.py`
- `experiments/execution/hello.go`
- `experiments/networking/http_request.py`

Files created or modified by this progress check:

- `PROGRESS.md`
- `GRADEBOOK.md`

Working tree status before this progress update:

- Clean.

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
- `portfolio/backend/tests/repositories/test_project_repository.py`
- `portfolio/backend/tests/unit/test_project_service.py`

Passing:

- `portfolio/backend/.venv/bin/python -m pytest`
  - Result: 35 collected, 35 passed in 8.96s.
- `portfolio/backend/.venv/bin/python -m pytest --cov=app --cov-report=term-missing`
  - Result: 35 collected, 35 passed in 10.89s.

Warnings:

- 61 warnings from SQLAlchemy/Python deprecation: `datetime.datetime.utcnow()` is deprecated; use timezone-aware UTC values.

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
| `app/error_handlers.py` | 83% | 27, 36-43 |
| `app/exceptions.py` | 100% | None |
| `app/extensions.py` | 100% | None |
| `app/models/__init__.py` | 100% | None |
| `app/models/project.py` | 93% | 18 |
| `app/repositories/__init__.py` | 100% | None |
| `app/repositories/project_repository.py` | 76% | 28-30, 41-43, 50-52 |
| `app/routes/__init__.py` | 100% | None |
| `app/routes/health.py` | 100% | None |
| `app/routes/home.py` | 80% | 7 |
| `app/routes/info.py` | 80% | 8 |
| `app/routes/project.py` | 97% | 65 |
| `app/schemas/__init__.py` | 100% | None |
| `app/schemas/project_schema.py` | 95% | 51, 96, 104 |
| `app/services/__init__.py` | 100% | None |
| `app/services/project_service.py` | 96% | 44 |
| Total | 93% | 21 missed statements |

Commands run:

- `git status --short`
- `git log --oneline --decorate -10`
- `git ls-files | grep -E '\.venv|__pycache__|\.pytest_cache|htmlcov|\.coverage'`
- `find . -path './.git' -prune -o -path './portfolio/backend/.venv' -prune -o -type f -print | sort`
- `sed -n '1,260p' COURSE_TRACKER.md`
- `sed -n '1,260p' PROJECT_STATE.md`
- `sed -n '1,260p' notes/request-response-schemas.md`
- `sed -n '1,260p' notes/repository-integration-testing.md`
- `sed -n '1,260p' portfolio/backend/app/schemas/project_schema.py`
- `sed -n '1,260p' portfolio/backend/app/routes/project.py`
- `sed -n '1,320p' portfolio/backend/tests/repositories/test_project_repository.py`
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
| `d9a2cc141e6a` | add technologies to projects | Migration file exists and is current head |

Alembic current:

- `d9a2cc141e6a (head)`

Alembic head:

- `d9a2cc141e6a (head)`

Pending migrations:

- None detected by `alembic current` and `alembic heads`; current revision matches head.

## Unresolved Issues

Issue: No-op Alembic migration exists.

- Cause: `portfolio/backend/migrations/versions/7b11003d2c3a_.py` has message `empty message` and `pass` in upgrade/downgrade.
- Suggested next action: Leave it if already applied in shared history, but avoid creating empty migrations in future classes.

Issue: Deprecation warnings in test run.

- Cause: `datetime.datetime.utcnow()` is used by SQLAlchemy defaults in `app/models/project.py`.
- Suggested next action: Move to timezone-aware UTC timestamps, then rerun tests and Alembic checks.

## Technical Debt

- Repository rollback test exists but is weak; it forces an exception with `repository.create(...)` rather than a realistic SQLAlchemy failure.
- Database constraint tests are still incomplete.
- Lower coverage in repository layer: `app/repositories/project_repository.py` is 76%.
- Lower coverage in error handlers: `app/error_handlers.py` is 83%.
- Lower coverage in home/info routes: `app/routes/home.py` and `app/routes/info.py` are 80%.
- Direct schema unit tests are not yet present; current schema behavior is mostly covered through API tests.
- CI pipeline.
- Debug `print()` remains in `ProjectUpdateSchema.validate_and_normalize`.
- The repository name in the academy instructions, `engineering-journey-platform`, does not match the verified local Git directory name, `academy`.

## Latest Git Commit

- Short SHA: `c1e6b6e`
- Subject: `test: added tests for project_repository`

Recent history:

- `c1e6b6e (HEAD -> master) test: added tests for project_repository`
- `615af46 feat: add project request and response schemas`
- `db317b4 chore: upgraded codex to a teaching assistant.`
- `d36134b chore: stop tracking virtual environment`
- `1728398 test: add Flask service and API tests`
- `5bb199d refactor: centralize API error handling`
- `050fd7f feat: add project service layer and CRUD endpoints`
- `ef3fb28 feat: implement repository pattern for project data access`
- `e3a013a feat: configure Alembic and create initial database migrations`
- `80b7c1a feat: integrate SQLAlchemy and create first model`

## Next Recommended Step

Next class:

- Continue Class #014 - Testing the Layered Flask Architecture.

Preparation required:

- Add direct schema tests for `ProjectCreateSchema`, `ProjectUpdateSchema`, and `ProjectResponseSchema`.
- Add error-handler tests for Marshmallow validation errors, HTTP exceptions, app errors, and unexpected errors.
- Strengthen repository rollback and database constraint tests.
- Remove debug `print()` from schema validation.
- Replace deprecated `datetime.utcnow` defaults with timezone-aware UTC values.
- Keep `pytest --cov=app --cov-report=term-missing` passing.
