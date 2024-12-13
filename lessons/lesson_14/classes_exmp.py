
# my_list = [1,23]
#
# user = {
#     "id": 1,
#     "name": 'Ivan',
#     'age': 55
# }
#
# users = [user, user, user]  #  response з api
#
# if not isinstance(users, list):
#     assert ...
#
# for user in users:

class Dog:

    def make_noize(self):
        print('Rrrrr...')

class Spaniel(Dog):
    pass

my_dog = Dog()
my_span = Spaniel()

my_span.make_noize()
my_list = [1,23]

my_dog.make_noize()
my_list.append(5)