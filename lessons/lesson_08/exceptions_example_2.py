user_data = {'u_id': 3, 'user_name': 'Alex'}

def test_check_user_data():
    expected_id = 1
    expected_name = 'Ivan'

    errors = []

    errors = _check_condition(expected_id, user_data['u_id'], errors)
    errors = _check_condition(expected_name,  user_data['user_name'], errors)

    assert not errors, f'we have next errors {errors}'


def _check_condition(expeced, actual, errors_list):
    try:
        assert expeced == actual
    except AssertionError:
        errors_list.append(f'Error {actual} == {expeced}')

    finally:
        return errors_list

# test_check_user_data()


def send_request(url, params):
    response = None
    # sending request
    response = {}

    if url == 'users/300':
        raise AssertionError(f'response is bad for {url}, {params}')

    return {'user_id': int(url.split(r"/")[-1])}



def test_users():

    for user_id in [1,2,5, 300]:

        try:
            user_data = send_request(f'users/{user_id}', {})
        except AssertionError:
            print(f'Users has no data for id={user_id}')
            continue

        assert user_data['user_id'] == user_id


test_users()