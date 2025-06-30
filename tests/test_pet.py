import allure
import pytest
from allure_commons.types import Severity
from helpers.api_requests import api_request, verify_response_json_schema, verify_status_code, check_simple_field, \
    check_condition
from helpers.pet_helpers import create_pet, update_pet
from tests.conftest import get_headers, add_pet
from project_with_api_autotests.data import pets


@allure.title('Создание питомца со статусом "availabe"')
@allure.tag('web', 'smoke')
@allure.story('Питомец')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Shkuratov Artem')
def test_create_pet_with_available_status(get_headers):
    response = create_pet(
        pet_data=pets.dog,
        headers=get_headers
    )

    verify_response_json_schema(
        response=response,
        schema_title='pet_schema.json'
    )
    verify_status_code(response=response, expected_status_code=200)
    check_simple_field(response.json(), 'status', pets.dog.status)

@allure.title('Создание питомца со статусом "pending"')
@allure.tag('web', 'smoke')
@allure.story('Питомец')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Shkuratov Artem')
def test_create_pet_with_pending_status(get_headers):
    response = create_pet(
        pet_data=pets.cat,
        headers=get_headers
    )

    verify_response_json_schema(
        response=response,
        schema_title='pet_schema.json'
    )
    verify_status_code(response=response, expected_status_code=200)
    check_simple_field(response.json(), 'status', pets.cat.status)

@allure.title('Создание питомца со статусом "sold"')
@allure.tag('web', 'smoke')
@allure.story('Питомец')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Shkuratov Artem')
def test_create_pet_with_sold_status(get_headers):
    response = create_pet(
        pet_data=pets.lion,
        headers=get_headers
    )

    verify_response_json_schema(
        response=response,
        schema_title='pet_schema.json'
    )
    verify_status_code(response=response, expected_status_code=200)
    check_simple_field(response.json(), 'status', pets.lion.status)

@allure.title('Изменение информации о питомце')
@allure.tag('web', 'smoke')
@allure.story('Питомец')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Shkuratov Artem')
def test_update_pet(get_headers, add_pet):
    pet_id = add_pet
    updated_data = pets.lion

    response = update_pet(
        pet_data=updated_data,
        headers=get_headers,
        pet_id=pet_id
    )

    verify_response_json_schema(
        response=response,
        schema_title='pet_schema.json'
    )
    verify_status_code(response=response, expected_status_code=200)
    check_simple_field(response.json(), 'id', pet_id)
    check_simple_field(response.json(), 'name', updated_data.name)
    check_simple_field(response.json(), 'status', updated_data.status)

@allure.title("Поиск питомцев по статусу: {status}")
@allure.tag('web', 'smoke')
@allure.story("Питомец")
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Shkuratov Artem')
@pytest.mark.parametrize("status", [
    pytest.param("available", id="available_status"),
    pytest.param("pending", id="pending_status"),
    pytest.param("sold", id="sold_status")
])
def test_find_pets_by_status(get_method_endpoint, status):
    with allure.step(f"Отправка запроса для статуса {status}"):
        response = api_request(
            endpoint=get_method_endpoint,
            method_type='GET',
            params={'status': status}
        )

    verify_response_json_schema(
        response=response,
        schema_title='get_pets_schema.json'
    )
    verify_status_code(response=response, expected_status_code=200)
    check_condition(all(pet['status'] == status for pet in response.json()))

@allure.title("Поиск питомца по id")
@allure.tag('web', 'smoke')
@allure.story("Питомец")
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Shkuratov Artem')
@pytest.mark.flaky(reason="API sometimes returns 404 timeout")
def test_find_pet_by_id(get_pet_endpoint, add_pet):
    response = api_request(
        endpoint=get_pet_endpoint,
        method_type='GET',
        path_params={'id':add_pet}
    )

    verify_response_json_schema(
        response=response,
        schema_title='pet_schema.json'
    )
    verify_status_code(response=response, expected_status_code=200)
    check_simple_field(response.json(), 'id', add_pet)

@allure.title("Удаление питомца по id")
@allure.tag('web', 'smoke')
@allure.story("Питомец")
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Shkuratov Artem')
@pytest.mark.flaky(reason="API sometimes returns 404 timeout")
def test_delete_pet(get_pet_endpoint, add_pet):
    api_request(
        endpoint=get_pet_endpoint,
        method_type='DELETE',
        path_params={'id':add_pet}
    )

    response = api_request(
        endpoint=get_pet_endpoint,
        method_type='GET',
        path_params={'id':add_pet}
    )

    verify_status_code(response=response, expected_status_code=404)
    check_simple_field(response.json(), 'message', 'Pet not found')
