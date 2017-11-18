def union(a,b):
    for e in b:
        if e not in a:
            a.append(e)
            return a

a = [1,2,11,23,4567,900,13]
b = [1,2,6,22,34567,900,4567]

print (union(a,b))
