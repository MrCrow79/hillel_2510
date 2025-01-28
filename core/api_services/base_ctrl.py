import requests
import curlify


class BaseCtrl:


    def send_request(self, method, url, params=None, headers=None, json=None, expected_status_code=None, schema=None):

        # getattr(requests, method) == requests.post  | requests.get
        response = getattr(requests, method)(url=url, params=params, headers=headers, json=json)

        print(f'curl:\n{curlify.to_curl(response.request)}')

        if expected_status_code:
            assert response.status_code == expected_status_code, \
                f'Status code is not {expected_status_code}, but {response.status_code}'

        if schema is not None:
            schema.load(response.json())

        return response


        # getattr(requests, method) --> requests.__getattr__(method)


# if __name__ == '__main__':
#     bc = BaseCtrl()
#
#     # r1 = bc.send_request(method='post', url='https://gorest.co.in/public/v2/users')
#     # r2 = getattr(bc, 'send_request')(method='post', url='https://gorest.co.in/public/v2/users')\
#
#     o1 = bc.send_request
#     o2 = getattr(bc, 'send_request')
#
#     # o1 == o2
#     # r1 == r2
#     print(o1 == o2)



        # if method.lower() == 'get':
        #
        #     response = requests.get(url=url, params=params, headers=headers)
        #
        #     print(f'curl:\n{curlify.to_curl(response.request)}')
        #
        #     if expected_status_code:
        #         assert response.status_code == expected_status_code, \
        #             f'Status code is not {expected_status_code}, but {response.status_code}'
        #
        #     return response
        #
        # if method.lower() == 'post':
        #
        #     response = requests.post(url=url, params=params, headers=headers, json=json)
        #
        #     print(f'curl:\n{curlify.to_curl(response.request)}')
        #
        #     if expected_status_code:
        #         assert response.status_code == expected_status_code, \
        #             f'Status code is not {expected_status_code}, but {response.status_code}'
        #
        #     return response


