x = int(input("Please insert the first value "))
y = int(input("Please insert the second value "))
try:
    ratio = x/y
    print(ratio)
except ZeroDivisionError:
    print("Please make sure you are inserting a numerical number!")
