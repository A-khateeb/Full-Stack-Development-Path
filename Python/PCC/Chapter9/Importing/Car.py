"""
A module that represents a car
"""
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.make) + " " + self.model + " " + str(self.year)
        return long_name.title()

    def read_odometer(self):
        return("This car has " + str(self.odometer_reading) + " miles on it ")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            return("You cannot roll back the odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

    def gas_tank_fill(self):
        return("This car needs to be filled in gas ")
class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size

    def describe_battery(self):
        return("This cas has a "+ str(self.battery_size) + "-kmh battery")

    def get_range(self):
        if self.battery_size == 70 :
            range = 240
        elif self.battery_size == 85:
            range = 285
        message = "This car can go approximately " + str(range)
        message += ' miles on full charge '
        return (message)


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def gas_tank_fill(self):
        return("This cas does not need to be filled in fuel!")
