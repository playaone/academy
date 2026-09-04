# Engineering Journey Academy Gradebook

Last updated: 2026-09-04

## Summary

| Class | Topic | Assignment | Implementation | Tests | Notes | Overall |
|------|------|------:|------:|------:|------:|------:|
| #002 | Git workflow | 68 | 74 | 60 | 65 | 68 |
| Subtopic | Flask testing with pytest | 78 | 86 | 90 | 76 | 84 |
| #013 | Request Validation and Response Schemas with Marshmallow | 82 | 86 | 82 | 80 | 84 |
| #019 | CI Foundations with GitHub Actions | 87 | 84 | 95 | 86 | 87 |

Current average score, numbered reviewed classes only: 80

Current average score, including reviewed subtopics: 82

Highest score: 87 - Class #019, CI Foundations with GitHub Actions

Lowest score: 68 - Class #002, Git workflow

Most improved topic: Testing discipline and verification habits

Weakest topic: Written technical explanations

Strongest topic: Flask API testing, request validation, and CI concepts

Current engineering level: Early backend apprentice moving toward junior-backend readiness

Confidence level for continuing Class #019: Medium-high. The backend CI workflow runs the right local command, but the syllabus numbering mismatch should be resolved before marking the class complete.

Review priority list:

- Explain concepts with more precision and less shorthand.
- Explain concepts with precise boundaries, especially CI versus merging and CI versus deployment.
- Fix lingering backend technical debt: debug schema output and UTC deprecation warnings.
- Remove tracked coverage artifacts from Git.
- Resolve the Class #019/#020 syllabus mismatch.

Knowledge gap list:

- Difference between CI checks, merge policy, deployment, and continuous deployment.
- Difference between local environment state and reproducible CI state.
- Cleaner wording around process exit codes and failed CI steps.
- More precise Git terminology around commits, branches, and commit message conventions.

## Class #002 Review - Git Workflow

Evidence reviewed:

- `assignments/class-002.md`
- `notes/git-workflow.md`
- Git history containing `bfacce8 docs: complete class 002 assignment`
- Git branch history containing `class-002-git-workflow`

Score breakdown:

- Technical correctness: 27/40
- Understanding: 20/30
- Completeness: 14/20
- Engineering practices: 7/10
- Overall: 68/100

What is correct:

- The branch answer correctly identifies isolation as the main benefit.
- Commit message answer recognizes concise descriptions.
- Conventional commit labels are mostly correctly identified.
- The beginner mistake answer recognizes large, unfocused commits as a problem.

What needs correction:

- Branches are not only for avoiding direct impact to the main branch. They also support review, collaboration, experimentation, CI checks, and safe integration.
- A good commit message should explain intent and context, not only summarize files changed.
- `docs` means documentation changes, not "documentations".
- `refactor` means behavior-preserving restructuring, not simply any improvement.

Improved answer:

```text
Engineers use branches to isolate a focused change, collaborate safely, open reviews, run checks before merging, and keep the main branch stable.

A good commit message is concise, specific, and explains the intent of the change. The subject should describe what changed, and the body can explain why when context is needed.

feat adds user-visible functionality. fix corrects a bug. docs changes documentation only. refactor restructures code without changing behavior.

Beginners often make huge mixed commits, skip small commits, write vague messages, work directly on main, and forget to pull or review changes before merging.
```

Additional practice:

- Rewrite three old commit messages into stronger conventional commit messages.
- Create a branch, make two focused commits, and explain why each commit is separate.

## Subtopic Review - Flask Testing With Pytest

Evidence reviewed:

- `notes/flask-testing-with-pytest.md`
- `portfolio/backend/tests/conftest.py`
- `portfolio/backend/tests/unit/test_project_service.py`
- `portfolio/backend/tests/integration/test_health_routes.py`
- `portfolio/backend/tests/integration/test_project_routes.py`
- Passing pytest and coverage runs in earlier verification.

Score breakdown:

- Technical correctness: 34/40
- Understanding: 24/30
- Completeness: 18/20
- Engineering practices: 8/10
- Overall: 84/100

What is correct:

- Tests are organized into unit and integration folders.
- Fixtures create a Flask app and test client.
- Tests use a per-test temporary SQLite database.
- Service tests use a fake repository, which shows dependency-injection understanding.
- API tests cover success, missing required fields, invalid JSON, duplicates, missing resources, unsupported fields, empty updates, and delete behavior.

What needs correction:

- The written notes explain core testing ideas, but several answers are shallow or imprecise.
- Coverage is line execution, not proof of behavior correctness.
- The fake/mock distinction should mention interaction assertions and behavior verification.
- Some test names and formatting remain rough.

Improved answer:

```text
Unit tests verify one small unit in isolation, often replacing dependencies with fakes or mocks. Integration tests verify that multiple real components work together, such as Flask routes, service logic, SQLAlchemy, and the test database.

Coverage measures which lines or branches were executed by tests. It does not prove correctness because tests can execute code without asserting the right behavior or covering important edge cases.
```

Additional practice:

- Add schema unit tests.
- Add error-handler tests.
- Add CI that runs `pytest --cov=app --cov-report=term-missing`.

## Class #013 Review - Request Validation and Response Schemas With Marshmallow

Evidence reviewed:

