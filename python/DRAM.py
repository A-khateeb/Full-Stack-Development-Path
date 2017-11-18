
print (2**10)
print (2**20)
print (2**30)

y = 2**40
print ('Ter compared to byte',y)
y*=8
print ('And compared to bit')
y=7/y
print (y)

#print (2**30*2*8)

def print_all_elements_in(p):
    i= 0
    while i<len(p):
        print (p[i])
        i=i+1

p = [1,2,3,4,5,6,7,8,9,0]
print_all_elements_in(p)

def print_all_element(a):
    for i in a:
        print (i)

z= ["a","b",["c","d"]]

print_all_element(z)





def sum_list(p):
    sum =0
    for i in range(0,len(p)):
        sum = sum + p[i]
    return sum

h = [1,2,3,4,5]
print (sum_list(h))


sum = 0
for s in range(0, len(h)):
    sum = sum +h[s]
print (sum)
