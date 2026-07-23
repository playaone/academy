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