class Car:

    def __init__(self, engine, number_of_wheels=4, tank=50, coef_of_gas_to_km=0.1):
        self.engine = engine
        self.number_of_wheels = number_of_wheels
        self.tank = tank
        self.current_level_of_gas = tank
        self.coef_of_gas_to_km = coef_of_gas_to_km

    def drive(self, point_of_destination: str, distance: int):

        if (self.current_level_of_gas - distance*self.coef_of_gas_to_km) < self.get_minimum_fuel_in_car():
            print('You have to small fuel')
            return
        self.current_level_of_gas = self.current_level_of_gas - distance*self.coef_of_gas_to_km
        print(f'Driving to {point_of_destination}')

    def start(self):
        print('Start....')

    def stop(self):
        print('Stop....')

    def get_minimum_fuel_in_car(self):
        return 0


    def add_fuel(self, num_of_gas):
        self.current_level_of_gas = self.current_level_of_gas + num_of_gas
        if self.current_level_of_gas  > self.tank:
            self.current_level_of_gas = self.tank


class Nissan(Car):
    brand = 'Nissan'


class NissanSkyline(Nissan):
    model = 'skyline'


class BMW(Car):
    brand = 'BMW'


class MotoBMW(BMW):
    model = 'moto_x1'

    def __init__(self, engine):
        super().__init__(engine=engine, number_of_wheels=2, tank=30, coef_of_gas_to_km=0.3)  # виклик функції __init__ у найпершого батька де є ця функція


class Tesla(Car):
    brand = 'Tesla'




class Model3(Car):
    model = 'Model3'

    def __init__(self, min_tank_level):
        super().__init__(engine='Electro', tank=75, coef_of_gas_to_km=0.1)

        if min_tank_level < 5:
            self.min_tank_level = 5
        else:
            self.min_tank_level = min_tank_level





    def get_minimum_fuel_in_car(self):
        return self.min_tank_level

    # def drive(self, point_of_destination: str, distance: int):
    #
    #     if (self.current_level_of_gas - self.min_tank_level) < distance * self.coef_of_gas_to_km:
    #         print('Model3: You have to small fuel')
    #         return
    #     self.current_level_of_gas = self.current_level_of_gas - distance * self.coef_of_gas_to_km
    #     print(f'Model3: Driving to {point_of_destination}')


skyline_blue = NissanSkyline('v6')
skyline_red = NissanSkyline('v6')
my_moto = MotoBMW('v4')
model_3 = Model3(min_tank_level=20)
print(model_3.min_tank_level)

model_3.drive('Kyiv', 650)

# skyline_red.drive('Kyiv', 400)
# my_moto.drive('Kyiv', 400)
# print(skyline_red.current_level_of_gas)
# print(my_moto.current_level_of_gas)

# print(skyline_blue.number_of_wheels)
# print(my_moto.number_of_wheels)
#
# print(f'{skyline_blue.model} is driving')
# skyline_blue.start()
# skyline_blue.drive('Kyiv', 10)
# skyline_blue.stop()

