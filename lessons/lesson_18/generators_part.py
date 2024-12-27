import time

def get_numbers_from_0_to_5():
    print('start')
    a = 1
    yield 0
    a = 1
    yield 1
    a = 1
    yield 2
    a = 1
    yield 3
    a = 1
    yield 4
    a = 1
    yield 5

#
# for k in get_numbers_from_0_to_5():
#     print('current number', k)



# print(get_numbers_from_0_to_5())
# res = get_numbers_from_0_to_5()  # в змінну res покладе ітератор від генератора get_numbers_from_0_to_5
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))

start_time = time.time()  # поточний час в секундах
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Використання генератора для отримання чисел Фібоначчі
fib = fibonacci_generator()
for _ in range(400000):
    next(fib)

print('Time result', time.time() - start_time)
