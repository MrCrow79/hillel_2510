# рядок.split(роздільник)  - розділяє рядок по роздільник і  повертає список рядків

row = ('Функція split() використовується для розділення рядка на частини на основі певного роздільника '
       'та повертає список отриманих частин.     Основні варіанти використання split():')

splitted_row = row.split('split')
# print(splitted_row[0])
# print(splitted_row[1])
# print(splitted_row[2])
#
# print(row.split('asdadasdadasd'))
# print(row.split(row))

# split() - розділяти по пробілу

split_without_arg = row.split()
split_with_space = row.split(' ')
# print(split_without_arg)
# print(split_with_space)

# re - regex - regular expressions - регулярні вирази

# [a-zA-z] - всі латинські символи
# \d - всі цифри
# \s - всі цифри

import re
new_row = 'He 9 asd 909 xnxn'

print(re.split(r'\d+', new_row))

