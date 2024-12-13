from enum import Enum

class BaseEnum(Enum):

    @classmethod
    def get_all_as_list(cls):
        return [k.value for k in list(cls)]


class Scores(BaseEnum):
    POSITIVE = 'positive'
    NEGATIVE = 'negative'


class Averages(BaseEnum):
    GOOD = 'good'
    BAD = 'bad'


resposen_value = 'postive'
resposen_value2 = 'negative'

# for k in [resposen_value, resposen_value2]:
#     assert k in Scores.get_all_as_list(), f'{k} not one of {Scores.get_all_as_list()}'

print(Scores.POSITIVE.value)

print(Scores.get_all_as_list())
print(Averages.get_all_as_list())

# print(Scores.POSITIVE.value)
# print(Scores.NEGATIVE.value)
# print(Averages.GOOD.value)