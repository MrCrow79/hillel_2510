import pytest

@pytest.fixture
def connect_to_db():
    print('connecting to db...')
    db_connector = 'This_is_db_Connector'
    yield db_connector
    print("closing connection ...")


def test_example(connect_to_db):  # використання фікстур

    print(connect_to_db)
    assert 1==1