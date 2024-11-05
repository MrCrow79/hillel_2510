utf8_row = 'Привіт'

win_1251 = utf8_row.encode('windows-1251')  # в який формат ковертувати

print(utf8_row)
print(win_1251)

decoded_row = win_1251.decode('windows-1251') # з якого формата ковертувати в utf-8


print(b'\xcf\xf0\xe8\xe2\xb3\xf2'.decode('windows-1251'))  # b = байти
name = 'Den'
f'Hey {name}\n\n'
r'Hey {name}\n\n'  # raw - сира строка, тобто в строці нічого не буде змінюватись, екранування не буде працювати
print(decoded_row)