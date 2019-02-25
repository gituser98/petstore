from utils import test_utils
from utils import api_methods
from utils import constants
import pytest
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


@pytest.mark.postpet
def test_add_new_valid_pet():
    generated_pet = test_utils.generate_pet()
    logger.info('Posting pet: {0}'.format(generated_pet))
    response = api_methods.post_pet(generated_pet)

    assert response.status_code == constants.HTTP_OK, "HTTP Status is not correct!"
    assert response.json() == generated_pet, "Response body doesn't match the expected object!"
    assert generated_pet == response.json()

    # Add database check to verify pet is created

    api_response = api_methods.get_pet_by_id(generated_pet['id'])
    assert generated_pet == api_response.json()
    assert api_response.status_code == constants.HTTP_OK


@pytest.mark.postpet
def test_add_new_valid_pet_id_0():
    generated_pet = test_utils.generate_pet()
    generated_pet['id'] = 0
    logger.info('Posting pet: {0}'.format(generated_pet))
    response = api_methods.post_pet(generated_pet)

    assert response.status_code == constants.HTTP_OK, "HTTP Status is not correct!"
    assert isinstance(response.json()['id'], int)
    assert test_utils.compare_dicts_ignore_keys(response.json(), generated_pet, {'id'}), \
        "Response body doesn't match the expected object! "


@pytest.mark.postpet
def test_add_new_valid_pet_negative_id():
    generated_pet = test_utils.generate_pet()
    generated_pet['id'] = -1
    logger.info('Posting pet: {0}'.format(generated_pet))
    response = api_methods.post_pet(generated_pet)

    assert response.status_code == constants.HTTP_OK, "HTTP Status is not correct!"
    assert response.json() == generated_pet, "Response body doesn't match the expected object!"


@pytest.mark.postpet
def test_add_new_invalid_pet_missing_field():
    generated_pet = test_utils.generate_pet_missing_field('name')
    logger.info('Posting pet with required missing field: \'name\' : {0}'.format(generated_pet))
    response = api_methods.post_pet(generated_pet)

    # Based on Swagger documentation, 'name' field is required (red *) so this should be 405
    assert response.status_code == constants.HTTP_OK


@pytest.mark.postpet
def test_add_new_invalid_pet_empty_body():
    empty_object = {}
    logger.info('Posting pet with empty body : {0}'.format(empty_object))
    response = api_methods.post_pet(empty_object)

    # Based on Swagger documentation, valid input is required so this should be 405
    assert response.status_code == constants.HTTP_OK
