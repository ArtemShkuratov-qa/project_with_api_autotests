import json
import random
from dataclasses import asdict

import pytest

from helpers.api_requests import api_request
from project_with_api_autotests.data import pets


@pytest.fixture
def endpoint():
    return '/v2/pet'

@pytest.fixture
def get_method_endpoint():
    return '/v2/pet/findByStatus'

@pytest.fixture()
def get_pet_endpoint():
    return '/v2/pet/{id}'

@pytest.fixture
def get_headers():
    return {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

@pytest.fixture()
def add_pet(endpoint, get_headers, request):
    pet_instance = random.choice([pets.cat, pets.lion, pets.dog])
    payload = json.dumps(asdict(pet_instance))

    result = api_request(
        endpoint,
        method_type='post',
        headers = get_headers,
        data=payload
    )

    return result.json()['id']

@pytest.fixture(params=['available', 'pending', 'sold'])
def pet_status(request):
    return request.param