# def greetings(name):
#     print(f'hello, {name}')
#
#
# # greetings('Den')
# hello_fn = greetings
# hello_fn('Alex')
#
# def how_are_you(fnct, *args):
#     fnct(*args)
#     print('How are you?')
#
# # how_are_you(greetings, 'Yuri')
#
# greetings2 = how_are_you
# greetings2(greetings, 'Sofa')

# декоратор
def how_are_you(fn):
     def wrapper(*args, **kwargs):
         res = fn(*args, **kwargs)
         print('How are you?')
         return res
     return wrapper


def do_twice(fn):
     def wrapper(*args, **kwargs):
         print('---------------First')
         fn(*args, **kwargs)
         print('---------------Second')
         res = fn(*args, **kwargs)
         print('---------------Done')
         return res
     return wrapper

@how_are_you
@do_twice
def greetings(name):
    print(f'hello, {name}')

greetings('Den')


def skip_errors(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except Exception as e:
            print(f'Catch {e}')

    return wrapper

@skip_errors
def division(num1, num2):
    return num1/num2

@skip_errors(2)
def print_text(text: str, separator='\n', some_value=123):
    print(some_value)
    for k in text.split(separator):
        print(k)

# print_text('asd\nfgh', some_value=8888)

# print(division(1,2))
# print(division(5,0))
# print(division(1,'asd'))
# print(division([1], {2:3}))