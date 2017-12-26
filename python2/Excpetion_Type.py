#name = int(input("Enter your age"))
age = -1
while age <=0:
    try:
        age = int(input("Insert your age\n"))
        if age <= 0:
            print("YOur age must be a positive number")
    except (ValueError, EOFError):
        pass
