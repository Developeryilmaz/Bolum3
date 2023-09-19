import requests
from pprint import pprint


def client():
    credentials = {
        'username': 'test11',
        'password1': 'Test@1234',
        'password2': 'Test@1234',
        'email': 'test11@gmail.com'
    }

    response = requests.post(
        url='http://127.0.0.1:8000/api/rest-auth/registration/',
        data=credentials,
    )

    print('Status Code:', response.status_code)

    response_data = response.json()
    pprint(response_data)


if __name__ == '__main__':
    client()
