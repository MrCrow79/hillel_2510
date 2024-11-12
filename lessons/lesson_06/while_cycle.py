

# while bool

# counter = 10
# while True:  # вічний цикл
#
#     print('while row. counter', counter)
#     counter -= 1  # зменшую каунтер ан 1 при кожній ітерації циклу while
#
#     if counter == 0:
#         break


# while True:
#     user_number = int(input('Catch the number, input number from 0 to 10: '))
#     if user_number == 7:
#         break
# counter = 10
# while counter >= 0:
#
#     print('while row. counter', counter)
#     counter -= 1  # зменшую каунтер ан 1 при кожній ітерації циклу while

while True:

    magic_number = 7

    user_number = int(input('Catch the number, input number from 0 to 10: '))

    if user_number == 7:
        print('You are winner')
        break

    if 6 <= user_number <= 8:
        print('Almost catch')
        continue

    if user_number < 0 or user_number > 10:
        print('Not even close')


