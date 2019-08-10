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
