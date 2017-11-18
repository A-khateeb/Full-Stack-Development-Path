def spam(DivideBy):
    return 42/DivideBy
try:
    print(spam(2))
    print(spam(0))
    print(spam(12))
    print(spam(1))
except ZeroDivisionError: print("Invalid Argument")
    
