
user = {
    'id': 1,
    'name': 'Den',
    'position': 'aqa'
}

# if bool:

if user['name'] == 'Den':  # if true - continue
    print('You are den')

if user['name'] == 'Alex':  # if false - do nothing
    print('You are Alex')

if user['id'] == 2:
    print('Never be printed')

elif user['position'] == 'aqa1':
    print('You are aqa1')

elif user['id'] == 1:
    print('You have id 1')

else:
    print('Will be executed if all `if` and `elif` are not executed')

print('Done')


if user['id'] == 1 and user['name'] == 'Alex':  # True and False => False
    print('Never be printed')
elif (user['id'] == 1 or user['name'] == 'Alex') and True:  # True or False => True
    print('You are Alex or have id = 1')

# True and True = True
# True and False = False
# True or False = True
# False or False = False