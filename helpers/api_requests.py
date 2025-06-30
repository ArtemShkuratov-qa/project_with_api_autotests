import json
from dataclasses import asdict
from pathlib import Path
import allure
import requests
from requests import Response
from utils.attach_function import response_logging, response_attaching
from jsonschema import validate
from dotenv import load_dotenv
import os

load_dotenv()  # Загружает переменные из .env
BASE_URL = os.getenv("BASE_API_URL")

@allure.step('Отправляем запрос {method_type}')
def api_request(endpoint, method_type, params=None, path_params: dict = None, **kwargs):
    if path_params:
        endpoint = endpoint.format(**path_params)

    url = f"{BASE_URL}{endpoint}"
    response = requests.request(method_type, url, params=params, **kwargs)
    response_logging(response)
    response_attaching(response)
    return response

def load_schema(schema_name):
    return str(Path(__file__).parent.parent.joinpath(f'schemas/{schema_name}'))

@allure.step('Проверяем ответ на соответствие JSON-схеме')
def verify_response_json_schema(response: Response, schema_title):
    schema = load_schema(schema_title)
    with open(schema) as file:
        validate(response.json(), json.loads(file.read()))

@allure.step('Проверяем запрос на соответствие JSON-схеме')
def verify_request_json_schema(schema_title, payload):
    schema = load_schema(schema_title)
    with open(schema) as file:
        payload = asdict(payload)  # Преобразуем в словарь
        validate(payload, json.loads(file.read()))

@allure.step('Проверяем, что статус код соответствует ожидаемому')
def verify_status_code(response: Response, expected_status_code):
    assert response.status_code == expected_status_code

@allure.step('Проверяем значения из тела ответа')
def check_simple_field(response_data, field_name, expected_value):
    assert response_data[field_name] == expected_value, \
        f"{field_name}: ожидалось {expected_value}, получено {response_data[field_name]}"

@allure.step('Проверяем значения из тела ответа')
def check_condition(condition, context=""):
    if not condition:
        raise AssertionError(f"Проверка не пройдена. {context}")

