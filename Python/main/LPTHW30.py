people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars")
elif cars < people:
    print("We should not take the cars")
else:
    print("We should not take the cars@!!!!")

if trucks > cars:
    print("That's too many trucks")
elif trucks < cars:
    print("Maybe we can take the cars")
else:
    print("We still cannot decide!")

if people > trucks:
    print("Let us just take the trucks")
else:
    print("Let us stay at home")
