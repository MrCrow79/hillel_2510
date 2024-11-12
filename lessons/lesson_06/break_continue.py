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

for user in users:

    # case 1
    # if user['position'] == 'qa' and user['exp'] > 3:
    #     print('QA was found')
    #     print(user)
    #     break
    #
    # elif user['position'] == 'qa' and user['exp'] <= 3:
    #     print('Maybe QA was found')
    #     print(user)


    # case 2 == case 1
    # if user['position'] == 'qa':
    #     if user['exp'] > 3:
    #         print('QA was found')
    #         print(user)
    #         break
    #     else:
    #         print('Maybe QA was found')
    #         print(user)


    # case 3
    # if user['position'] != 'qa':
    #     continue # перейти до наступної ітерації цикла for

    # if user['exp'] < 3:  # 0- 2
    #     continue
    # elif user['exp'] < 6: # 3 - 6
    #     print('Maybe QA was found')
    #     print(user)
    # else:  # 7+
    #     print('QA was found')
    #     print(user)
    #     break

    # case 4 == case 3
    if user['position'] != 'qa':
        continue # перейти до наступної ітерації цикла for
    if user['exp'] >= 6 :  # 7+
        print('QA was found')
        print(user)
        break

    elif user['exp'] >= 3: # 3-6
        print('Maybe QA was found')
        print(user)




# for user in users:
#
#     print(user['name'])
#
#     if user['id'] > 2:
#         for _ in range(user['exp']):
#             print(f"{user['name']} has {user['exp']} year of profession life")
#
#     if user['id'] == 3:
#         break
#
#     print('-'*80)

print('Done')