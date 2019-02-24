from config import properties
from requests.compat import urljoin
import requests


def post_pet(payload):
    response = requests.post(properties.BASE_URL, json=payload)
    return response


def get_pet_by_id(pet_id):
    response = requests.get(urljoin(properties.BASE_URL, str(pet_id)), properties.HEADERS)
    return response


def get_pet_by_status(status):
    url = properties.BASE_URL + 'findByStatus?status=' + status
    response = requests.get(url, properties.HEADERS)
    return response


def delete_pet_by_id(pet_id):
    response = requests.delete(urljoin(properties.BASE_URL, str(pet_id)))
    return response
