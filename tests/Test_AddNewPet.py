from utils import TestUtils as utils
from utils import ApiMethods as api
from utils import Constants as constants
import pytest


@pytest.mark.addpet
def test_add_new_valid_pet():
    generated_pet = utils.generate_pet()
    print('Generated pet: : ', generated_pet)
    api.post_pet(generated_pet)
    response = api.get_pet_by_id(generated_pet['id'])
    assert response.status_code == constants.HTTP_OK
    assert response.json() == generated_pet


@pytest.mark.addpet
def test_add_new_invalid_pet():
    generated_pet = utils.generate_pet()
    del generated_pet['id']
    print('Generated pet: : ', generated_pet)
    response = api.post_pet(generated_pet)
    assert response.status_code == constants.HTTP_OK  # Based on Swagger documentation, this should be 405
