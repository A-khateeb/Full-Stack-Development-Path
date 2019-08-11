class Restaurant():
	def __init__(self, rname, rType):
		self.rname = rname
		self.rType = rType
	
	def describe_restaurant(self):
		return(self.rname + " is an " + self.rType)

	def open_restauarant(self):
		return(self.rname.title() + " is open now")


new_rest = Restaurant("Pizza Hut" , "French cuzine")
#print(new_rest.rname.title())
print(new_rest.describe_restaurant())
print(new_rest.open_restauarant())

your_rest = Restaurant("Falafel" , "Arabic cuzine")
#print(your_rest.rname.title())
print(your_rest.describe_restaurant())
print(new_rest.open_restauarant())

my_rest = Restaurant("Hamburger" , "American cuzine")
#print(my_rest.rname.title())
print(my_rest.describe_restaurant())
print(new_rest.open_restauarant())

