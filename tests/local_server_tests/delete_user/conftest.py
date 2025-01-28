from faker import Faker
import random
from pytest import fixture

faker = Faker()


@fixture
def get_new_random_user_for_deleting(local_server_ctrl, auth_header):
    return local_server_ctrl.create_student(json={"name": faker.name(), "score": random.choice(range(1, 101))},
                                            auth_data=auth_header).json()

@fixture(scope='session')
def get_new_random_user(local_server_ctrl, auth_header):

    print('fixture get_new_random_user creating')

    st = local_server_ctrl.create_student(json={"name": faker.name(), "score": random.choice(range(1, 101))},
                                            auth_data=auth_header).json()

    yield st

    print('fixture get_new_random_user deleting')

    local_server_ctrl.delete_user(student_id=st['id'], auth_data=auth_header)