# print(all([1, 'asd', True, [1,2]]))  # поверне true якщо bool(кожнийй елемент) == True
# print(all([1, '', True, [1,2]]))  # поверне true якщо bool(кожнийй елемент) == True
#
# print(any([0, False, []]))  # поверне true якщо хоча б 1 bool(кожнийй елемент) == True
# print(any([1, False, []]))  # поверне true якщо хоча б 1 bool(кожнийй елемент) == True


users = [{'id': 1}, {'id': 30}, {'id': 17}]

# for index, user in enumerate(users, start=1):
#     print(f'Index of {user} is {index}')


# print(list(filter(lambda x: x['id']> 15, users)))
#
# print(min([1,2,-3], key=lambda x: pow(x, 2)))
# print(max([1,2,-3], key=lambda x: pow(x, 2)))
#
# print(sum([1,5,6,7,254,345]))


# base_numbers = [2, 4, 6, 8, 10, 2, 3, 4]
# powers = [1, 2, 3, 4, 5]
# numbers_powers = list(map(lambda x, y: x+y, base_numbers, powers))  # x + y
# numbers_powers = list(map(pow, base_numbers, powers))  # pow(x, y) -  піднесення в степінь
# # [pow(base_numbers[0], powers[0]), pow(base_numbers[1], powers[1]), ..., pow(base_numbers[-1], powers[-1])]
#
# print(numbers_powers)  # [2, 16, 216, 4096, 100000]
#
# print([pow(base_numbers[k], powers[k]) for k in range(min([len(base_numbers), len(powers)]))])
#
# list_of_rows = ['asd', '', 'asd', None]
# list_of_rows2 = ['asd', '', 'asd', None]
#
# list_of_rows = list(map(lambda x: x if x is not None else '', list_of_rows))
# list_of_rows = [k for k in list_of_rows if k]
# print(list_of_rows)
# list_of_rows = list(filter(lambda x: x, list_of_rows))
# print(list_of_rows)
#
# list_of_rows = [k for k in list_of_rows2 if k]
# print(list_of_rows2)


