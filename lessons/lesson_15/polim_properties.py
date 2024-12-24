class Student:

    def __init__(self, name, math_score, lit_score):
        self.name = name
        self.math_score = math_score
        self.lit_score = lit_score
        self.__average_score = None
        self.__set_average_score()


    def __set_average_score(self):
        self.__average_score = (self.lit_score * 1.1 + self.math_score * 0.9)/2

    @property
    def average_score(self):  # для читання
        return self.__average_score

    # @average_score.setter
    # def average_score(self, value):  # для читання
    #     self.__average_score = value
    #     print('!!!ALARM average score was changed')


alex = Student('Alex', 90, 75)
print(alex.average_score)  # викликає property average_score
# alex.average_score = 90   # викликає average_score.setter average_score
# print(alex.average_score)


class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return 'Animal sounds'


class Dog(Animal):
    pass
    # def make_sound(self):
    #     return "Woof!"


class Cat(Animal):
    def make_sound(self):
        return "Meow!"


# Використання поліморфізму
animals = [Dog("Buddy"), Cat("Whiskers")]

# for animal in animals:
#     print(f"{animal.name} says: {animal.make_sound()}")
# Виведе:
# Buddy says: Woof!
# Whiskers says: Meow!

# __all__ = ['Cat', 'Dog']