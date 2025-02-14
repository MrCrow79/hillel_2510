import random

from faker import Faker

faker = Faker()


def print_user_data(user_name, user_pwd):
    print(f'{user_name} {user_pwd}')


# print_user_data('Den', 'Mer')


class UserData:

    def __init__(self, user_name=None, age=None):
        self.user_name = user_name
        self.age = age

    def with_random_name(self):
        self.user_name = faker.name()
        return self

    def with_random_age(self):
        self.age = random.choice(range(18, 66))
        return self

    def with_negative_age(self):
        self.age = random.choice(range(-200, -100))
        return self

    def __str__(self):
        return f"{self.user_name}, {self.age}"

    me = ('Den', 'Mer')


user = UserData().with_random_name().with_random_age()
user2 = UserData().with_random_name().with_negative_age()
user3 = UserData().with_random_name()

print(user)
print(user2)
print(user3)

# data_me_tuple = UserData.me
#
#
# print_user_data(*data_me_tuple)
# print_user_data(data_me_tuple)
