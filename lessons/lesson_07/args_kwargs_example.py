def filter_dicts(base_dict, *args, print_info=False, **kwargs) -> list:

    result_list = []

    full_list = [base_dict, *args]  # args це tuple, kwargs це словник

    if not kwargs:  # якщо порожній словник kwargs
        if print_info:
            for user in full_list:
                print(user, end='\n-------------')
        return full_list

    for dct in full_list:

        is_need_to_add = True
        for key, value in  kwargs.items():

            if key not in dct:
                is_need_to_add = False
                break
            else:
                if dct[key] != value:
                    is_need_to_add = False
                    break
        if is_need_to_add:
            result_list.append(dct)

    if print_info:
        for user in result_list:
            print(user, end='\n-------------\n')

    return result_list

# отримати людей ікі працють нe на першій роботі
filter_dicts(
    {'id': 1, 'name': "Alex", 'has_a_job': True, 'is_first_job': True},
    {'id': 2, 'name': "Den", 'has_a_job': False},
    {'id': 3, 'name': "Sofa", 'has_a_job': True, 'is_first_job': False},
    {'id': 4, 'name': "Ivan", 'has_a_job': False},
    {'id': 5, 'name': "Mor", 'has_a_job': True, 'is_first_job': False},
    has_a_job=True, is_first_job=False, print_info=True
)




