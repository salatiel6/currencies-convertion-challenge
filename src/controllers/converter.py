import requests
from datetime import date
from .config import config


class Converter:
    @staticmethod
    def convert(amount, *currencies):
        current_date = str(date.today())
        api_key = config.currency_api_key
        from_currency = "BRL"
        response_format = "json"

        converted = {
            "base_currency": from_currency,
            "amount": amount,
            "converted_currencies": {}
        }

        for currency in currencies:
            url = "https://api.getgeoapi.com/v2/currency/historical/" \
                  f"{current_date}?" \
                  f"api_key={api_key}&" \
                  f"from={from_currency}&" \
                  f"to={currency}&" \
                  f"amount={str(amount)}&" \
                  f"format={response_format}"

            response = requests.get(url, verify=False)

            if response.status_code == 200:
                data = response.json()
                converted_amount = \
                    float(data["rates"][currency]["rate_for_amount"])
                converted["converted_currencies"][currency] = \
                    round(converted_amount, 2)

        return converted


converter = Converter()
