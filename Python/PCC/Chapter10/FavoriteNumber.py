import json
filename = "number.json"
fav_number = input("What is your favorite number? ")
with open(filename, 'w') as file_object:
    json.dump(fav_number, file_object)

with open(filename) as file_object:
    fav_number = json.load(file_object)
    print("Your favorite number is " + fav_number)
    
