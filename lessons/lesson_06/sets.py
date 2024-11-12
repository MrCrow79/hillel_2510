#

names = {'Den', 'Ivan', 'Den'}

# for name in names:
#     print(name)
#
# print(hash('Den'))
# print(hash('Den'))
# print(hash('Ivan'))
#
# lst = [1,2]
#
# print(id(lst))
# lst.append(3)
# print(lst)
# hash(lst)
# print(id(lst))



# create
names = {'Den', 'Ivan', 'Den'}
list_of_ages = [20, 50, 45, 50]

set_of_ages = set(list_of_ages)

# print(set_of_ages)

set_compr = {k**2 for k in list_of_ages}

# print(set_compr)

# update
set_compr.update([1,2])
set_compr.update(set_of_ages)

set_compr.add(888)
# print(set_compr)

# print(set_compr)

# delete
# el = set_compr.pop()  # видаляє випадковий елемент

# print(el)
# print(set_compr)

set_compr.remove(2025)
print(set_compr)

# logic operator

print(2 in set_compr)  # return bool value
print(2025 in set_compr)  # return bool value

response = [
    {'id': 1, 'name ': 'Ivan'},
    {'id': 2, 'name ': 'Ivan'},
    {'id': 3, 'name ': 'Ivan'},
    {'id': 4, 'name ': 'Ivan'},
    {'id': 5, 'name ': 'Ivan'},
    {'id': 6, 'name ': 'Ivan'},
    {'id': 6, 'name ': 'Ivan'},
]

# user_ids = [user['id'] for user in response] - list comprehension

user_ids = []

for user in response:
    user_ids.append(user['id'])

user_ids_set = set(user_ids)
print(user_ids)

result = len(response) == len(user_ids_set)  # чи є дублікати
print(result)