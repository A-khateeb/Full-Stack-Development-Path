def greatest(p):
    big = 0
    for e in p:
        if e>big:
            big = e
    return big

print (greatest([1,2,3,4,5]))

print (greatest([]))

print (greatest([24,66,11,12,75]))
