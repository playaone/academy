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

---

## Academy Review

Score:

- Technical correctness: 31/40
- Understanding: 24/30
- Completeness: 16/20
- Engineering practices: 8/10
- Overall: 79/100

What is correct:

- You understand that route handlers should not contain database queries.
- You correctly identify the repository as the database access layer.
- You understand separation of concerns improves maintainability and testing.

Corrections:

- Routes should avoid both database queries and business logic. In your current architecture, routes should call services, and services should call repositories.
- The request flow answer skips the service layer, which is important because your implementation uses `ProjectService`.
- Repository pattern testing is not only about testing the repository directly; it also lets service tests use fake repositories.

Improved answer:

```text
Route handlers should not contain database queries because routes should focus on HTTP input and output. Business rules belong in the service layer, and database access belongs in the repository.

A repository encapsulates database operations such as querying, creating, updating, and deleting records.

Separating concerns keeps code easier to test, debug, and change.

For `/projects`, the route receives the HTTP request, calls the service, the service applies business rules, the service calls the repository, the repository queries the database, and the result flows back through the service to the route response.

The Repository Pattern helps tests because service tests can use fake repositories, and repository tests can focus specifically on database behavior.
```

Additional practice:

- Draw the request flow: route -> service -> repository -> database.
- Add repository tests for create, update, delete, and rollback behavior.
