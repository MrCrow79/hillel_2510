user = {
    'id': 4,
    'name': 'Sofa',
    'position': 'qa',
    'exp': 3,
    'tools': []
}

users = [
    {
        'id': 4,
        'name': 'Sofa',
        'position': 'qa',
        'exp': 2,
        'tools': ['dev tools']
    },
    {
        'id': 5,
        'name': 'Den',
        'position': 'qa',
        'exp': 4,
        'tools': ['dev tools', 'postman']
    },
    {
        'id': 6,
        'name': 'Ivan',
        'position': 'qa',
        'exp': 7,
        'tools': ['postman', 'pqsql']
    },
]

# for data in user:  #  по ключах
#     print(data)
#
# for data in user.keys():  #  по ключах
#     print(data)

# for data in user.values():  # по значеннях
#     print(data)

# for data in user.items(): # по таплах (ключ, значення)  можу ходити по [(id, 4), (name, Sofa)]
#     print(data)

for user in users:

    user_data = list(user.values())  # user.keys(), user.items()

    # user_data має id, name, position, exp, tools
    # name = user_data[1]
    # user_id = user_data[0]
    # tools = user_data[-1]

    # id, name, position, exp, tools = user_data

    user_id, name, position,exp, tools =  user_data

    print('-'*80)
    print(f"Checking info for {user_id}: {name}")
    # print(*_)
    # print(tools)

    if exp < 5:
        continue
    print(f'Worked with {", ".join(tools)}')

    if 'postman' in tools:
        print('You are hired')
        break


