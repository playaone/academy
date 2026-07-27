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