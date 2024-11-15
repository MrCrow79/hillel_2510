# lambda_name = lambda l_argument: l_argument > 5


def lambda_name(l_argument):
    return l_argument > 5

def get_id_of_dict(dct: dict):
    return dct['id']

users = [{'id': 888, 'name': "Den", 'has_a_job': False},
         {'id': 14, 'name': "Sofa", 'has_a_job': True, 'is_first_job': False},
         {'id': 55, 'name': "Ivan", 'has_a_job': False},
         {'id': 6, 'name': "Mor", 'has_a_job': True, 'is_first_job': False}]


users2 = [{'id': 888, 'name': "Den", 'has_a_job': False},
         {'id': 14, 'name': "Sofa", 'has_a_job': True, 'is_first_job': False},
         {'id': 55, 'name': "Ivan", 'has_a_job': False},
         {'id': 6, 'name': "Mor", 'has_a_job': True, 'is_first_job': False}]

# відсортувати цих юзеріd по id
users.sort(key=lambda x: x['id'], reverse=False) # reverse=False по замовчуванню, від 0 до 100
users2.sort(key=get_id_of_dict, reverse=True) # від 100 до 0
print(users)
print(users2)
