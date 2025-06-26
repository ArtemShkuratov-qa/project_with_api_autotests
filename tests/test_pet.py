import json
from dataclasses import asdict

import allure
import pytest

from helpers.api_request import api_request
from tests.conftest import api_url, endpoint, get_headers, add_pet
from project_with_api_autotests.data import pets


def test_create_pet_with_available_status(api_url, endpoint, get_headers):
    payload = json.dumps(asdict(pets.dog))

    result = api_request(
        api_url,
        endpoint,
        method_type='post',
        headers = get_headers,
        data=payload)

    assert result.status_code == 200
    assert result.json()['status'] == pets.dog.status

def test_create_pet_with_pending_status(api_url, endpoint, get_headers):
    payload = json.dumps(asdict(pets.cat))

    result = api_request(
        api_url,
        endpoint,
        method_type='post',
        headers = get_headers,
        data=payload)

    assert result.status_code == 200
    assert result.json()['status'] == pets.cat.status

def test_create_pet_with_sold_status(api_url, endpoint, get_headers):
    payload = json.dumps(asdict(pets.lion))

    result = api_request(
        api_url,
        endpoint,
        method_type='post',
        headers = get_headers,
        data=payload)

    assert result.status_code == 200
    assert result.json()['status'] == pets.lion.status


def test_update_pet(api_url, endpoint, get_headers, add_pet):
    pet_id = add_pet
    payload = asdict(pets.lion)
    payload['id'] = pet_id
    payload = json.dumps(payload)

    result = api_request(
        api_url,
        endpoint,
        method_type='put',
        headers=get_headers,
        data=payload
    )

    assert result.status_code == 200
    assert result.json() == json.loads(payload)


@allure.title("Поиск питомцев по статусу: {status}")
@allure.feature("Pet API")
@allure.story("GET /pet/findByStatus")
@pytest.mark.parametrize("status", [
    pytest.param("available", id="available_status"),
    pytest.param("pending", id="pending_status"),
    pytest.param("sold", id="sold_status")
])
def test_find_pets_by_status(api_url, get_method_endpoint, status):
    with allure.step(f"Отправка запроса для статуса {status}"):
        response = api_request(
            base_api_url=api_url,
            endpoint=get_method_endpoint,
            method_type='GET',
            params={'status': status}
        )

    with allure.step("Проверка ответа"):
        assert response.status_code == 200
        assert all(pet['status'] == status for pet in response.json())
