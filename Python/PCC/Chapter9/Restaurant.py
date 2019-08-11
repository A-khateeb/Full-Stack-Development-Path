class Restaurant():
	def __init__(self, rname, rType):
		self.rname = rname
		self.rType = rType
	
	def describe_restaurant(self):
		print(self.rname + " is a " + self.rType)
	def open_restauarant(self):
		print(self.rname + " is open now")

new_rest = Restaurant("Pizza Hut" , "French cuzine")
print(new_rest.rname.title())
print(new_rest.describe_restaurant())


