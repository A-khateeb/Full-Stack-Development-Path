def count(data,target):
    n = 0
    for item in data:
        data = [None]
        if item == target:
            print("Hit", n, item)
            n+= 1
    return n

dataset=[1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8]

count(dataset,2)
