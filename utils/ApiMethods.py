from utils import Constants as constants
from requests.compat import urljoin
import requests


def post_pet(payload):
    r = requests.post(constants.BASE_URL, json=payload)
    return r


def get_pet_by_id(pet_id):
    r = requests.get(urljoin(constants.BASE_URL, str(pet_id)), constants.HEADERS)
    return r
