import random
from faker import Faker


# list_of_friends = ['Den', 'Alex', 'Ivan']
# row_of_smth = 'Allice was ....'
#
# for el in row_of_smth:
#     print(el)
#
# print('-------------')
#
# try:
#     iterth = iter(row_of_smth)  # get iterator
#     while True:
#         print(next(iterth))  # get next element
# except StopIteration:
#     pass



class MyIterator:

    list_of_greetings = [
        'Hello',
        'Hi',
        'Nice to meet you',
    ]

    def __init__(self, *args):
        self._list_of_names = args
        self.current_position = 0


    def __iter__(self):
        return self

    def __next__(self):

        if self.current_position == len(self._list_of_names):
            raise StopIteration

        current_greetings = random.choice(self.list_of_greetings)
        current_name = self._list_of_names[self.current_position]
        self.current_position += 1

        return f'{current_greetings} {current_name}'


# for name in MyIterator('Den', 'Ivan', 'Sofia'):  # зробить _ = iter(MyIterator('Den', 'Ivan', 'Sofia')), name = next(_)
#     print(name)



class UserDataGetter:

    _faker = Faker()


    def __init__(self, quantity_of_users):
        self.quantity_of_users = quantity_of_users
        self.current_user_counter = 0


    def __iter__(self):
        return self

    def __next__(self):

        if self.current_user_counter == self.quantity_of_users:
            raise StopIteration

        # ось цю частину можна замінити на запити до сервера з рандомним id
        user_data = {
            "id": self.current_user_counter + 1,
            "name": self._faker.name(),
            "age": random.choice(range(18, 66))  #  від 18 до 65
        }
        self.current_user_counter += 1 # збільшення на 1

        return user_data


for user in UserDataGetter(5): # for _ in range(5)

    print(f'{user["id"]}, {user["name"]}')