import logging

from flask import Flask, request
from marshmallow.exceptions import ValidationError as MarshmallowValidationError
from werkzeug.exceptions import HTTPException

from app.exceptions import ApplicationError
from app.extensions import db

logger = logging.getLogger(__name__)


def register_error_handlers(app: Flask):
    @app.errorhandler(ApplicationError)
    def handle_application_error(error):
        db.session.rollback()

        return {
            "error": {"code": error.error_code, "message": error.message}
        }, error.status_code

    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        return {
            "error": {
                "code": error.name.lower().replace(" ", "_"),
                "message": error.description,
            }
        }, error.code

    @app.errorhandler(Exception)
    def handle_unexpected_error(error):
        db.session.rollback()

        logger.exception("Unhandled application error", exc_info=error)

        return {
            "error": {
                "code": "internal_server_error",
                "message": "An unexpected error occured",
            }
        }, 500

    @app.errorhandler(MarshmallowValidationError)
    def handle_schema_validation_error(error):
        return {
            "error": {
                "code": "validation_error",
                "message": "Request validation failed",
                "details": error.messages,
                "path": request.path,
            }
        }, 400
