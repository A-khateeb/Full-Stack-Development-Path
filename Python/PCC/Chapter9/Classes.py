class Dog():
    def __init__(self, name, age):
#        pass
         self.name = name
         self.age = age

    def sit(self):
        print(self.name.title()+" is now sitting")

    def roll_over(self):
        print(self.name.title() + " is rolling over")


my_dog = Dog('willie', 26)
your_dog = Dog('lucy', 5)
print("My dog's name is " + my_dog.name.title())
print("My dog's age is " + str(my_dog.age) + " years old")
my_dog.roll_over()
my_dog.sit()
print("\n\n")
print("Your dog's name is " + your_dog.name.title())
print("Your dog's age is " + str(your_dog.age) + " years old")
your_dog.roll_over()
your_dog.sit()

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
        print("This car has " + str(self.odometer_reading) + " miles on it ")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back the odometer!")

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

my_tesla = ElectricCar('Tesla', 'model s ', 2016)
print(my_tesla.get_descriptive_name())
print(my_tesla.battery.describe_battery())
print(my_tesla.battery.get_range())
print(my_tesla.gas_tank_fill())
new_car = Car('Audi' , 'A4', 2019)
print(new_car.get_descriptive_name())
new_car.update_odometer(23500)
new_car.read_odometer()
new_car.increment_odometer(100)
new_car.read_odometer()
