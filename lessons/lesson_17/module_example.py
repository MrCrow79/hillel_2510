import sys

# print(sys.path)

sys.path.append('/home/den/hillel/hillel_2510/')
# print(sys.path)

from lessons.lesson_15.polim_properties import Cat


# import math, json  # import json
import math as mt
# #
# # from math import sqrt, tau
from math import sqrt as math_sqrt

from math import *  #  імпорт все, небажаний варіант

# from CONSTANTS import *

#
# print(math.pi)
print(mt.e)
print(sqrt(25.5))
print(math_sqrt(35.5))
print(tau)



# def test_check_cat():
#     my_cat = Cat(name='Tigra')
#     assert my_cat.make_sound() == "Meow!"

my_cat = Cat(name='Tigra')
assert my_cat.make_sound() == "Meow!"