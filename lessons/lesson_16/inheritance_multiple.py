
class Animal:

    def __init__(self, name, color):
        self.name = name
        self.color = color

class Mouse(Animal):

    animal_type = 'Mouse'

    def __init__(self, name, color, paws):

        Animal.__init__(self, name, color)
        # self.name = name
        # self.color = color
        self.paws = paws
        self.live_with_family = True

    @staticmethod
    def make_sound():
        print('Pi-pi-pi')

    @staticmethod
    def walk():
        print('walking...')

class Bird(Animal):

    animal_type = 'Bat'

    def __init__(self, name, color, wings):

        Animal.__init__(self, name, color)
        # self.name = name
        # self.color = color
        self.wings = wings
        self.can_fly = True

    @staticmethod
    def make_sound():
        print('url...')

    @staticmethod
    def fly():
        print('flying...')


class Bat(Mouse, Bird):

    def __init__(self, name, color):

        Bird.__init__(self, name, color, wings=2)
        Mouse.__init__(self, name, color, paws=4)

    def __str__(self):
        return(f'name={self.name}, color={self.color}, wings={self.wings}, paws={self.paws}, '
               f'live_with_family={self.live_with_family}, can_fly={self.can_fly}')


print(Bat.__mro__)

my_bat = Bat('uni', 'grey')
#
# my_bat.fly()
# my_bat.walk()
# my_bat.make_sound()
# print(my_bat)
