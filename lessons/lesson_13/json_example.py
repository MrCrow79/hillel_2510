import json

# users = [
#     {'id':1, 'name': 'Denys', 'score': 75.5, 'is_qa': True, 'company': None},
#     {'id':2, 'name': 'Alex', 'score': 75.5, 'is_qa': False, 'company': {'id': 2, 'name': "FB"}},
# ]

# print(users)  # str(users)
# json_users = json.dumps(users, indent=4)  # -> str
# print(json_users)

# with open('users.json', 'w') as f:
#     f.write(json_users)

# with open('users.json', 'w') as f:
#     json.dump(users, indent=4, fp=f)

with open('users.json') as f:
    print(json.load(f)[1])


#     data = f.read()
#
# users = json.loads(data)
# print(type(data))
# print(type(users))
# print(users[0])