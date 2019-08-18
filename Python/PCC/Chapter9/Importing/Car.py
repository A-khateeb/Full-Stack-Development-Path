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
