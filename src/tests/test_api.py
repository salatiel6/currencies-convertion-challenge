import pytest
import json
import sys
sys.path.insert(1, "../")  # Sets 'src' directory as sources root

from controllers import app  # noqa: E402
from controllers import converter  # noqa: E402
from controllers import config  # noqa: E402


@pytest.fixture
def client():
    """Starting flask app on testing environment"""
    app.config['TESTING'] = True
    client = app.test_client()

    yield client


def test_home(client):
    """Tests if the index page is working"""
    url = "/home"
    result = client.get(url)

    assert result.status_code == 200


def test_converter_with_one_param(client):
    """Tests the converter method passing only one currency"""
    amount = 100
    converted_currencie = converter.convert_with_get_geo_api(amount, "USD")

    assert converted_currencie["base_currency"] == "BRL"
    assert converted_currencie["amount"] == amount
    assert "USD" in converted_currencie["converted_currencies"].keys()
    assert len(converted_currencie["converted_currencies"]) == 1


def test_convert_route_with_valid_param(client):
    """Tests the convert route with an accepted param"""
    amount = 100
    url = f"/convert?amount={amount}"

    result = client.get(url)
    response_body = json.loads(result.data)

    assert result.status_code == 200
    assert len(response_body["converted_currencies"]) == \
           len(config.currencies)


def test_convert_route_with_invalid_param(client):
    """Tests the convert route with an unaccepted param"""
    amount = "asdf"
    url = f"/convert?amount={amount}"

    result = client.get(url)
    response_body = json.loads(result.data)

    assert result.status_code == 400
    assert response_body["message"] == "Input payload validation failed"
    assert response_body["errors"]["amount"] == \
           "could not convert string to float: 'asdf'"


def test_convert_route_with_missing_arg(client):
    """Tests the convert route without the required url param"""
    url = "/convert"

    result = client.get(url)
    response_body = json.loads(result.data)

    assert result.status_code == 400
    assert response_body["message"] == "Missing arg: 'amount'"


def test_convert_route_with_invalid_float_format(client):
    """Tests the convert route with unaccepted money format"""
    amount = "599,90"
    url = f"/convert?amount={amount}"

    result = client.get(url)
    response_body = json.loads(result.data)

    assert result.status_code == 400
    assert response_body["message"] == "Input payload validation failed"
    assert response_body["errors"]["amount"] == \
           "could not convert string to float: '599,90'"
