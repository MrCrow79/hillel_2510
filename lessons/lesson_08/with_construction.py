# file_ = open('some_file.txt') # відкритят файлу на читання з ім'ям some_file.txt який лежить в цій директорії
#
# data = file_.read()  # витягнути інфу з файла
# # print(data)
#
# file_.close()  # закрити файл
from lessons.lesson_08.exceptions_example import counter

# try:
#     file_ = None
#     file_ = open('some_file1.txt')
#     data = file_.read()
#     print(data)
#
# except FileNotFoundError:
#     print('Can\'t open file')
#
#
# finally:
#     if file_ is not None:
#         file_.close()

with open('some_file.txt') as file_:  # file_ = open('some_file.txt')
    data = file_.read()

print(data)

