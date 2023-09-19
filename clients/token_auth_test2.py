import requests
from pprint import pprint


def client():
    token = 'Token 1922704172c4c432dff919aa8702c5ece1ef1433'

    headers = {
        'Authorization': token
    }

    response = requests.get(
        url='http://127.0.0.1:8000/api/user-profiles/',
        headers=headers
    )

    print('Status Code:', response.status_code)

    response_data = response.json()
    pprint(response_data)


if __name__ == '__main__':
    client()
