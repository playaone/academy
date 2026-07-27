What is the difference between an expected application error and an unexpected error?
    An expected application error is a type of error encoutered during normal application use, such as validation errors when user inputs invalid values, while unexpected errors are error that occur when the application is unable to perform an operation due to one reason or the other, example is database operation error.

Why should routes not repeatedly catch the same exceptions?
    This makes the routes noisy and maintenace more tricky.

Why must failed SQLAlchemy sessions be rolled back?
    To avoid stale sessions and operations which may lead to errors like pendingRollbackError

Why should internal exception messages not be sent directly to clients?
    Internal exception messages may contain sensitive values that only the developers should see.

What is the difference between:
    ApplicationError
        These are app developer defined exception handlers.
    HTTPException
        This is flask reserved/internal class for HTTP exception handling.
    Exception
        This is python internal exception class.

Explain the error flow when ProjectService raises ResourceNotFoundError.
    User makes a request, the request handler validates it and call ProjectService to process the request, ProjectService calls the repository for the requested resource, repository returns nothing, ProjectService raises the ResourceNotFoundError.

---

## Academy Review

Score:

- Technical correctness: 31/40
- Understanding: 24/30
- Completeness: 16/20
- Engineering practices: 8/10
- Overall: 79/100

What is correct:

- You understand that expected application errors are part of normal app behavior.
- You understand route-level repeated exception handling causes noisy code.
- You understand failed SQLAlchemy sessions must be rolled back.
- You understand internal exception messages should not be leaked to clients.

Corrections:

- `ApplicationError` is a custom exception class, not an exception handler.
- `HTTPException` is Werkzeug/Flask's base for HTTP-aware exceptions such as 404.
- `Exception` is Python's general base class for many errors; it is not specifically an "internal exception class".
- The ResourceNotFound flow should continue through the centralized error handler, which converts the exception into a JSON response and status code.

Improved answer:

```text
An expected application error is a known business or validation problem, such as invalid input or a missing project. An unexpected error is a bug or infrastructure failure the app did not intentionally model.

Routes should not repeatedly catch the same exceptions because centralized error handlers keep route code clean and make response formatting consistent.

Failed SQLAlchemy sessions must be rolled back because the session enters a failed state after certain database errors.

Internal exception messages should not be sent to clients because they may expose secrets, SQL details, file paths, or implementation details.

`ApplicationError` is the app's custom base exception. `HTTPException` is Flask/Werkzeug's HTTP exception base. `Exception` is Python's general exception base.

When `ProjectService` raises `ResourceNotFoundError`, Flask passes it to the registered error handler, which returns a safe JSON error body with a 404 status code.
```

Additional practice:

- Add tests for every custom error type.
- Add one test proving unexpected exceptions return a generic safe message.
