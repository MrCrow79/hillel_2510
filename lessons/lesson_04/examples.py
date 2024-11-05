row = 'Banana, 1, apple, 2, list, str, 3, ten, 7'

# замінити числа 1, 2, 3, 4 на one, two, three, four
# результат = строка з заміниними цифрами

index_1 = row.find('1')  # число
new_row = row.replace('1', 'one')
new_row = new_row.replace('2', 'two')
new_row = new_row.replace('3', 'three')
new_row = new_row.replace('4', 'four')

new_row_2 = (row.replace('1', 'one').replace('2', 'two').replace('3', 'three')
             .replace('4', 'four'))
#
# print(row)
# print(new_row)
# print(new_row_2)

# Зробити так, що б кожне нове речення починалось з великої літери. Всі інші слова з маленької

text = ('Метод використовується для пошуку підстрічки в рядку і повертає індекс '
        'першого входження знайденої підстрічки. Якщо підстрічка не знайдена, повертається -1. і нове речення')

split_text = text.split('.')
# print(split_text)

for sent in split_text:
    var = sent.lstrip()  # прибрали пробіли і записали результат в var
    print(var.capitalize())