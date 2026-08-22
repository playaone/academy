What problem do test factories solve?
    They provide ready to use data for testing and reduce data declaration repetition.

What is the difference between a fixture and a factory?
    A fixture initializes dependencies while a factory initializes data.

What is fixture composition?
    This is the creation of fixtures using other fixtures

What is fixture dependency hell?
    This is where fixture composition gets too deep.

Why should database fixtures usually use function scope?
    This is to ensure that each test gets a clean db to work with.

What makes a test deterministic?
    A test is deterministic when the values are controlled and known before hand.

Why must tests not depend on execution order?
    Because tests are not ran sequencially, and tests should pass when tested individually

What does "test behavior, not implementation" mean?
    This mean the result of the tested function is more important than the implementation of the tested function.

Why are factories especially useful as schemas grow?
    Because only the factory needs to be adjusted.