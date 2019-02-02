##Animal is-a object
class Animal(object):
    pass
## Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        self.name = name
## Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        self.name = name
## Person is-a object
class Person(object):
    def __init__(self, name):
        ##Person has a name
        self.name = name
        ## Person has-a Pet
        self.pet = None
##Employee is-a Person
class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

##Fish is-a object
class Fish(object):
    pass
##Salmon is-a Fish
class Salmon(Fish):
    pass
##Halibut is-a Fish
class Halibut(Fish):
    pass

##Satan is-a Cat, is-a Animal
satan = Cat("Satan")
##Rover is-a Dog
rover = Dog("Rover")
##Mary is-a Person
mary = Person("Mary")
##Mary has-a Pet satan
mary.pet = satan
##Frank is-a Employee has-a name has-a salary
frank = Employee("Frank", 10000)
##Frank has-a pet
frank.pet = rover
##Flipper is-a fish
flipper = Fish()
##Crouse is-a Fish
crouse = Fish()
##Harry is-a Halibut
harry = Halibut()
