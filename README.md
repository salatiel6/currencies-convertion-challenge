![](https://img.shields.io/badge/version-v0.2.3-gold)  
![](https://img.shields.io/badge/python-v3.10.1-blue)
![](https://img.shields.io/badge/Flask-v2.1.2-pink)
![](https://img.shields.io/badge/Docker-v20.10.17-orange)
![](https://img.shields.io/badge/flake8-v5.0.4-purple)

![](https://img.shields.io/badge/pytest-v7.1.2-black)
![](https://img.shields.io/badge/passed_tests-6-brightgreen)
![](https://img.shields.io/badge/failed_tests-0-red)

![](https://img.shields.io/badge/coverage-99%25-brightgreen)

- [The Challenge](#the-challenge)
- [The Currencies Convert Feature](#the-currencies-convert-feature)
- [Request Example](#request-example)
- [Project Structure](#project-structure)
- [How To Run Locally](#how-to-run-locally)
- [How To Run With Docker](#how-to-run-with-docker)
- [Documentation](#documentation)

# The Challenge
The challenge was to build an API which could receive a BRL amount of money, and convert it for any other currency.

The whole solution was built with `Flask`, linted with `flake8`, tested with `pytest` and documented on swagger with `flask-restx`

## The Currencies Convert Feature
For converting the currencies, I chose to use GetGeo API, which we can get the current day rate for every currency.  
The method receives the amount to be converted and a dynamical amount of currencies. Like this:
```
def convert_with_get_geo_api(amount, *currencies) -> dict:
```
For building the request we use datetime.date to set the current day;  
Get our GetGeo API Key;  
Set the base currency as BRL;  
And we set the response format as json.
```
current_date = str(date.today())
api_key = config.currency_api_key
from_currency = "BRL"
response_format = "json"
```
Then, for every currency, we make a request for GetGeo API using the params:
```
for currency in currencies:
    url = "https://api.getgeoapi.com/v2/currency/historical/" \
          f"{current_date}?" \
          f"api_key={api_key}&" \
          f"from={from_currency}&" \
          f"to={currency}&" \
          f"amount={str(amount)}&" \
          f"format={response_format}"

    response = requests.get(url)
```
After that, we mount our response the match what was asked on the challenge:
```
if response.status_code == 200:
    data = response.json()
    converted_amount = \
        float(data["rates"][currency]["rate_for_amount"])
    converted["converted_currencies"][currency] = \
        round(converted_amount, 2)
```

## Request Example
Environment: `Local`  
Method: `GET`  
Endpoint: `http://localhost:8465/convert?amount=599.90`  

Response Body:
```
{
    "base_currency": "BRL",
    "amount": 599.9,
    "converted_currencies": {
        "USD": 115.98,
        "EUR": 119.47,
        "INR": 9558.57
    }
}
```

## Project Structure
```
src                              ----- Sources Root
|__ run.py                       ----- Gets all the configured app and runs it all.
|__ controllers                  ----- Api main features
    |__ routes.py                ----- Warps ervery api route
    |__ config.py                ----- Contains all the configuration variables
    |__ converter.py             ----- Has a class that should have one or more currency converter
    |__ error_handlers.py        ----- Configures all errors to be documented on swagger
    |__ docs                     ----- Swagger models documentation
        |__ error_models.py      ----- Models errors output for swagger
        |__ output_models.py     ----- Models successful outputs for swagger
    |__ exceptions               ----- Custom exceptions directory
        |__ missing_arg_error.py ----- Exception that handles requests without the necessaries url query arguments
|__ server                       ----- Flask API server configuration
    |__ server.py                ----- Configures flask app and api for building with swagger
|__ tests                        ----- Test cases for flask api
    |__ test_api.py              ----- All the tests
```

## How To Run Locally
Requirements:
- [Git](https://git-scm.com/downloads)
- [Python3.10](https://www.python.org/downloads/)

1. Clone the repository  
`https://github.com/salatiel6/gabriel-salatiel-eng-gruposbf-backend-python.git`


2.  Create virtual environment (recommended)  
`python -m venv ./venv`


3. Activate virtual environment (recommended)  
Windows: `venv\Scripts\activate`  
Linux/Mac: `source venv/bin/activate`


4. Open the challenge directory  
Widows/Linux:`cd gabriel-salatiel-eng-gruposbf-backend-python`  
Mac: `open gabriel-salatiel-eng-gruposbf-backend-python`


5. Install every dependencies  
`pip install -r requirements.txt`


6. Open the source directory  
Windows/Linux: `cd src`  
Mac: `open src`


7. Run tests  
Without coverage: `pytest`  
With coverage: `pytest -vv --cov=. --cov-report=term-missing --cov-config=.coveragerc`


8. Run the application  
`python run.py`


9. Check the API [Documentation](#documentation) (If you want to use Swagger)

## How To Run With Docker
This application was developed in a Windows OS. So I'm not sure if Linux or Mac could run the container.

Requirements:
- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/)

1. Clone the repository  
`https://github.com/salatiel6/gabriel-salatiel-eng-gruposbf-backend-python.git`


2. Open the challenge directory  
Widows/Linux:`cd gabriel-salatiel-eng-gruposbf-backend-python`  
Mac: `open gabriel-salatiel-eng-gruposbf-backend-python`


3. Build docker image  
`docker-compose build`


4. Start docker container  
`docker-compose up -d`


5. Check the API [Documentation](#documentation) (If you want to use Swagger)

## Documentation
The API was documented on a `swagger UI`, built with `flask-restx`.

If you run the application locally access `http://localhost:8465/docs` to check it out.  
**OBS**: Remember to check if your browser is not forcing `http` to become `https`. If it happens you won't be able to access the swagger.
