What is a repository integration test?
    A repository integration test is an automated test designed to ensure that the data access layer of an application correctly interacts with the database.

Why do repository tests use a real database?
    Because the repository is tasked with the database operations and communication, the repository has to use a real database to ensure the operations yeild expected results.

Why should repositories return None instead of HTTP errors?
    Repositories are not concerned with business logic or user feedback, it is the responsibility of the route layer to return HTTP errors.

What layer should raise ResourceNotFoundError?
    The service layer should raise the error.

Why are repository tests important if API tests already exist?
    Repository test are important because it checks the database and data logic, while the API tests checks the whole system end-to-end.

What is the difference between:
    Service unit tests.
        Unit test to ensure business logic correctness.
    Repository integration tests
        Ensures data logic and database operations accuracy.
    API integration tests
        Full system tests, end-to-end.