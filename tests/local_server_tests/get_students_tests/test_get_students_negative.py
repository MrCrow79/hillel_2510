import pytest



@pytest.mark.smoke
@pytest.mark.local_server
@pytest.mark.skip(reason='Jira issue #123')
@pytest.mark.parametrize('limit', ['11.5', False, [], 'asdasd'])  # TODO: find quantity of students and check +-1
def test_get_students_limit_negative(local_server_ctrl, limit):

    resp = local_server_ctrl.get_students(params={'limit': limit}).json()
    assert len(resp) == limit



