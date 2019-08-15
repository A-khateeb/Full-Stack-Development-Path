from random import random
class Restaurant():
     def __init__(self, rname, rType):
         self.rname = rname
         self.rType = rType
         self.number_served = 10

     def open_restauarant(self):
         return(self.rname + " is open now")

     def customers_served(self):
         return("The number of customers served is " + str(self.number_served))
     def describe_restaurant(self):
         return(self.rname + " is a " +self.rType)

     def set_number_served(self, customers):
         self.number_served = customers
     def increment_served(self, customers):
         self.number_served += customers



class IceCream(Restaurant):
    def __init__(self, rname, rType):
        super().__init__(rname, rType)
        self.rname = rname
        self.rType = rType
    def describe_flavors(self):
        flavoree = ["A","B","C"]
        for items in flavoree:
            message = "The flavor you are searching for is "  + list(range(items))
        return(message)

new_rest = Restaurant("Pizza Hut" , "French cuzine")
print(new_rest.rname.title())
print(new_rest.describe_restaurant())
ice = IceCream("Pizza Hut" , "French cuzine")
print(ice.describe_flavors())
print()
#new_rest.number_served = 66
new_rest.set_number_served(50)
new_rest.increment_served(10)
print(new_rest.customers_served())
