def custom_calc(num1: int | float, num2: int | float, operation='+', return_string: bool = False):

    if operation == '+':
        result = num1 + num2

    elif operation == '-':
        result = num1 - num2

    elif operation == r'/':
        if num2 == 0:
            print('You cant divide by 0')
            return
        result = num1 / num2

    else:
        print('You have to put some normal operator')
        return

    if return_string:
        return str(result)

    return result


result1 = custom_calc(1, 3)
result2 = custom_calc(1, 3, r'/')
result3 = custom_calc(1, 3, return_string=True)
result4 = custom_calc(1, num2=3, return_string=True)
result5 = custom_calc(operation='/', num2=5, num1=1, return_string=True)


print(result1)
print(result2)
print(type(result3), result3)
print(type(result4), result4)
