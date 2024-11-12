users = [
    {
        'id': 1,
        'name': 'den',
        'position': 'aqa',
        'exp': 4
    },
    {
        'id': 2,
        'name': 'alex',
        'position': 'qa',
        'exp': 7
    },
    {
        'id': 3,
        'name': 'mor',
        'position': 'pm',
        'exp': 2
    },
    {
        'id': 4,
        'name': 'Sofa',
        'position': 'qa',
        'exp': 3
    },

]

# for user in users:
#
#     print(user['name'])
#
#     if user['id'] > 2:
#         for _ in range(user['exp']):
#             print(f"{user['name']} has {user['exp']} year of profession life")
#
#     print('-'*80)



for user in users:

    print(user['name'])

    if user['id'] > 2:
        for _ in range(user['exp']):
            print(f"{user['name']} has {user['exp']} year of profession life")

    print('-'*80)

# for number in range(10):  # for number in (0,1,2,3,4,5,6,7,8,9)
#     print(number)

# for number in range(5, 10):  # for number in (5,6,7,8,9)
#     print(number)