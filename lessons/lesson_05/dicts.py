# user = {
#     'id': 1,
#     'name': 'Yuri',
#     'position': 'JS dev'
# }

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
# get values, keys

user_position = user['position']  # небезпечний, може призвети до KeyError
# print(user_position)

user_name_error = user.get('name1', 'unknown name')  # дістати значення по ключу. або 'unknown name', None de default
user_name = user.get('name', 'unknown name')  # дістати значення по ключу. або 'unknown name'
# print(user_name_error)
# print(user_name)


all_keys = list(user.keys())
all_values = list(user.values())
all_items = list(user.items())

print(all_keys)
print(all_values)
print(all_items)

for key in user.keys():
    print(key)

for value in user.values():
    print(value)

for key, value in user.items():
    print(f'A key is {key} with values {value}')