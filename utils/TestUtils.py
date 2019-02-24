import random
import string


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
