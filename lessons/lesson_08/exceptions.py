
# def division(a, b):
#
#     if b == 0:
#         print('You cant divide by 0')
#         return
#     return a / b

def division(a, b):

    result = None
    try:
        result = a / b  # код де потенційно буде помилка

    except ZeroDivisionError as e:  # перехоплення конкретної помилки
        print('ZeroDivisionError. You cant divide by 0')
        print('Error reason is: ', e)

    except ArithmeticError as e:  # перехоплення конкретної помилки
        print('ArithmeticError. You cant divide by 0')
        print('Error reason is: ', e)

    except TypeError as e:
        print('Incorrect action')
        print('Error reason is: ', e)

    except (ZeroDivisionError, TypeError) as e:
        print('somth happens')
        print('Error reason is: ', e)

    return result

print(division(1, 2))
print('-'*80)
print(division('1', 2))
print('-'*80)
print(division(1, 0))

