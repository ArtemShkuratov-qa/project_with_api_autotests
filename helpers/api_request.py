import requests
from utils.attach_function import response_logging, response_attaching


def api_request(base_api_url, endpoint, method_type, params=None, **kwargs):
    url = f"{base_api_url}{endpoint}"
    response = requests.request(method_type, url, params=params, **kwargs)
    response_logging(response) # логирование запроса и ответа
    response_attaching(response) # добавление аттачей
    return response
