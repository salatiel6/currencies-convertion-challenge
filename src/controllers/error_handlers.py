from server import server
from .docs import default_error_model
from .exceptions import MissingArgError

api = server.api


class ErrorHandlers:
    @staticmethod
    @api.errorhandler(MissingArgError)
    @api.marshal_with(default_error_model, code=400)
    def handle_missing_arg_error_exception(error):
        return {'message': error.message}, 400
