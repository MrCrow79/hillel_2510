row = 'Hello wy name is Alex'

spl_row = row.split()

print(spl_row)

join_row = '_'.join(spl_row)

print(join_row)
print(' '.join(spl_row))

# print(' '.join(['1', '2', ['asd', '2'], '4']))  # помилка

list_names = ['Den', 'Alex', 'Ivan']

filters_list = ['is_active', 'company_id', 'spent_per_day']

print(f'Filters were used: {", ".join(filters_list)}')

print(f'list of names: {list_names}')

print('|'.join(['Alex']))

row1 = 'Hello my name'
row2 = 'Hi I\'m asd'

print('|'.join([row1, row2]))