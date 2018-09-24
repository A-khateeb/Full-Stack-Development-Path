def add(a,b):
    print(f"Adding {a} + {b}")
    return a+b

def subtraction(a,b):
    print(f"Subtracting {a} - {b}")
    return a-b

def multiply(a,b):
    print(f"multiply {a} * {b}")
    return a*b

def divide(a,b):
    print(f"Divide {a}/{b}")
    return a/b

print("Let us do some math with just functions ")
age = add(25,2)
height = subtraction(200,10)
weight = multiply(100,2)
iq = divide(100,2)
print(f"Age:{age}, Height:{height}, Weight:{weight}, IQ:{iq}")

print("Here is a Puzzle!")
what = add(age, subtraction(height, multiply(weight,divide(iq,2))))

print("This becomes", what,"Can you do it by hand!")
