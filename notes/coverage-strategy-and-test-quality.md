What does code coverage actually measure?
    Coverage measures execution, not correctness.

What's the difference between line and branch coverage?
    Line coverage checks if each executable line of code runs at least once, while branch coverage checks if every true and false outcome of each conditional decision point runs

Why can 100% coverage still contain serious bugs?
    100% code coverage only means every line or branch of code was executed during a test, not that it was tested correctly.

What makes an assertion meaningful?
    A meaningful assertion is a precise check that verifies the actual output or state of your code matches a specific expected result, rather than just confirming the code runs without crashing.

What's the difference between behavior testing and implementation-detail testing?
    Behavior testing checks what a system does from the outside using public inputs and outputs, while implementation-detail testing checks how the system works on the inside by inspecting private variables or internal function calls.

When is assert_called_once() appropriate?
    assert_called_once() is appropriate when you are using mocks to test side effects or integrations, and you need to verify that a external dependency or action was triggered exactly one time.

Why can excessive mocking weaken tests?
    Excessive mocking weakens tests because it couples tests too closely to internal code structure and creates a false sense of security by hiding real integration failures between actual components.

What is a test smell?
    A test smell is a surface indicator in test code that suggests a deeper design or maintenance problem, even if the test still passes successfully.

When should parametrization be avoided?
    Parametrization should be avoided when the test cases have different business logic, execution flows, or expected assertions, making the parameterized code overly complex and hard to read.

How can coverage reveal dead code?
    Code coverage reveals dead code by highlighting lines, branches, or entire files that never execute, even when your entire test suite runs and exercises every known feature, edge case, and user flow.

Why should a coverage threshold be based on an inspected baseline rather than an arbitrary number?
    A coverage threshold should be based on an inspected baseline because arbitrary numbers (like 80% or 90%) ignore the unique architecture, legacy code, and risk profile of your specific application.