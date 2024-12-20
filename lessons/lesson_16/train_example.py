# Створити класс потяг, в класі потяг є Локомотив(Вагон), і є Вагони. Вагон це класс.
# Локомотив обов'язковий в потязі, вагони не обов'язкові
# локомотив не може приймати пасажирів
# кожен вагон може приймати до 10 пасажирів


import random
from faker import Faker


class Wagon:
    max_pass = 10  # кожен вагон може приймати до 10 пасажирів

    wagon_number=1

    # def __init__(self):
    def __init__(self, number=None):
        self.pass_ = []
        self.number = number if number is not None else random.choice(range(1, 200))  # випадковий або засетаплений номер вагону
        # self.number = self.wagon_number
        # __class__.wagon_number += 1

    def add_pass(self, pass_: dict):  # {'name': name, 'age': age}
        if len(self.pass_) < self.max_pass:
            self.pass_.append(pass_)

    def __len__(self):
        return len(self.pass_)


class Locomotive(Wagon):
    max_pass = 0  # локомотив не може приймати пасажирів


class Train:

    def __init__(self):
        self.locomotive = Locomotive()  # Локомотив обов'язковий в потязі,
        self.wagons = []  # вагони не обов'язкові
        pass

    def add_wagon(self, wagon: Wagon):
        self.wagons.append(wagon)

    def list_of_pass(self):
        lst = []

        for wagon in self.wagons:
            for pass_ in wagon.pass_:
                lst.append({f'wagon_{wagon.number}': pass_})
        return lst

    def __len__(self):
        return len(self.wagons)


train = Train()

for _ in range(5):
    wagon =  Wagon()
    for k in range(3):
        wagon.add_pass({'name': Faker().name()})  # Faker().name() - генерує рандомне ім'я

    train.add_wagon(wagon)

print(train.locomotive)
print(*train.list_of_pass(), sep='\n')
# train.wagons.append(wagon_1)
# print(train.wagons)
# print(train.wagons[0].pass_)
# print(train.wagons[0].number)
# print(len(train))
# print(len(train.wagons[0]))
#
# print(Wagon().number)
# print(Wagon().number)
# print(Wagon().number)
# print(Wagon().number)
# print(Wagon().number)
# print(Wagon().number)
