import json

import requests


def get_default_header():
    headers = {'content-type': 'application/json'}
    return headers


def validate_and_get_user(auth_token):
    url = "http://0.0.0.0:8090/validate"
    data = {"authToken": auth_token}
    headers = get_default_header()

    response = requests.post(url=url, data=json.dumps(data), headers=headers)

    if response.status_code != 200:
        return False, None

    return True, json.loads(response.content)
