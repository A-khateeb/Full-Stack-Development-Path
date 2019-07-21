def value_error(number):
    message = "The number '" +"' you inserted is not considered as an integer"
    print(message)

while True:
    x = input("Please insert the first number ")
    if x == 'q':
        print("Quitting")
        break
    y = input("Please insert the second number ")
    if y == 'q':
        print("Quitting")
        break
    try:
        result = int(x) + int(y)
        int(result)
    except TypeError:
        message = "The number '" +"' you inserted is not considered as an integer"
        print(message)
    except ValueError:
        message = "The number '" +"' you inserted is not considered as an integer"
        print(message)
    else:
        print(result)
