# my_row = 'A nottt very long string that spans two lines'
# #
# # for char in my_row:
# #     print(char)
#
# last_char = my_row[-1]  # останній символ
# before_last_char = my_row[-2]  # передостанній
# print(last_char)
# print(before_last_char)
#
# print(len(my_row))  #  кількість символів в my_row
#
# char_43 = my_row[42]
# print(char_43)
#
# #error_char = my_row[1000]
#
# first_5_symbols = my_row[:5]  # від 0 до 5 і 5 невключно
# first_6_symbols = my_row[0:6]  # від 0 до 6 і 6 невключно
# from_5_30_symbols = my_row[5:30]  # від 5 до 30 і 30 невключно
# print(first_5_symbols)
# print(first_6_symbols)
# print(from_5_30_symbols)
#
# each_2_symbol = my_row[0:-1:2] # від 0 до останнього з кроком 2
# print(each_2_symbol)
# print(my_row[30:])      # від 30(включно) до кінця  з кроком 1
#
# print(my_row[::2])  # кожен другий елемент
#
# print(my_row[::-1]) # перегонути строку
#
#
description = ("f-стрічки (formatted string literals) введені у "
               "Python 3.6 та є зручним способом форматування рядків. "
               "Вони дозволяють вбудовувати значення змінних та виразів "
               "безпосередньо в рядок, забезпечуючи більш читабельний та компактний код.")


print(description[:21])

print(len(description))
print(description[-5:])