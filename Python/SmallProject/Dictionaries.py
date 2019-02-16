name_birthday = {"Ahmad": "Apr 1", "Mohammad":"Sep 11 ", "Afeef": "10 July"}

while True:
        print("Type the name of your friend (blank to stop)")
        name = input()
        if name == '':
            break

        if name in name_birthday:
            print("The birthday of your friend is : "+name_birthday[name])
        else:

                print("The name does not exist "+ name)
                print("What is "+ name+"'s birth date")
                bday = input()
                name_birthday[name] = bday
                print(name_birthday)
                print("It is now saved in the database")


