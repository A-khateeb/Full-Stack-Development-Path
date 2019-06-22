# def greet_user():
#     '''Display a simple greeting!'''
#     print("Hello")

def greet_user(username):
    '''Display a simple greeting!'''
    print("Hello " + username.title() + "!")

name = 'afeef'
greet_user(name)

##############################
##############################

#Positional Arguments are arguments based on the position of the parameter passed in the function
#Data passed in the function is a parameter
def animal_info(animal_type, animal_name):
    print("I have a " + animal_type+ "!")
    print("My "+ animal_type + "'s name is "+ animal_name.title())
#Data passed in the function call is an argument
animal_info('Cat', 'Harry')
animal_info('Shambar', 'Hamster')
##############################
##############################
#Keyword arguments are name-value passed to the function in the function call
#Data passed in the function is a parameter
def animal_info(animal_type, animal_name):
    print("I have a " + animal_type+ "!")
    print("My "+ animal_type + "'s name is "+ animal_name.title())
#Data passed in the function call is an argument
animal_info(animal_type = 'Cat', animal_name = 'Harry')
animal_info(animal_name = 'Willie', animal_type = 'Hamster')
##############################
##############################
def animal_info(animal_name, animal_type = "dog"):
    print("I have a " + animal_type+ "!")
    print("My "+ animal_type + "'s name is "+ animal_name.title())
#Data passed in the function call is an argument
animal_info(animal_name = 'Harry')
animal_info(animal_name = 'Willie', animal_type = 'Hamster')
