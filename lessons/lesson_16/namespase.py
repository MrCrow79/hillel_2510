value = 75

class Example:

    value = 55


class NewExample:

    value = 65


# ex1 = Example()
# ex2 = NewExample()
#
# print(ex1.value)
# print(ex2.value)
# print(value)


def greetings(name):

    print(f'Hello {name}')

def say_hi():
    name = 'Den'
    print(f'Hi {name}')

# name = 'Alex'
# greetings('Ivan')
# say_hi()

def choose_user_greetings():

    name = 'Den'

    def get_hi():
        name = 'Ivan'
        return f'Hi {name}'

    def get_hello():
        return f'Hello {name}'

    print(get_hi())
    print(get_hello())

    # if len(name) > 3:
    #     print(get_hi())
    # else:
    #     print(get_hello())

name = 'Alex'

# choose_user_greetings()
# print(name)
# choose_user_greetings('Den')