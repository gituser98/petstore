from utils import test_utils
from utils import api_methods
from utils import constants
import pytest
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


@pytest.mark.updatepet
def test_update_pet():
    generated_pet = test_utils.generate_pet()
    pet_id = generated_pet['id']
    logger.info('POST pet: {0}'.format(generated_pet))
    response = api_methods.post_pet(generated_pet)

    test_utils.verify_pet_from_api(generated_pet, response)

    # Add database check to verify pet is created

    api_response = api_methods.get_pet_by_id(pet_id)
    assert api_response.status_code == constants.HTTP_OK
    assert generated_pet == api_response.json()

    # Generate a new pet and set the id to the id from original pet
    updated_generated_pet = test_utils.generate_pet()
    updated_generated_pet['id'] = pet_id
    logger.info('PUT updated pet with same id: {0} and new values: {1}'.format(pet_id, updated_generated_pet))
    updated_response = api_methods.put_pet(updated_generated_pet)

    test_utils.verify_pet_from_api(updated_generated_pet, updated_response)

    # Add database check to verify pet is updated

    updated_api_response = api_methods.get_pet_by_id(pet_id)

    test_utils.verify_pet_from_api(updated_generated_pet, updated_api_response)


@pytest.mark.updatepet
def test_update_pet_invalid_body():
    generated_pet = test_utils.generate_pet()
    pet_id = generated_pet['id']
    logger.info('POST pet: {0}'.format(generated_pet))
    response = api_methods.post_pet(generated_pet)

    test_utils.verify_pet_from_api(generated_pet, response)

    # Add database check to verify pet is created

    api_response = api_methods.get_pet_by_id(pet_id)
    test_utils.verify_pet_from_api(generated_pet, api_response)

    # Generate a new pet with required missing field and set the id to the id from original pet
    updated_generated_pet = test_utils.generate_pet_missing_field('name')
    updated_generated_pet['id'] = pet_id
    logger.info('PUT updated pet with same id: {0} and new values: {1} (missing \'name\')'.
                format(pet_id, updated_generated_pet))
    updated_response = api_methods.put_pet(updated_generated_pet)

    # Based on Swagger documentation, 'name' field is required (red *) so this should be 405
    test_utils.verify_pet_from_api(updated_generated_pet, updated_response)

    # Add database check to verify pet is updated

    updated_api_response = api_methods.get_pet_by_id(pet_id)
    test_utils.verify_pet_from_api(updated_generated_pet, updated_api_response);


@pytest.mark.updatepet
def test_update_pet_invalid_id():
    # should return 400
    pass


@pytest.mark.updatepet
def test_update_pet_nonexistent_id():
    # should return 404
    pass


