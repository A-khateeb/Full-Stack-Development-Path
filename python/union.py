def union(a,b):
    for e in b:
        if e not in a:
            a.append(e)
            return a

a = [1,2,3]
b = [1,2,6]
print (union(a,b))
