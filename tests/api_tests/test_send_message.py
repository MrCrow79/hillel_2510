import pytest
import requests

host = '127.0.0.1'
port = 7070

def get_content():
    return requests.get(f'http://127.0.0.1:7070/content').json()  # поверне dict {'content': []}


@pytest.mark.parametrize('data_to_send', [
    'Den',
    1,
    [1,2,3],
    True,
    [{1:2}]
])
def test_send_content(data_to_send):

    requests.post(f'http://127.0.0.1:7070/content', json=data_to_send)  # поверне dict {'content': []}

    assert get_content()['content'][-1] == data_to_send