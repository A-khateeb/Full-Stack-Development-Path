import collections
def sqrt(x):
    if not isinstance(x,(int,float)):
        raise TypeError('x must be numberic !')
    elif x<0:
        raise ValueError('x cannot be negative !')

#b = sqrt('hello')
print(sqrt(-4))
#print('Value of B = ',b)
