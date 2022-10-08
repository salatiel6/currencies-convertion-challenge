from server import server
from .docs import default_error_model
from .exceptions import MissingArgError

api = server.api


class ErrorHandlers:
    """Configures all errors to be documented on swagger"""
    @staticmethod
    @api.errorhandler(MissingArgError)
    @api.marshal_with(default_error_model, code=400)
    def handle_missing_arg_error_exception(error) -> tuple:
        return {'message': error.message}, 400
