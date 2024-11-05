row = 'Перевірка, чи рядок складається тільки з Великих Літер:'

upper_row = 'ASD'
title_row = 'Aasd As'
lower_row = 'asd'

# print('is_upper', row.isupper())  # чи всі літери великі
# print('is_upper', upper_row.isupper())
#
# print('is_title', row.istitle()) # чи кожна літера нового словавелика
# print('is_title', title_row.istitle())
#
# print('is_lower', row.islower())  # чи всі літери малі
# print('is_lower', lower_row.islower())


print(row.upper())
print(row.lower())
print(row.title())
print(row.capitalize()) # робить великою тільки першу літеру
print(row.swapcase())
print(row)

# # usd USD, Usd
#
# returned_row = 'Hi.. bla-bla 10 Usd'
#
# new_text = returned_row.lower()
# print('Usd'.lower() in new_text)