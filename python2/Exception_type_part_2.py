age = -1
while age <=0:
    try:
        age = int(input("Please insert your age\n"))
        if age <=0:
            print("Please make sure to insert your correct age!")
    except ValueError:
        print("Please insert a suffient age!")
        raise   
    except IOError:
        print("Please re-insert your age!")
        raise
