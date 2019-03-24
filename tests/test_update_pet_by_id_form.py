from utils import test_utils
from utils import api_methods
from utils import constants
import pytest
import logging
import copy

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


@pytest.mark.updatepetwithid
def test_update_pet():
    generated_pet = test_utils.generate_pet()
    pet_id = generated_pet['id']
    logger.info('POST pet: {0}'.format(generated_pet))
    response = api_methods.post_pet(generated_pet)

    test_utils.verify_pet_from_api(generated_pet, response)

    # Add database check to verify pet is created

    api_response = api_methods.get_pet_by_id(pet_id)
    test_utils.verify_pet_from_api(generated_pet, api_response)

    # Update pet with form
    api_methods.post_pet_by_id(pet_id, "new_name", "new_status")

    # Add database check to verify pet is updated

    updated_api_response = api_methods.get_pet_by_id(pet_id)

    updated_expected_object = copy.deepcopy(generated_pet)
    updated_expected_object['name'] = "new_name"
    updated_expected_object['status'] = "new_status"

    test_utils.verify_pet_from_api(updated_expected_object, updated_api_response)


@pytest.mark.updatepetwithid
def test_update_pet_id_name_only():
    # Should return 200
    pass


@pytest.mark.updatepetwithid
def test_update_pet_id_status_only():
    # Should return 200
    pass


@pytest.mark.updatepetwithid
def test_update_pet_nonexistent_id():
    # Should return 404
    pass


@pytest.mark.updatepetwithid
def test_update_pet_invalid_id():
    # Should return 405
    pass


@pytest.mark.updatepetwithid
def test_update_pet_invalid_name():
    # Should return 405
    pass


@pytest.mark.updatepetwithid
def test_update_pet_invalid_status():
    # Should return 405
    pass
