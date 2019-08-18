# from Car import ElectricCar, Car
# import Car
# from Car import *
from Car import Car
from electric_car import ElectricCar
my_beetle = Car("VW", 'Beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar("Tesla","roadster",2015)
print(my_tesla.get_descriptive_name())
