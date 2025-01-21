from datetime import datetime


# print(datetime.now())

row1 = '21-01-2025 18:46:00'  # timezone = UTC
row2 = '2025-01-21 6:30:20 PM'  # timezone = UTC
row3 = '25-20-02 6:30:20.333 AM'  # timezone = UTC, але маємо microseconds
row4 = '21-01-2025T18:46:00 +0100'  # timezone = +1 hour

# datetime.strftime()  # from td object
# datetime.strptime()  # to datime object

row1_td = datetime.strptime(row1, '%d-%m-%Y %H:%M:%S')  # to datime object
row2_td = datetime.strptime(row2, '%Y-%m-%d %I:%M:%S %p')
row3_td = datetime.strptime(row3, '%y-%d-%m %I:%M:%S.%f %p')
row4_td = datetime.strptime(row4, '%d-%m-%YT%H:%M:%S %z')

print(type(datetime.strftime(row2_td, '%Y-%m-%d %H:%M:%S')))
print(datetime.strftime(row2_td, '%Y-%m-%d %H:%M:%S'))

# ISO format

print(datetime.fromisoformat('2025-01-21T18:59:57.376764'))

# print(row1_td)
# print(row2_td)
# print(row3_td)
# print(row4_td)