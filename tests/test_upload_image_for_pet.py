import pytest
import logging


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


@pytest.mark.uploadimage
def test_upload_valid_image_for_pet():
    pass


@pytest.mark.uploadimage
def test_upload_valid_image_for_nonexistent_pet():
    pass


@pytest.mark.uploadimage
def test_upload_invalid_file_type_for_pet():
    pass


@pytest.mark.uploadimage
def test_upload_valid_image_additional_metadata():
    pass


@pytest.mark.uploadimage
def test_upload_valid_image_invalid_metadata():
    pass



