from Zero_Division import x
from Max_Optional_Key import maximum
import math
def fibonaci():
    a,b = 0,1
    while True:
        yield a
        a,b =b, a+b



print(fibonaci())
c = float(input("Insert a value for C as integer"))
#print(pi(c))
print(math.sqrt(c))
r = int(input("Insert the first value"))
d = int(input("Insert the second value"))
maximum(r,d)
