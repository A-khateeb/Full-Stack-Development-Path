r =  [1,2,3,4,5,6,7]
print(r)
p = r[::-1]
print(p)
'''''
'''''
def reverse(data):
    return [data[-(i+1)] for i in range (len(data))]


data = [1,2,3,4,5,6,7,8]
m = reverse(data)
print(m)
