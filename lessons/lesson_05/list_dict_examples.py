users = [
    {'id': 1, 'name': 'alex' },
    {'id': 2, 'name': 'Den' },
    {'id': 4, 'name': 'Ivan' },
    {'id': 3, 'name': 'Sofa' },
]

# 1) створити список тільки з id
list_of_users_ids = [item['id'] for item in users]  # [1,2,4,3]

# is_sorted = list_of_users_ids.sort()  # is_sorted  буде None
# 2) перевірити чи відсортований  list_of_users_ids
print(list_of_users_ids)
print(sorted(list_of_users_ids))
print(list_of_users_ids == sorted(list_of_users_ids))