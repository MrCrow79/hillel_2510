name = 'Den'
age = 33

row = f"My name is {name}. Im {age} years old"

row2 = "My name is {name}. Im {age} years old".format(name='Alex', age=22)
row3 = "My name is {}. Im {} years old".format(name, age)

row4 = "My name is {}. Im {} years old"

print(row)
print(row2)
print(row3)
print(row4.format('Lex', 55))
print(row4)