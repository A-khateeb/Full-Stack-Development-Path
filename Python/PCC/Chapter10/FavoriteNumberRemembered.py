import json
filename = "numbers123.json"

def store_number():
    try:
       with open(filename) as file_object:
           number = json.load(file_object)
#           print("The favorite number is " + number)
    except FileNotFoundError:
        return None
    else:
        return number
def add_number():
    number = store_number()
    if number:
        print("Your favorite number is "+ str(number))
    else:
        number = input("What is your favorite number? ")
        with open(filename, 'w') as file_object:
            json.dump(number, file_object)
            print("You favorite number "+ number +" is added to the safe zone!")

add_number()
