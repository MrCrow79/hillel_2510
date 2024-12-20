class Animal:

    def __init__(self, name):
        self.name = name


class Cat(Animal):

    animal_type = 'Cat'

    def __init__(self, name, color):

        super().__init__(name)  # ==> Animal.__init__(name)
        self.color = color
        self.paws = 4

    @staticmethod
    def make_sound():
        print('Murrr')

class Dog(Animal):
    animal_type = 'Dog'

    def __init__(self, name, color):

        super().__init__(name)  # ==> Animal.__init__(name)
        self.color = color
        self.paws = 4

    @staticmethod
    def make_sound():
        print('Gav')



aria = Cat('aria', 'grey')
riabko = Dog('riabko', 'black')

# print(aria.color)
# print(aria.name)
#
# aria.make_sound()
# print(aria.animal_type)
# riabko.make_sound()
# Dog.make_sound()
# print(riabko.animal_type)

# anima = Animal('Tysia')
#
# print(anima.name)