import pytest


@pytest.mark.smoke
@pytest.mark.local_server
def test_get_students(local_server_ctrl):

    resp = local_server_ctrl.get_students().json()
    print(resp)
    assert len(resp) > 0


@pytest.mark.smoke
@pytest.mark.local_server
def test_get_default_student(local_server_ctrl):

    default_student_id = 630
    resp = local_server_ctrl.get_student(student_id=default_student_id).json()
    print(resp)
    assert len(resp) > 0
    assert resp['id'] == default_student_id