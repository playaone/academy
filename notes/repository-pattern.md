Why shouldn't route handlers contain database queries?
    Routes should only handle http requests and responses, and not business logic.
What is the responsibility of a repository?
    A repository is concerned with database queries.
Why is separating concerns important?
    This reduces code clusters, improves maintainability, easy debugging, and prevents repetitive codes.
Explain the flow of a request from /projects to the database.
    A clients makes a request to the /projects endpoint, the route handler validates the request, makes a call to the appropraite repository, the repository makes the database query, then returns the result to the route handler, which then responds to the client with the repository's result.

What advantages does the Repository Pattern provide when writing tests?
    Tests can be directed to the repository without involving the route handlers, providing more targeted tests.