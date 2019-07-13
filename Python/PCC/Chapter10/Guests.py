import datetime
name = input("Please insert your name ")
with open("guests.txt" , 'w') as file_object:
    file_object.write(name + '\n')
    a = datetime.datetime.now()
    file_object.write(str(a))
