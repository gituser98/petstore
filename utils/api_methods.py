from config import properties
from requests.compat import urljoin
import requests


def post_pet(payload):
    response = requests.post(properties.BASE_URL, json=payload)
    return response


def post_pet_by_id(pet_id, name, status):
    payload = 'name=' + name + '&' + 'status=' + status
    response = requests.post(urljoin(properties.BASE_URL, str(pet_id)), data=payload)
    return response


def put_pet(payload):
    response = requests.put(properties.BASE_URL, json=payload)
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


def upload_image_for_pet(pet_id, file):
    headers = {'accept': 'application/json', 'Content-Type': 'multipart/form-data'}
    url = urljoin(properties.BASE_URL, str(pet_id)) + '/uploadImage'
    response = requests.post(url, data=file, headers=headers)
    return response
