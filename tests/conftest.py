import pytest
from helpers.pet_helpers import PetHelpers
from project_with_api_autotests.data import pets


@pytest.fixture
def add_pet():
    """Фикстура создает питомца и возвращает его ID"""
    response = PetHelpers.create_pet(pets.dog)
    return response.json()['id']