"""Modeling successfull outputs for swagger"""

from flask_restx import fields
from server import server


converted_currencies_model = server.api.model(
    "converted_currencies_model", {
        "CUR": fields.Float(default=0.0),
        "REN": fields.Float(default=0.0),
        "CYS": fields.Float(default=0.0)
    }
)

convert_output_model = server.api.model(
    "convert_output_model", {
        "base_currency": fields.String(default="BRL"),
        "amount": fields.Float(),
        "converted_currencies": fields.Nested(converted_currencies_model)
    }
)
