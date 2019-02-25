from utils import test_utils
from utils import api_methods
from utils import constants
import pytest
import logging
import random

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


@pytest.mark.deletepet
def test_delete_by_id():
    pet_id = api_methods.post_pet(test_utils.generate_pet()).json()['id']
    logger.info('Posted pet with id: {0} for deletion'.format(pet_id))
    response = api_methods.get_pet_by_id(pet_id)

    assert response.status_code == constants.HTTP_OK
    logger.info('Deleting the pet with id: {0}'.format(pet_id))
    assert api_methods.delete_pet_by_id(pet_id).status_code == constants.HTTP_OK
    assert api_methods.get_pet_by_id(pet_id).status_code == constants.HTTP_NOT_FOUND


@pytest.mark.deletepet
def test_delete_by_nonexistent_id():
    pet_id = random.randint(900000000, 999999999)
    logger.info('Deleting a nonexistent pet with id: {0}'.format(pet_id))
    assert api_methods.delete_pet_by_id(pet_id).status_code == constants.HTTP_NOT_FOUND


@pytest.mark.deletepet
def test_delete_by_invalid_id():
    logger.info('Deleting a pet with invalid id: {0}'.format(constants.INVALID_ID))
    assert api_methods.delete_pet_by_id(constants.INVALID_ID).status_code == constants.HTTP_NOT_FOUND
    # Based on Swagger, this should return 400
