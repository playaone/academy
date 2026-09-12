class ApplicationError(Exception):
    """Base exception for expected application errors."""

    status_code = 500
    error_code = "application_error"

    def __init__(self, message):
        super().__init__(message)
        self.message = message


class ValidationError(ApplicationError):
    status_code = 400
    error_code = "validation_error"


class ResourceNotFoundError(ApplicationError):
    status_code = 404
    error_code = "resource_not_found"


class ConflictError(ApplicationError):
    status_code = 409
    error_code = "conflict"


class UnsupportedFieldError(ApplicationError):
    status_code = 400
    error_code = "unsupported_field"
