import random
import string
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.WARNING)


def generate_pet():

    random_id = random.randint(900000, 999999)
    random_int = random.randint(100, 200)
    random_string = ''.join(random.choice(string.ascii_uppercase) for _ in range(5))

    random_pet = {
        "id": random_id,
        "category": {
            "id": random_int,
            "name": "category_name_" + random_string
        },
        "name": "name_" + random_string,
        "photoUrls": [
            "photo_url1_" + random_string,
            "photo_url2_" + random_string
        ],
        "tags": [
            {
                "id": random_int,
                "name": "tags_name_" + random_string
            }
        ],
        "status": "status_" + random_string
    }

    return random_pet


def generate_pet_missing_field(field_to_be_removed):
    pet = generate_pet()
    del pet[field_to_be_removed]
    return pet


def compare_dicts_ignore_keys(dict1, dict2, ignore_keys):
    keys_dict1 = set(dict1).difference(ignore_keys)
    keys_dict2 = set(dict2).difference(ignore_keys)
    return keys_dict1 == keys_dict2 and all(dict1[k] == dict2[k] for k in keys_dict1)
