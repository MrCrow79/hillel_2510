# ''.startswith(), ''.endswith()

# print('Hello my name is Den'.startswith('Hel'))
# print('Hello my name is Den'.endswith('en'))
#
# print('Hello my name is Den'.startswith(' Hel'))
# print('Hello my name is Den'.endswith('en '))

row = 'Hello my name is Den'

# case 1
# print('Hello' in row)

# case 2
sub_row = row[0:5]
# print(sub_row)

# print(sub_row in row)

case3 = row.split()
# print(case3[0] == 'Hello')

the_word = 'Hel'
row = 'Hello my name is Den'

len_of_the_word = len(the_word)
actual = row[0:len_of_the_word]

# print(len_of_the_word)
# print(actual)
#
# print(actual == the_word)

print(row.find(the_word))

if row.find(the_word) == 0:
    print(True)
