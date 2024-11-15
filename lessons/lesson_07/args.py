def filter_dict(*args, key_for_filtering: str = 'name', values_for_filtering='Ivan') -> list:

    result_list = []

    for dct in args:

        if key_for_filtering in dct:
            if dct[key_for_filtering] == values_for_filtering:
                result_list.append(dct)

    return result_list

print(filter_dict(
    {'id': 1, 'name': 'Ivan'}, {'id': 3, 'name': 'Ivan'}, {'id': 2, 'name': 'Sofa'}, {'id': 4, 'name': 'Den'}
))

