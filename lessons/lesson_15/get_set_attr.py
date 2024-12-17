class User:

    def __init__(self, name, math_score):
        self.name = name  # min 3, max 20, self.__setattr__('name', name)
        self.math_score = math_score  # від 1 до 100, self.__setattr__('math_score', math_score)


    def __setattr__(self, key, value):

        if key == 'name':
            if len(value) < 4 or len(value) > 20:
                raise AttributeError(f'Name should be between 3 and 20 chars, cur_value is {value}')
            # super().__setattr__(key, value)  # викличе __setattr__, батьківського класу

        elif key == 'math_score':
            if value < 1 or value > 100:
                raise AttributeError(f'math_score should be between 1 and 100, cur_value is {value}')
            # super().__setattr__(key, value)  # викличе __setattr__, батьківського класу

        # else:
        #     raise AttributeError(f'user can have only math_score and name')

        super().__setattr__(key, value)  # викличе __setattr__, батьківського класу


    def __getattribute__(self, item):

        return f'You get the {item} and values is {super().__getattribute__(item)}'

alex = User('Alex', 8)
# alex.math_score = 100500  #  ==> alex.__setattr__('math_score', 100500)
alex.age = 55

# print(alex.name)
# print(alex.math_score)
# print(alex.age)

print(getattr(alex, 'name'))

# for score in ['average', '95lt', 'min_value']:
#     assert getattr(alex, score) > 0