import requests

from core.api_services.base_ctrl import BaseCtrl
from core.api_services.local_server.schemas import BaseUserSchema


class LocalServer(BaseCtrl):

    def __init__(self, url='http://127.0.0.1:8080/'):
        self.url = url


    def get_student(self, student_id: int, expected_status_code=200, is_need_schema_validation=True):

        if is_need_schema_validation:
            schema = BaseUserSchema()
        else:
            schema = None

        return self.send_request(url=f'{self.url}students/{student_id}', method='get',
                                 expected_status_code=expected_status_code, schema=schema)

    def get_students(self,  params: dict = None, expected_status_code=200, is_need_schema_validation=True):

        if is_need_schema_validation:
            schema = BaseUserSchema(many=True)
        else:
            schema=None

        return self.send_request(url=f'{self.url}students/', method='get',
                                 expected_status_code=expected_status_code, schema=schema, params=params)


    def create_student(self, json: dict, auth_data: str, expected_status_code=201, is_need_schema_validation=True):

        if is_need_schema_validation:
            schema = BaseUserSchema()
        else:
            schema=None

        return self.send_request(url=f'{self.url}students/', method='post', json=json,
                                 headers={'token': auth_data},
                                 expected_status_code=expected_status_code, schema=schema)


    def delete_user(self, student_id: int, auth_data: str, expected_status_code=204):

        return self.send_request(url=f'{self.url}students/{student_id}', method='delete',
                                 headers={'token': auth_data},
                                 expected_status_code=expected_status_code)


    def auth(self, json,  expected_status_code=200):

        return self.send_request(url=f'{self.url}auth/', method='post', json=json,
                                 expected_status_code=expected_status_code)
