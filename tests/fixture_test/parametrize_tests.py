import pytest


@pytest.mark.parametrize('page_size', [1, 10, 50, 100])
@pytest.mark.parametrize('page', [1, 5, 7, 300])
@pytest.mark.parametrize('user_age', [18, 19, 30, 57, 64, 65])
def test_example(page_size, page, user_age):

        print(f"sending_request to get /users?page_size={page_size}&page={page}&user_age_gte={user_age}")
