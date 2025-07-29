import json
from dataclasses import asdict
import random
from .api_requests import api_request
from project_with_api_autotests.data import pets


class PetHelpers:
    PET_ENDPOINT = '/v2/pet'
    FIND_BY_STATUS_ENDPOINT = '/v2/pet/findByStatus'
    PET_BY_ID_ENDPOINT = '/v2/pet/{id}'

    DEFAULT_HEADERS = {
        'accept': 'application/json',
        'Content-Type': 'application/json'
    }

    @classmethod
    def create_pet(cls, pet_data, headers=None):
        return api_request(
            endpoint=cls.PET_ENDPOINT,
            method_type="POST",
            headers=headers or cls.DEFAULT_HEADERS,
            data=json.dumps(asdict(pet_data))
        )

    @classmethod
    def update_pet(cls, pet_data, pet_id, headers=None):
        payload = asdict(pet_data)
        payload['id'] = pet_id

        return api_request(
            endpoint=cls.PET_ENDPOINT,
            method_type='PUT',
            headers=headers or cls.DEFAULT_HEADERS,
            data=json.dumps(payload)
        )

    @classmethod
    def add_pet(cls, headers=None):
        pet_instance = random.choice([pets.cat, pets.lion, pets.dog])
        payload = json.dumps(asdict(pet_instance))

        result = api_request(
            endpoint=cls.PET_ENDPOINT,
            method_type='post',
            headers=headers or cls.DEFAULT_HEADERS,
            data=payload
        )

        return result.json()['id']