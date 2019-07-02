class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is sitting now")
    def roll_over(self):
        print(self.name.title() + " rolled over!")

my_dog = Dog('willie' , 6)
print("My dogs name is " + my_dog.name.title())
print("My dogs age is " + str(my_dog.age))
my_dog.name
