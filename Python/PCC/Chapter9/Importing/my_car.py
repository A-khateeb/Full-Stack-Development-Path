from Car import Car

my_car = Car('Audi','A4',2016)
print(my_car.get_descriptive_name())
my_car.odometer_reading = 23
print(my_car.read_odometer())
