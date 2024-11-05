# row = "10.5"
# # float_row = float(row)
# # print(type(float_row))
# # print(float_row)
# #
# row2 = '10'
# int_row2 = int(row2)
# # print(type(int_row2))
# # print(int_row2)
# #
# # num1 = 15.7
# #
# # str_num1 = str(num1)
# #
# # print(type(num1))
# # print(type(str_num1))
# # print(str_num1)
#
# # print(type(int_row2))
# # print(isinstance(int_row2, int))
# #
# # if type(int_row2) == int:
# #     print('int int by using type')
# #
# # if isinstance(int_row2, int):
# #     print('int int by using isinstance')
# #
# # print(isinstance(False, int))
# # print(isinstance(False, bool))
#
#
# if 'n' in 'instrument':  #=> спочатку обчислюеться вираз  'n' in 'instrument' який повертає True, а потім If True
#     print('Was found')
#
# if 'n' in 'istrumet':  #=> спочатку обчислюеться вираз  'n' in 'istrumet' який повертає False, а потім If False
#     print('Was found 2')
#
# if 'instrument'.find('n'): # повертає індекс першого входження, число
#     print('Was found 3')
#
# if 'instrument'.find('n'):  # 'instrument'.find('n') повертне 1, а потім буде if bool(1) що дорівнює if True
#     print('Was found 3')
#
# # if 'instrument'.find('n'):  # 'instrument'.find('n') повертне 1, а потім буде if bool(1) що дорівнює if True
# # if 1:
# # if bool(1):
# # if True:
# #     print('Was found 3')
#
# print(bool('asd'))  # True
# print(bool(1)) # True
# print(bool(-1)) # True
# print(bool([1,23])) # True
# print(bool(True)) # True
#
# print(bool(''))  # False
# print(bool(0)) # False
# print(bool([])) # False
# print(bool(False)) # False
# print(bool(None)) # False

the_word = 'asdasdas'
if 'instrument'.find(the_word):  # 'instrument'.find('asdasdas') повертне -1, а потім буде if bool(-1) що дорівнює if True
    print(f'Was found {the_word}')

the_word2 = 'ins'
if 'instrument'.find(the_word2):  # 'instrument'.find('ins') повертне 0, а потім буде if bool(0) що дорівнює if False
    print(f'Was found {the_word2}')

# print(bool(None))


