def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
            numBrought = numBrought + v.get(item, 0)
    return numBrought
  

allGuests = {"Alice":{"Apples": 5,"Pretzels":12},
             "Bob":{"Ham Sandwiches":3,"Apples":2},
             "Carol":{"Cups":3,"Apple Pies":1}}



print("Number of things being brought")

print("- Apples "+str(totalBrought(allGuests,'Apples')))
print("- Pretzels "+str(totalBrought(allGuests,'Pretzels')))
print("- Ham sandwiches "+str(totalBrought(allGuests, 'Ham Sandwiches')))
print("- Cups "+str(totalBrought(allGuests,'Cups')))
print("- Apple Pies "+str(totalBrought(allGuests, 'Apple Pies')))
