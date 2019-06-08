people = []
person1 = {"First Name":"Afeef","Last Name":"Khateeb","age":27,"city":"Jerusalem"}
person2 = {"First Name":"Muhammad","Last Name":"Nairokh","age":30,"city":"Ramallah"}
person3 = {"First Name":"Ahmad","Last Name":"Abu Shambar","age":50,"city":"Yafa"}

people.append(person1)
people.append(person2)
people.append(person3)

for i in people:
    for m,n in i.items():
        print((str(m)).title()+ ": "+(str(n)).title())
    print(".............")
