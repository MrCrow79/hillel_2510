import requests

from core.api_services.base_ctrl import BaseCtrl


class Swapi(BaseCtrl):

    def __init__(self, url='https://www.swapi.tech/api/'):
        self.url = url


    def get_user(self, user_id: int, expected_status_code=200):

        return self.send_request(url=f'{self.url}people/{user_id}', method='get',
                                 expected_status_code=expected_status_code)


    def get_users(self, parameters=None, expected_status_code=200):

        return self.send_request(url=f'{self.url}people/',  params=parameters, method='get',
                                 expected_status_code=expected_status_code)


    def get_planet(self, planet_id: int, expected_status_code=200):

        return self.send_request(url=f'{self.url}planets/{planet_id}', method='get',
                                 expected_status_code=expected_status_code)