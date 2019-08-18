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
#        return(flavoree[0:])
        return("The flavors you are looking for are \n"+"\n".join(str(x) for x in flavoree))
