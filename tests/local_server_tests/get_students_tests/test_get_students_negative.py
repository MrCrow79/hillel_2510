from core.api_services.local_server_ctrl import LocalServer
import pytest


@pytest.mark.local_server
def test_get_default_student_negative(local_server_ctrl):  # local_server_ctrl результат виконання функції з tests/local_server_tests/conftest.py

    default_student_id = 10050  # str, None
    resp = local_server_ctrl.get_student(student_id=default_student_id, expected_status_code=500)