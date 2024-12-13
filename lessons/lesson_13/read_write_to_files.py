
# f = open('main')
# data = f.read()
# f.close()

# r - читати
# w - створити(пере-створити) і записати
# a - створити та додати(або просто додати)
# r+ -  ситати + писати
# a+ -  читати + додавати
# rb -  з байтами
# wb -  з байтами
# ab -  з байтами

file_name = 'example.log'
# lines_4_writing = ['first_row', '\n', 'second_row', '\n', 'third row']
# lines_4_writing2 = ['first_row', 'second_row', 'third row']
# with open(file_name, 'w') as f:
#     data = f.write('first_row')
#     data = f.write('\n')
#     data = f.write('second_row')
#     data = f.write('\n')
#     f.write('\n'.join(lines_4_writing2))  # свлеїти в одну строку з \n між елементами
#     # f.writelines(lines_4_writing)


with open(file_name, 'a') as f:
    f.write('\nnew row from append')

with open(file_name, 'r') as f:
    data = f.read()

for row in data.split('\n'):
    if row.endswith('_row'):
        print(row)
