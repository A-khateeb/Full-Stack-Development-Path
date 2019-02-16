myPets = ["Zophie","Pooka","Fat-tail"]
while True:
    print("Enter a pet name")
    name = input()
if name not in myPets:
    print("I dont have this pet in my list "+name)
else:
    print("Roger that it is in the list")
