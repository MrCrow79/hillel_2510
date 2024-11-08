user = [('id', 1), ('name', 'Ivan')]
users = dict(user)

print(users)

names = ['DEn', 'Alex', 'Ivan', 'Mor', 'Sofa']
ages = [20,30,50,20,10,55,44]

result = dict(zip(names, ages))
print(result)


# dict comprehension

len_of_names = {}
for name in names:
    len_of_names[name] = len(name)

print(len_of_names)

len_of_names_2 = {k: len(k) for k in names}
print(len_of_names_2)