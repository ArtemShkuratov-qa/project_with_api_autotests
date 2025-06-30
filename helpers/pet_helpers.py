import json
from dataclasses import asdict
from .api_requests import api_request


def create_pet(pet_data, headers):
    return api_request(
        endpoint="/v2/pet",
        method_type="POST",
        headers=headers,
        data=json.dumps(asdict(pet_data))
    )

def update_pet(pet_data, headers, pet_id):
    payload = asdict(pet_data)
    payload['id'] = pet_id

    return api_request(
        endpoint='/v2/pet',
        method_type='PUT',
        headers=headers,
        data=json.dumps(payload)
    )