def product(data):
    for i in range(len(data)):
        if (i*i)%2 !=0:
            print(i)

l = [1,2,3,4]
c= product(l)
print(c)
