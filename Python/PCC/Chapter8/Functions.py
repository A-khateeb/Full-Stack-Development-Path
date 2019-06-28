# def greet_user():
#     '''Display a simple greeting!'''
#     print("Hello")
#
# def greet_user(username):
#     '''Display a simple greeting!'''
#     print("Hello " + username.title() + "!")
#
# name = 'afeef'
# greet_user(name)
#
# ##############################
# ##############################
#
# #Positional Arguments are arguments based on the position of the parameter passed in the function
# #Data passed in the function is a parameter
# def animal_info(animal_type, animal_name):
#     print("I have a " + animal_type+ "!")
#     print("My "+ animal_type + "'s name is "+ animal_name.title())
# #Data passed in the function call is an argument
# animal_info('Cat', 'Harry')
# animal_info('Shambar', 'Hamster')
# ##############################
# ##############################
# #Keyword arguments are name-value passed to the function in the function call
# #Data passed in the function is a parameter
# def animal_info(animal_type, animal_name):
#     print("I have a " + animal_type+ "!")
#     print("My "+ animal_type + "'s name is "+ animal_name.title())
# #Data passed in the function call is an argument
# animal_info(animal_type = 'Cat', animal_name = 'Harry')
# animal_info(animal_name = 'Willie', animal_type = 'Hamster')
# ##############################
# ##############################
# def animal_info(animal_name, animal_type = "dog"):
#     print("I have a " + animal_type+ "!")
#     print("My "+ animal_type + "'s name is "+ animal_name.title())
# #Data passed in the function call is an argument
# animal_info(animal_name = 'Harry')
# animal_info(animal_name = 'Willie', animal_type = 'Hamster')
# #animal_info()
# ##############################
# ##############################
# ##Return value
#
# def get_name(first_name, last_name):
#     full_name = first_name +' '+last_name
#     return full_name.title()
# musician = get_name('Harry', 'Potter')
# print(musician)
#
# ##############################
# ##############################
# #Return a value with optional argument
#
# def get_name(first_name ,last_name, middle_name = ''):
#     if middle_name:
#         full_name = first_name +' '+middle_name+' '+last_name
#     else:
#         full_name = first_name + ' ' + last_name
#     return full_name.title()
# musician = get_name('Harry','Potter', middle_name = 'lee')
# print(musician)
# musician = get_name('Harry','Potter')
# print(musician)
# ##############################
# ##############################
# #Return a dictionary
#
#
# def build_person(first_name , last_name, age = '' ):
#     person= {'first':first_name, 'last': last_name}
#     if age:
#         person['age'] = age
# #        print(person)
#     return person
#
# musican = build_person('Afeef' ,'khateeb', age = '26')
# print(musican)
# ##############################
# ##############################
# ##While loop with a function
# def get_formated_name(first_name, last_name ):
#     full_name = first_name + " "+last_name
#     return full_name
#
# while True:
#     print("Please tell me your name ")
#     print("Enter q or Q to quit")
#     f_name = input("First Name ")
#     if f_name == 'q' or f_name == 'Q':
#         break
#     l_name = input("Last Name ")
#     if l_name == '1' or l_name == 'Q':
#         break
#     name = get_formated_name(f_name,l_name)
#     print("Hello "+ name)
#
# ##############################
# ##############################
#
#
# def greeting_user(names):
#     for i in names:
#         msg = 'Hello ' + i.title()
#         print(msg)
#
#
# username = ['hannah', 'afeef' , 'Muhammad' ]
# greeting_user(username)

##############################
##############################

# unprinted_desing = ['iphone Case','robot pendant','dodecahedron']
# completed_desgin = []

# while unprinted_desing:
#     current_design = unprinted_desing.pop()
#     print("Printing Model " + current_design)
#     completed_desgin.append(current_design)
# print("The following models have been printed")
# for completed_desgin in completed_desgin:
#     print(completed_desgin.title())

def print_design(unprinted_desing, completed_desgin):
    while unprinted_desing:
        current_design = unprinted_desing.pop()
        print("Printing Model: " + current_design)
        completed_desgin.append(current_design)

def show_completed_design(completed_desgin):
    print("Designs that are done:\n")
    for s in completed_desgin:
        print(s.title())

unprinted_desing = ['iphone Case','robot pendant','dodecahedron']
completed_desgin = []

print_design( unprinted_desing, completed_desgin)
show_completed_design(completed_desgin)
