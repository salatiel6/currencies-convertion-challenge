from flask_restx import fields
from server import server

default_error_model = server.api.model(
    "default_error_model", {
        "message": fields.String(default="$_ERROR_MESSAGE")
    }
)
