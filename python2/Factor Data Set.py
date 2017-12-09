def scale(data, factor):
    for j in range(len(data)):
        data[j]*=factor
    return j
data = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
count = scale(data,2)
print(count)