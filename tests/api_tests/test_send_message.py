import pytest
import requests
import logging
import json

host = '127.0.0.1'
port = 7071

BASE_URL = f'http://{host}:{port}/content'

def get_content():
    return requests.get(BASE_URL).json()  # поверне dict {'content': []}
    # return json.loads(requests.get(BASE_URL).text())  # поверне dict {'content': []}

def get_content_ids() -> list[int]:
    all_content = get_content()
    logging.info(f'content is {str(all_content)}')
    len_of_content = len(all_content['content'])

    ids = list(range(len_of_content))

    return ids

@pytest.mark.parametrize('data_to_send', [
    'Den',
    1,
    [1,2,3],
    True,
    [{1:2}]
])
def test_send_content(data_to_send):

    requests.post(BASE_URL, json=data_to_send)  # поверне dict {'content': []}


    assert get_content()['content'][-1] == data_to_send


def test_get_all_content():

    response = requests.get(BASE_URL)  # поверне dict {'content': []}


    assert  response.status_code == 200  # повернулась валідна відповідь


@pytest.mark.parametrize('content_id', get_content_ids())
def test_get_content_by_id(content_id):

    response = requests.get(f'{BASE_URL}/{content_id}')

    assert response.status_code == 200