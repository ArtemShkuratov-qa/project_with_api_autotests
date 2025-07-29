import allure
import pytest
from allure_commons.types import Severity
from helpers.api_requests import api_request, verify_response_json_schema, verify_status_code, check_simple_field, \
    check_condition, verify_request_json_schema
from helpers.pet_helpers import PetHelpers  # Импортируем весь класс
from project_with_api_autotests.data import pets


@allure.title('Создание питомца со статусом "available"')
@allure.tag('web', 'smoke')
@allure.story('Питомец')
@allure.severity(Severity.BLOCKER)
@allure.label('owner', 'Shkuratov Artem')
def test_create_pet_with_available_status():
    response = PetHelpers.create_pet(
        pet_data=pets.dog,
        headers=PetHelpers.DEFAULT_HEADERS  # Используем стандартные заголовки
    )

    verify_request_json_schema(
        schema_title='request_pet_schema.json',
        payload=pets.dog
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
def test_create_pet_with_pending_status():
    response = PetHelpers.create_pet(
        pet_data=pets.cat,
        headers=PetHelpers.DEFAULT_HEADERS
    )

    verify_request_json_schema(
        schema_title='request_pet_schema.json',
        payload=pets.dog
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
def test_create_pet_with_sold_status():
    response = PetHelpers.create_pet(
        pet_data=pets.lion,
        headers=PetHelpers.DEFAULT_HEADERS
    )

    verify_request_json_schema(
        schema_title='request_pet_schema.json',
        payload=pets.dog
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
def test_update_pet(add_pet):  # Используем фикстуру
    pet_id = add_pet
    updated_data = pets.lion

    response = PetHelpers.update_pet(
        pet_data=updated_data,
        pet_id=pet_id
    )

    verify_request_json_schema(
        schema_title='request_pet_schema.json',
        payload=updated_data
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
def test_find_pets_by_status(status):
    response = api_request(
        endpoint=PetHelpers.FIND_BY_STATUS_ENDPOINT,  # Используем константу из класса
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
@pytest.mark.flaky(reason="Сервис периодически возвращает статус код 404")
def test_find_pet_by_id(add_pet):
    response = api_request(
        endpoint = f"{PetHelpers.PET_BY_ID_ENDPOINT.format(id=add_pet)}",
        method_type='GET'
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
@pytest.mark.flaky(reason="Сервис периодически возвращает статус код 404")
def test_delete_pet(add_pet):
    api_request(
        endpoint=f"{PetHelpers.PET_BY_ID_ENDPOINT.format(id=add_pet)}",
        method_type='DELETE'
    )

    response = api_request(
        endpoint=f"{PetHelpers.PET_BY_ID_ENDPOINT.format(id=add_pet)}",
        method_type='GET'
    )

    verify_status_code(response=response, expected_status_code=404)
    check_simple_field(response.json(), 'message', 'Pet not found')
