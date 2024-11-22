def assert_user(actual_user, user_id, user_name, user_companies_len):
    error = []

    assert actual_user, 'user data is empty!'  # actual user is not empty

    # нема сенсу перевіряти далі, якщо user_id невірний, тобто це інший юзер
    assert actual_user['id'] == user_id, f'user_id: expected {user_id}, but got {actual_user["id"]}'

    if actual_user['name'] != user_name:
        error.append(f'user_name: Expected {user_name}, but got {actual_user["name"]}')

    if len(actual_user["companies"]) != user_companies_len:
        error.append(f'len of companies: Expected {len(actual_user["companies"])}, but got {user_companies_len}')

    assert not error, '\n'.join(error)  # not errors == not bool(error)