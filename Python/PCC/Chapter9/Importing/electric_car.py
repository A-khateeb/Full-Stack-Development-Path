from Car import Car
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
