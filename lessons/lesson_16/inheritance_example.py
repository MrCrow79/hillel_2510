

class Endpoint:

    get_user = '/user/{user_id}'
    get_user_details = '/user/{user_id}/details'


class RequestExecutor:


    def __init__(self, base_url='127.0.0.0'):
        self.base_url = base_url


    def send_request(self, url, **kwargs):


        print(f'Sending request to {url} with parameters: {kwargs}')

# поганий варіант
# class UserCtrl(RequestExecutor, Endpoint):
#
#     def get_user_data(self, user_id):
#
#         url = f'{self.base_url}{self.get_user.format(user_id=user_id)}'
#
#         self.send_request(url=url, user_id=user_id)


# Варіант 1
class UserCtrl():


    def __init__(self, base_url=None):

        if base_url:
            self.executor = RequestExecutor(base_url)
        else:
            self.executor = RequestExecutor()

    def get_user_data(self, user_id):

        url = f'{self.executor.base_url}{Endpoint.get_user.format(user_id=user_id)}'

        self.executor.send_request(url=url, user_id=user_id)

# UserCtrl().get_user_data(8)