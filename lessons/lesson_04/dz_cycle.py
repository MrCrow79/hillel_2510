# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""

adwentures_of_tom_sawer = ''

counter = 0
for word in adwentures_of_tom_sawer.split():
    if word.istitle():
        counter += 1
print(counter)