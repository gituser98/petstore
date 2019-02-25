from utils import api_methods
from utils import constants
import pytest
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


AVAILABILITY_STATUS = 'sold'
STATUS_THAT_DOESNT_EXIST = 'this_status_doesnt_exist'


@pytest.mark.findpetbystatus
@pytest.mark.skip(reason="Disabled because size keeps changing frequently and we don't have DB access")
def test_get_by_status():
    logger.info('Getting pets with status: {0}'.format(AVAILABILITY_STATUS))
    response = api_methods.get_pet_by_status(AVAILABILITY_STATUS)
    assert response.status_code == constants.HTTP_OK

    list_of_pets = response.json()
    # Should be tested by getting the objects (where status='sold') from the database.
    # Then compare the size of the list and objects (database vs api response)
    assert len(list_of_pets) == 109

    # Another approach would be creating some number of items in database with unique status and query api with that
    # status. We can verify the number of items and each expected item.


@pytest.mark.findpetbystatus
def test_get_by_invalid_status():
    logger.info('Getting pets with status: {0}'.format(STATUS_THAT_DOESNT_EXIST))
    # Based on Swagger, this should return 400 but it returns an empty array with status 200
    response = api_methods.get_pet_by_status(STATUS_THAT_DOESNT_EXIST)
    assert response.status_code == constants.HTTP_OK
    list_of_pets = response.json()
    assert len(list_of_pets) == 0
