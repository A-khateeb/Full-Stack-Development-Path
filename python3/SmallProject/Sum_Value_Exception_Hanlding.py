import collections
def sum(values):
    if not isinstance(values, collections.iterable):
        raise TypeError("Values must be Iterabe")
#        print("The values inserted must be iterable!")
    total = 0
    for v in values:
        if not isinstance(v, (int,float)):
            raise TypeError("Values must be numeric")
#            print("Values must be numeric")
        total= total+v
    return total