- `notes/request-response-schemas.md`
- `portfolio/backend/app/schemas/project_schema.py`
- `portfolio/backend/app/routes/project.py`
- `portfolio/backend/app/error_handlers.py`
- `portfolio/backend/requirements.txt`
- `portfolio/backend/migrations/versions/d9a2cc141e6a_add_technologies_to_projects.py`
- `portfolio/backend/.venv/bin/python -m pytest`
- `portfolio/backend/.venv/bin/python -m pytest --cov=app --cov-report=term-missing`
- `portfolio/backend/.venv/bin/python -m alembic current`
- `portfolio/backend/.venv/bin/python -m alembic heads`

Score breakdown:

- Technical correctness: 33/40
- Understanding: 25/30
- Completeness: 17/20
- Engineering practices: 9/10
- Overall: 84/100

What is correct:

- Marshmallow is added to backend requirements.
- Create, update, and response schemas exist.
- Unknown fields raise validation errors.
- Required create fields and optional update fields are modeled correctly.
- Routes now call schema `load()` for request validation and `dump()` for responses.
- Validation errors are handled centrally and return structured JSON.
- Duplicate-title validation correctly remains in the service layer.
- API tests continue passing after schema integration.
- Alembic current revision matches head at `d9a2cc141e6a`.

What needs correction:

- Notes are mostly correct but still contain spelling issues and some shallow phrasing.
- `load()` does not merely "collect data"; it deserializes and validates input.
- `dump()` serializes Python objects into primitive JSON-compatible data.
- Direct schema unit tests are not present; schema behavior is mostly verified through API tests.
- `ProjectUpdateSchema.validate_and_normalize()` contains a debug `print()`, which should be removed.
- `ProjectCreateSchema` uses max title length 150 while the SQLAlchemy model column allows 200. This may be intentional, but the difference should be documented or aligned.

Improved answer:

```text
A SQLAlchemy model defines database structure and persistence behavior. A Marshmallow schema defines the API data contract: what input is accepted, how it is validated, and how objects are serialized for responses.

`load()` deserializes and validates incoming data. `dump()` serializes Python objects or model instances into JSON-compatible dictionaries.

The create schema requires `title` and `description` because a new project cannot be created without them. The update schema does not require them because PATCH can update only one field at a time.

`unknown = RAISE` rejects unexpected fields instead of silently accepting or dropping them.

Duplicate-title validation belongs in the service because it is a business rule that depends on existing application state.
```

Additional practice:

- Add direct tests for `ProjectCreateSchema`, `ProjectUpdateSchema`, and `ProjectResponseSchema`.
- Test whitespace normalization, invalid URLs, unknown fields, `allow_none`, and `load_default`.
- Remove debug output from schemas.
- Decide whether schema length limits should match database column sizes exactly.

## Class #014 Status - Testing the Layered Flask Architecture

Status: Active, not complete.

Evidence reviewed:

- `notes/repository-integration-testing.md`
- `portfolio/backend/tests/repositories/test_project_repository.py`
- Latest `pytest` run: 35 passed.
- Latest coverage run: 93%.

Current assessment:

- Repository tests were added and pass.
- The test suite now covers API, service, and repository layers.
- Class #014 is not complete yet because direct schema tests, error-handler tests, stronger rollback tests, and database constraint tests remain.

Current provisional score:

- Not graded as complete yet.

Next review requirements:

- Add a layered test matrix.
- Add direct schema unit tests.
- Add error-handler tests.
- Strengthen rollback and constraint tests.
- Keep `pytest --cov=app --cov-report=term-missing` passing.

## Class #019 Review - CI Foundations With GitHub Actions

Status: Active, reviewed but not marked complete.

Evidence reviewed:

- `notes/ci-foundations-github-actions.md`
- `.github/workflows/backend-ci.yml`
- `portfolio/backend/.venv/bin/python -m pytest`
- `portfolio/backend/.venv/bin/python -m pytest --cov=app --cov-report=term-missing`
- `.venv/bin/python -m pytest --cov=app --cov-branch --cov-report=term-missing --cov-fail-under=80` from `portfolio/backend`
- Alembic current/head from `portfolio/backend`

Score breakdown:

- Technical correctness: 34/40
- Understanding: 26/30
- Completeness: 18/20
- Engineering practices: 9/10
- Overall: 87/100

What is correct:

- The note explains CI, GitHub Actions workflow pieces, fresh environments, pytest failure signaling, and why CI must not depend on `instance/project.sql`.
- The workflow installs dependencies from `portfolio/backend/requirements.txt`.
- The workflow runs pytest with coverage and a coverage floor.
- The local CI-equivalent command passed with 72 tests and 95.02% branch-aware total coverage.

What needs correction:

- CI runs checks; it does not merge code by itself.
- Deployment and Continuous Deployment should not be treated as exactly the same idea.
- pytest failure should be described as a non-zero exit code, not only exit code 1.
- `MASTER_SYLLABUS.md` still lists Class #019 as Code Quality Tooling and Class #020 as Continuous Integration, while the latest learner note calls Class #019 CI Foundations.

Current provisional result:

- Strong pass on the written CI foundations assignment, but Class #019 should remain active until the syllabus mismatch is resolved and the workflow is committed after review.
