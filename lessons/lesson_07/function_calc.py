def custom_calc(num1: int | float, num2: int | float, operation: str) -> int | float | None:
    if operation == '+':
        return num1 + num2

    if operation == '-':
        return num1 - num2

    if operation == r'/':
        if num2 == 0:
            print('You cant divide by 0')
            return
        return num1 / num2


result = custom_calc(1, 0, r'/')

print(result)
