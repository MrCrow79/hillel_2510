# len(чогось)  функція яка повертає довжину чогось

name = 'den'

len_of_row = len(name)
# print(len_of_row)
# print(len(''))
# print(len([1,2]))
# print(len([]))

# len не буде працювати з int, bool, None, float

# in - перевірка на входження, повертає bool

# is_e_in_den = 'e' in 'Den'  # булева змінна, True
# print(is_e_in_den)
# print('x' in 'Den')
#
# if 10 in [1,2,3]:
#     pass

name = 'den'
print(id(name))
name = name + 'a'
print(id(name))


word_for_count = 'hihihasdasd'
count_of_h = word_for_count.count('h')
print(count_of_h)