import pytest
from copy import deepcopy

from tests.local_server_tests.get_students_tests.conftest import DEFAULT_USERS_LIMIT


@pytest.mark.smoke
@pytest.mark.local_server
@pytest.mark.parametrize('params', [{}, {'limit': None}], ids=['without limit', 'limit is None'])
def test_get_students_default_limit(local_server_ctrl, params):

    resp = local_server_ctrl.get_students(params=params).json()
    assert len(resp) ==  DEFAULT_USERS_LIMIT


@pytest.mark.smoke
@pytest.mark.local_server
@pytest.mark.parametrize('limit', [1, 5, 10, 100, 500])  # TODO: find quantity of students and check +-1
def test_get_students_limit(local_server_ctrl, limit):

    resp = local_server_ctrl.get_students(params={'limit': limit}).json()
    assert len(resp) == limit


@pytest.mark.smoke
@pytest.mark.local_server
@pytest.mark.parametrize('limit_related_to_students', [-1,0])
def test_get_students_limit_of_students(local_server_ctrl, get_quantity_of_users, limit_related_to_students):

    limit = get_quantity_of_users + limit_related_to_students

    resp = local_server_ctrl.get_students(params={'limit': limit}).json()
    assert len(resp) == limit


@pytest.mark.smoke
@pytest.mark.local_server
@pytest.mark.parametrize('limit_related_to_students', [1, 10, 55, 100500])
def test_get_students_more_than_limit_of_students(local_server_ctrl, get_quantity_of_users, limit_related_to_students):


    resp = local_server_ctrl.get_students(params={'limit': get_quantity_of_users + limit_related_to_students}).json()
    assert len(resp) == get_quantity_of_users


@pytest.mark.smoke
@pytest.mark.local_server
@pytest.mark.parametrize('sort_by', ['id', '-id', 'name', '-name', 'created_date'])
def test_get_students_sort_by(local_server_ctrl, sort_by):

    resp = local_server_ctrl.get_students(params={'sort_by': sort_by}).json()
    assert len(resp) > 0

    sorted_list = deepcopy(resp)
    reverse_parameter = False

    if sort_by.startswith('-'):
        sort_by = sort_by[1:]
        reverse_parameter=True

    sorted_list.sort(key=lambda x:x[sort_by], reverse=reverse_parameter)

    assert  sorted_list == resp





