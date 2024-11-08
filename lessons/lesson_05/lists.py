names = ['Den', 'Alex', 'Den', 'Ivan']

print(names[0])
print(names[1:])

for name in names:
    print(name)

print(names.count('Ivan'))
print(len(names))

print('-' * 80)

# update list

# append

names.append('Mor')  # додає як 1 елемент в names

print(names)
# print(id(names))

# names.append([1,2])
# print(names)
# names[-1].append(3)
# print(names)
# print(names[-1][-1])

# print(id(names))
# print(hash(names))

# names.extend([1,23])  # розширює names
# names.extend(('t1', 't2'))  # розширює names
# names.extend('string_values')  # розширює names
# print(names)

# names.insert(2, 'el_4_insert')
# names.insert(5, 'new_el_index')  # names.append('new_el')
# names.insert(len(names), 'new_el_len')  # names.append('new_el')
# names.insert(99, 'new_el_index')  # names.append('new_el')

# print(names)

# extracting

# first_name = names.pop(0)
# second_name = names.pop(-2)
# third_name = names.pop()
# print(names)
# print(first_name)
# print(second_name)
# print(third_name)

# numbers = [1,2,3,4,10,5,6,7,8]
#
# for number in range(len(numbers) - 1):  # for number in (0, 1, 2, 3, 4, 5, 6, 7, 8)
#
#     cur_num = numbers.pop()
#     if cur_num == 10:
#         print(10)
#         break
#
# print(numbers)

# remove

# names.remove('Den')
#
# print(names)
#
# if names.count('Zim') > 0:
#     names.remove('Zim')


# first_name, second_name, third_name, before_last_name, last_name = names

# print(first_name)
# print(second_name)
# print(third_name)
# print(before_last_name)
# print(last_name)


# first_name, *other_names = names
# print(first_name)
# print(other_names)
#
# print('-'*80)
# first_name, *other_names, last_names = names
# print(first_name)
# print(other_names)
# print(last_names)

# sorting

# numbers_list = [1, 2, 3, 4, 5, 7, 8, 6]
#
# new_sorted_list = sorted(numbers_list)
# new_reverse_sorted_list = sorted(numbers_list, reverse=True)
# print(new_sorted_list)
# print(numbers_list)
# # print(new_reverse_sorted_list)
#
# numbers_list.sort()
# numbers_list.sort(reverse=True)
# print(numbers_list)
#
# ids = [1,2,3,4,5,6,8,7]
#
# assert ids == sorted(ids), 'List are not sorted'

# print(sorted(names))

#
# my_tuple = (1,2,3)
# my_str = 'asdasd'
#
#
# my_tuple_list  = list(my_tuple)
# my_str_list  = list(my_str)
# my_range_list = list(range(4))  # [0,1,2,3]
#
# print(my_tuple_list)
# print(my_str_list)
# print(my_range_list)