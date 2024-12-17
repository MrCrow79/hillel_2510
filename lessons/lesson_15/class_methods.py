class User:

    min_age_of_user = 1
    all_users = []

    def __init__(self, name, age):
        self.name = name
        if age < self.min_age_of_user:
            raise AttributeError(f'Age cannot be less than {self.min_age_of_user}')
        self.age = age

        self.all_users.append({'name': name, 'age': age})   # в классову змінну all_users додаю словник з створеним юзером

    def print_info(self):
        print(f'My name is {self.name}, Im a {self.age} years old' )

    @staticmethod
    def print_hello(name):

        some_value = [42]
        print(f'Hello to {name}')

    @classmethod
    def print_min_age_of_user(cls):
        print(f'Min age is {cls.min_age_of_user}')

    @classmethod
    def get_all_created_users(cls):
        return cls.all_users

    def __del__(self):
        print(f'Deleting object {id(self)}, name = {self.name}')



print(User.get_all_created_users())
den = User('Den', 33)
print(User.get_all_created_users())
alex = User('Alex', 23)
print(User.get_all_created_users())
yuri = User('Yuri', 34)
print(den.get_all_created_users())
print(id(yuri))
yuri.__del__()  #  НЕ правильний спосіб видалення
print('After calling __del__()', id(yuri))
del yuri  # правильний спосіб видалення
print(id(yuri))

den.print_info()  # == User.print_info(den)

# den.print_hello('Den')
# User.print_hello('Alex')
# print(den.min_age_of_user)
# print(User.min_age_of_user)
# den.print_min_age_of_user()
# User.print_min_age_of_user()