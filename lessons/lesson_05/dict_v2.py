user = {
    'id': 1,
    'name': 'Yuri',
    'position': 'JS dev',
    ('name', 'position'): 'Y, JS',
    'friends': [
        {
            'id': 3,
            'name': 'Alex'
        },
        {
            'id': 4,
            'name': 'Ivan'
        },
    ]
}

print(user)
# user.clear()  # очистка вже існуючого
# user = {}  # новий об'єкт
# print(user)

# user_2 = user.copy()
# print(user_2)
#
# print(id(user['friends']))
# print(id(user_2['friends']))
# user['friends'].append({'id': 5, 'name': 'Mor'})
#
# # print(user_2)
#
name_of_user = user.pop('name')
name_of_user = user.popitem()
# print(user)
# print(name_of_user)

# update dict

user['city'] = 'Kharkiv'
print(user)
user['position'] = 'Manager'
print(user)

partical_info =  {'country': 'Ukraine', 'phone_number': 38096}

user.update(partical_info)
print(user)

user.setdefault('country', 'GB')
user.setdefault('phone_2', 38063)
print(user)
