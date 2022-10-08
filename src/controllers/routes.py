from server import server
from flask_restx import Resource, reqparse

from .config import config
from .converter import converter
from .error_handlers import ErrorHandlers
from .docs import default_error_model, convert_output_model
from .exceptions import MissingArgError

app, api = server.app, server.api
parser = reqparse.RequestParser()
error_handlers = ErrorHandlers


@app.route("/home")
def home():
    return f"Grupo SBF Challenge API - {api.version}", 200


@api.route("/convert", doc={
    "description": "Receives the product amount and coverts to the defined"
                   " currencies"
})
class Convert(Resource):
    parser.add_argument("amount", type=float, location="args")

    @staticmethod
    @api.expect(parser)
    @api.response(200, "SUCCESS", convert_output_model)
    @api.response(400, "BAD REQUEST", default_error_model)
    def get():
        args = parser.parse_args()
        amount = args["amount"]

        if amount:
            currencies = config.currency_list

            converted_currencies = converter.convert(amount, *currencies)

            return converted_currencies, 200
        else:
            raise MissingArgError("amount")
