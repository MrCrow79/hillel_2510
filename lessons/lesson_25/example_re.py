import re

text = """Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# print(text.startswith("Tom gave "))
# print(text.endswith(" in wealth."))
# print("Tom" in text)
#
# print(text.count('Tom'))

text = """
25B usd
25 000000000 usd
25B and 2 usd
25B USD
25B USDA

528B usd
25B EUR"""

# searching elements with 2 digit + B(?) + USD
# 250B USD or 250 billion USD or 250 billion and 215 usd
pattern = r'\b[0-9]{2}[A-Za-z]?\b(.+)\b(usd|USD){1}\b'

x = re.match(pattern, text)

import re

email = "user@example.com"
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(email_pattern, email):
    print("Email введено правильно.")
else:
    print("Некоректний формат email.")


# //div[@jsname="RNNXgb"]/div/div[@jscontroller]/../div