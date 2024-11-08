# tuple

# names = ('Den', 'Alex', 'Ivan')
#
# print(names[0])
# print(names[1:2])
#
# for name in names:
#     print(name)
#
#
# tuple_obj = (1, 'Den', 5.25, None, False, (1,2,3), [])
#
# print(tuple_obj[-2]) # передостанній
# print(tuple_obj)
# new_tuple = tuple_obj + (1,2,3,4)
#
# print(id(tuple_obj), tuple_obj)
# print(id(new_tuple), new_tuple)
# print(type(names))
# print(names)

names = ('Den', 'Alex', 'Ivan', 'Den', 'Alex')

print(names.count('Den'))
print(names.count('Ivan'))

print(names.count('asdasd'))
print('-'*80)
print(names.index('Alex'))  # return index 1
print(names.index('Alex', 2))  # return index 4

print(names.index('Alex', 0, 2))  # return index 1, .index(element, start_index(include), stop_index(not include))
print(len(names))


