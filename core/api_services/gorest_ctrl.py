import requests

from core.api_services.base_ctrl import BaseCtrl


class Gorest(BaseCtrl):

    headers = None

    def __init__(self, url='https://gorest.co.in/'):
        self.url = url


    def create_user(self, user_body, headers=None, expected_status_code=201):

        url = f'{self.url}public/v2/users'

        if not headers:  # якщо нема headers
            headers = dict()  # створю headers порожній словник

        headers.update(self._get_auth_headers())

        # Authorizaton: Bearer 180df87d1cd19c9a6220097af9834dc1bda7325bac5fb13ffe8a39d11f5dd49f
        return self.send_request(url=url, json=user_body, method='post', headers=headers,
                                 expected_status_code=expected_status_code)

    def get_user(self, user_id, expected_status_code=200):

        url = f'{self.url}public/v2/users/{user_id}'
        return self.send_request(url=url, method='get', expected_status_code=expected_status_code)


    @classmethod
    def _get_token(cls):
        #  тут може бути запит на ендпоінт автоирзації з логіном/паролем

        print('Getting new token')
        return 'Bearer 180df87d1cd19c9a6220097af9834dc1bda7325bac5fb13ffe8a39d11f5dd49f'

    @classmethod
    def _get_auth_headers(cls):
        if not cls.headers:
            cls.headers = dict()
            cls.headers['Authorization'] = cls._get_token()
        return cls.headers

# gorest_ctrl = Gorest()