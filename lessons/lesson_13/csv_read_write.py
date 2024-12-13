import csv

# Вказуємо розділювач як крапка з комою
with open('output.csv') as csvfile:
    data = list(csv.reader(csvfile))

for row in data:
    print(', '.join(row))

print('-'*80)

headers = data[0]
rows = data[1:]
# data_list = []

# for row in rows:
#     tuple_headers_row = tuple(zip(headers, row))
#     print(tuple_headers_row)
#     data_list.append(dict(zip(headers, row)))

data_list = [dict(zip(headers, row)) for row in rows]

print(data_list)

for row in data_list:
    print('user_name', row['Name'])

#  надрукувати всі імена
# for row in data[1:]:
#     print(row[0])

# list_reader = list(reader)
#
# for row in reader:
#     print(', '.join(row))
#
# print('-'*80)
#
# for row in list_reader:
#     print(', '.join(row))