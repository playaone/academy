What is the difference between a unit test and an integration test?
    Unit tests check components individually to verify they works as intended, whereas integration tests verifies how multiple components work together.

What does Arrange–Act–Assert mean?
    This is the princeple for structuring tests, first arrange the variables and conditions, Act - performs the intended test action, then Assert checks if the result is the expected result.

Why should tests use a separate database?
    Tests use a separate detabase so that the actual database is not affected by the testing operations.

What is a pytest fixture?
    A pytest fixture is a reusable function that is used in multiple test cases and pytest inserts/injects the returned value into the  function that needs it. This used instead of writing identical setups for multiple test cases.

Why must tests be independent?
    Tests must be independent to ensure that the output is not influenced by other tests. This makes the test predictable and manageable. Also tests are not ran in the order they are created so a test that depends on another may run before the dependent one.

What does pytest.mark.parametrize do?
    This gives multiple values to a test case without writing multiple instances of the same test.

What does code coverage measure?
    Code coverage measures the extent that your tests cover the functionalities implemented in your application.

Why does 100% coverage not guarantee correct software?
    100% coverage does not mean 100% test cases, which means you can get 100% coverage without writing test for all the possible scenarios that may arise while using the app.

What is the difference between a fake and a mock?
    A fake is a simplified implementation, while a mock is a preprogrammed behavior for specific methods.

Why is dependency injection helpful for testing?
    This makes it possible to use fake test values and doubles to run test operations instead and not affect production dependent programs like the database.

---

## Academy Review

Score:

- Technical correctness: 34/40
- Understanding: 24/30
- Completeness: 18/20
- Engineering practices: 8/10
- Overall: 84/100

What is correct:

- You understand the broad difference between unit and integration tests.
- You understand that tests need a separate database.
- You understand fixtures, parametrization, independence, fakes, mocks, and dependency injection at a useful beginner level.
- Your implementation verifies this learning: 30 pytest tests pass with 93% coverage.

Corrections:

- Unit tests verify one unit in isolation. Integration tests verify multiple real pieces working together.
- Arrange-Act-Assert is not just a "principle"; it is a structure: prepare, execute, verify.
- Coverage measures executed lines/branches, not "functionalities" directly.
- 100% coverage does not prove correctness because assertions may be weak and important scenarios may be missing.
- A mock is not only "preprogrammed behavior"; mocks can also verify interactions, such as whether a dependency was called.

Improved answer:

```text
Unit tests check one small unit in isolation, often replacing dependencies with fakes or mocks. Integration tests check that multiple components work together, such as routes, services, repositories, and the database.

Arrange-Act-Assert means arrange the test data and dependencies, act by running the behavior under test, and assert the expected result.

Tests use a separate database to protect real data and make tests repeatable.

A pytest fixture is reusable setup code that pytest injects into tests that request it.

Independent tests do not rely on execution order or leftover state from other tests.

Coverage measures which code lines or branches were executed by tests, not whether every behavior is correct.

A fake is a simple working substitute for a dependency. A mock is configured to return specific values and can verify how it was called.

Dependency injection makes testing easier because a service can receive a fake repository instead of using the real database repository.
```

Additional practice:

- Add repository rollback tests.
- Add database constraint tests.
- Improve coverage for `project_repository.py`, `error_handlers.py`, `home.py`, and `info.py`.
