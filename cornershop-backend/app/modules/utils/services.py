import random
import string
from uuid import UUID


def get_url(url: str):
    """
        Method get url from pagination

        :param url: url of next or previous
        :type url: str
        :return: url
    """
    count = 0
    position = 0
    # capture position of chart /
    for i, chart in enumerate(url):
        if "/" == chart:
            position = i
            count = count + 1
        if count > 2:
            break
    # get temporal url
    temporal_url = url[position:]
    return temporal_url


def code_generator(size=10, chars=string.ascii_lowercase + string.digits):
    """
       this method generates a string randomly

       :param size: size of string.
       :type size: integer.
       :param chars: sting with number and characters
       :type chars: str.
       :return: random string.
    """
    return ''.join(random.choice(chars) for _ in range(size))


def is_valid_uuid(uuid_value: str, version=4) -> bool:
    """
         Check if uuid_value is a valid UUID.

        :param uuid_value:
        :type uuid_value: str
        :param version: version of uuid
        :type version: int
        :return: True is uuid are correct
        :return: false is uuid are incorrect
    """
    try:
        uuid_obj = UUID(uuid_value, version=version)
    except ValueError as e:
        print(f"The value is not a uuid {e}")
        return False
    return str(uuid_obj) == uuid_value
