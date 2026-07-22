class ApplicationError(Exception):
    """Base exception for expected application errors."""
    
class ValidationError(ApplicationError):
    pass

class ResourceNotFoundError(ApplicationError):
    pass

class ConflictError(ApplicationError):
    pass