What is the main responsibility of the Service Layer?
    The service layer is responsible for business logic and validation.

Why should validation not live inside the repository?
    Data validation is part of business logic given that business logic is determined by the data received.

Why should HTTP status codes not be decided by the service?
    HTTP status codes should not be decided by the service layer because the service layer only handles the business logic, the routes are responsible for the request validation and providing necessary responses to the client.

Explain the request flow for POST /projects.
    The server receives the request along with the associated data, the HTTP method determines which of the route handlers will be responsible for this request, in this case, the create_project handler. The data received is then sent to the project.create_project service to validate and process the data. The service processes the data and upon successful validation the data is sent to the repository to create a new project. The repository executes this and return the new project to the service which return it to the route handler. The route handler then send it to the client with a 201 status code.

How does repository injection make the service easier to test?
    Because the service layer is structured to accept repository dependency injection, testing is much easier as testers can now create test repositories for the service.

What is the difference between:
    400 Bad Request
        This is the HTTP error status code for validation error, which means the user did not send the correct data.
    404 Not Found
        This means the requested resource was not found by the server.
    409 Conflict
        This means there is already a conflicting resource as the one the user is trying to create.

---

## Academy Review

Score:

- Technical correctness: 33/40
- Understanding: 25/30
- Completeness: 18/20
- Engineering practices: 8/10
- Overall: 84/100

What is correct:

- You correctly identify business logic and validation as service-layer responsibilities.
- You correctly keep HTTP status codes out of the service layer.
- Your POST `/projects` flow is mostly aligned with the implemented architecture.
- You understand repository injection as a testing tool.

Corrections:

- Some validation will eventually move into request schemas, especially in Class #014 with Marshmallow. The service should still enforce business rules that must remain true regardless of the HTTP layer.
- The route should parse and validate basic request shape, but detailed request validation and serialization should become schema-driven.
- `409 Conflict` can apply to create or update operations when the requested state conflicts with existing data.

Improved answer:

```text
The service layer owns business rules: required business fields, duplicate-title checks, missing-resource behavior, and deciding which repository operation should happen.

Validation should not live in the repository because the repository should focus on persistence, not business meaning.

HTTP status codes belong in the route or error-handler layer because they are part of the HTTP interface, not the business rule itself.

For POST `/projects`, the route receives JSON, validates request shape, calls the service, the service validates business rules, the repository creates the row, the service returns the project, and the route returns JSON with status 201.

Repository injection makes service tests easier because tests can pass a fake repository instead of touching the real database.
```

Additional practice:

- Decide which validations belong in Marshmallow schemas and which must remain service business rules.
- Add service tests for update duplicate-title conflicts.
