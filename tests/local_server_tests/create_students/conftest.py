import pytest


@pytest.fixture(scope='session')
def body_user_with_max_score():
    return {"name": "Alex", "score": 50}