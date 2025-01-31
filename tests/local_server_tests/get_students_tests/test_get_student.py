import pytest
import setting



@pytest.mark.smoke
@pytest.mark.local_server
def test_get_default_student(local_server_ctrl):

    default_student_id = 630
    resp = local_server_ctrl.get_student(student_id=default_student_id).json()
    print(resp)
    assert len(resp) > 0
    assert resp['id'] == default_student_id



@pytest.mark.local_server
# @pytest.mark.parametrize('student', [....])
# @pytest.mark.usefixtures(f'read_data_on_{setting.d_settings.current_env}')
def test_get_student(local_server_ctrl, last_n_students_parametrized, read_data_depend_on_env):

    resp = local_server_ctrl.get_student(student_id=last_n_students_parametrized['id']).json()
    print(resp)
    assert resp == last_n_students_parametrized
