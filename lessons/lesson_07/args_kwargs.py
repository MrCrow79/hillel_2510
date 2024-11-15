def filter_dict(base_dict, *args, key_for_filtering: str = 'name', values_for_filtering='Ivan') -> list:

    result_list = []

    start_list = [base_dict, *args]

    for dct in start_list:

        if key_for_filtering in dct:
            if dct[key_for_filtering] == values_for_filtering:
                result_list.append(dct)

    return result_list


def print_user_info(full_info=False, **kwargs):
    if full_info:
        for key, value in kwargs.items():
            print(f'{key} = {value}')
    else:
        print(f'name = {kwargs.get("name")}')

    if kwargs.get('lsit_of_positions'):
        print('also user have next positions in his list', kwargs.get("lsit_of_positions"))
    print('-'*80)


filtered_users = filter_dict(
    {'id': 1, 'name': 'Ivan', 'age': 30}, {'id': 3, 'name': 'Ivan'}, {'id': 2, 'name': 'Sofa'}, {'id': 4, 'name': 'Den'}
)

print_user_info(user_id=17, user_name='Den', age=88, lsit_of_positions=['QA', 'AQA'], full_info=True)


for user in filtered_users:
    print_user_info(**user, full_info=True)

