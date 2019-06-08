pets = []
pet_1 = {'Pet Name ':'Dog','age':5,'owner':'Afeef'}
pet_2 = {'Pet Name ':'Cat','age':25,'owner':'Tarq'}
pet_3 = {'Pet Name ':'Fish','age':35,'owner':'Muhammad'}
pet_4 = {'Pet Name ':'Wolf','age':15,'owner':'Ahmad'}

pets.append(pet_1)
pets.append(pet_2)
pets.append(pet_3)
pets.append(pet_4)

for i in pets:
    for m,n in i.items():
        print(str(m) , str(n))
