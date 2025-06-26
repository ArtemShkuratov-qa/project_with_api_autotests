import json
from dataclasses import asdict

import pytest

from helpers.api_request import api_request
from project_with_api_autotests.data import pets


@pytest.fixture
def api_url():
    return 'https://petstore.swagger.io'


@pytest.fixture
def endpoint():
    return '/v2/pet'

@pytest.fixture
def get_method_endpoint():
    return '/v2/pet/findByStatus'

@pytest.fixture()
def get_headers():
    headers = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    return headers

@pytest.fixture()
def add_pet(api_url, endpoint, get_headers):
    payload = json.dumps(asdict(pets.cat))

    result = api_request(
        api_url,
        endpoint,
        method_type='post',
        headers = get_headers,
        data=payload
    )

    return result.json()['id']


@pytest.fixture(params=['available', 'pending', 'sold'])
def pet_status(request):
    """Фикстура для параметризации тестов по статусам"""
    return request.param