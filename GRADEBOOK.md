# Engineering Journey Academy Gradebook

Last updated: 2026-07-27T01:53:07+01:00

## Summary

| Class | Topic | Assignment | Implementation | Tests | Notes | Overall |
|------|------|------:|------:|------:|------:|------:|
| #002 | Git workflow | 68 | 74 | 60 | 65 | 68 |
| #013 | Testing Flask Applications with Pytest | 78 | 86 | 90 | 76 | 84 |

Current average score: 76

Highest score: 84 - Class #013, Testing Flask Applications with Pytest

Lowest score: 68 - Class #002, Git workflow

Most improved topic: Testing discipline and verification habits

Weakest topic: Written technical explanations

Strongest topic: Flask API testing with pytest

Current engineering level: Early backend apprentice moving toward junior-backend readiness

Confidence level for moving to the next class: High for Class #014, with continued review of validation boundaries

Review priority list:

- Explain concepts with more precision and less shorthand.
- Add repository rollback and database constraint tests.
- Increase coverage for repository, error-handler, home, and info route modules.
- Keep generated files out of Git.
- Add CI when the testing workflow stabilizes.

Knowledge gap list:

- Difference between code coverage and behavioral completeness.
- Database constraints and transaction rollback verification.
- Cleaner separation of request validation, service rules, and serialization.
- More precise Git terminology around commits, branches, and commit message conventions.

## Class #002 Review - Git Workflow

Evidence reviewed:

- `assignments/class-002.md`
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

## Class #013 Review - Testing Flask Applications with Pytest

Evidence reviewed:

- `notes/flask-testing-with-pytest.md`
- `portfolio/backend/tests/conftest.py`
- `portfolio/backend/tests/unit/test_project_service.py`
- `portfolio/backend/tests/integration/test_health_routes.py`
- `portfolio/backend/tests/integration/test_project_routes.py`
- `portfolio/backend/.venv/bin/python -m pytest`
- `portfolio/backend/.venv/bin/python -m pytest --cov=app --cov-report=term-missing`
- Git commits `1728398 test: add Flask service and API tests` and `d36134b chore: stop tracking virtual environment`

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
- `pytest` passes with 30 tests.
- Coverage passes cleanly at 93%.
- Generated environment/cache/coverage artifacts are not tracked by Git.

What needs correction:

- The written notes explain core testing ideas, but several answers are shallow or imprecise.
- "100% coverage does not mean 100% test cases" is a useful start, but the deeper point is that coverage says lines executed, not behavior validated.
- The fake/mock distinction should mention interaction assertions and behavior verification.
- Tests do not yet visibly cover repository rollback behavior or database constraints.
- Some test names and formatting are still rough, for example `test_service_detetion_successful`.

Improved answer:

```text
Unit tests verify one small unit in isolation, often replacing dependencies with fakes or mocks. Integration tests verify that multiple real components work together, such as Flask routes, service logic, SQLAlchemy, and the test database.

Arrange-Act-Assert means prepare the input and dependencies, perform the behavior under test, then verify the expected outcome.

Tests use a separate database to protect real data, make test results repeatable, and allow cleanup after every test.

Coverage measures which lines or branches were executed by tests. It does not prove correctness because tests can execute code without asserting the right behavior or covering important edge cases.
```

Additional practice:

- Add repository tests that force SQLAlchemy errors and assert rollback behavior.
- Add tests for database constraints.
- Add targeted tests for `error_handlers.py`, `home.py`, and `info.py`.
- Add a CI workflow that runs `pytest --cov=app`.
