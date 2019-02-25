from utils import test_utils
from utils import api_methods
from utils import constants
import pytest
import logging
import random

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


@pytest.mark.findpetbyid
def test_get_by_id():
    generated_pet = test_utils.generate_pet()
    logger.info('Posting pet: {0}'.format(generated_pet))
    api_methods.post_pet(generated_pet)
    response = api_methods.get_pet_by_id(generated_pet['id'])

    assert response.status_code == constants.HTTP_OK
    assert generated_pet == response.json()


@pytest.mark.findpetbyid
def test_get_by_nonexistent_id():
    pet_id = random.randint(900000000, 999999999)
    logger.info('Find a nonexistent pet with id: {0}'.format(pet_id))
    assert api_methods.get_pet_by_id(pet_id).status_code == constants.HTTP_NOT_FOUND


@pytest.mark.findpetbyid
def test_get_by_invalid_id():
    logger.info('Find a pet with invalid id: {0}'.format(constants.INVALID_ID))
    assert api_methods.get_pet_by_id(constants.INVALID_ID).status_code == constants.HTTP_NOT_FOUND
    # Based on Swagger documentation, this should be 400, not 404
