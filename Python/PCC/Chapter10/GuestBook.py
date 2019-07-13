import datetime as dt
file_path = ("guest_book.txt")
print("Insert q or Q to Quit!")
while True:

    name = input("Insert your name please ")
    if name == "q" or name == "Q":
        exit()
    else:
        a = "Welcome " + name +" to the party"
        print(a)
        b = dt.datetime.now()
        with open(file_path , "a") as file_object:
            file_object.write(name + '\t')
            file_object.write(a + '\t')
            file_object.write(str(b))
            file_object.write("\n")
