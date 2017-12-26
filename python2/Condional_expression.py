#result = param(n if n>=0 else -n)

while True:
    try:
        n = int(input("Please insert the first number to compare"))
        v = int(input("Please insert the second number to compare"))
        result = (n if n>v else v)
        print(result)
    except ValueError:
        print("Please insert a correct value")
        
