'''
def Odd_square(n):
    assert n > 0
    for n in range(0,n):
        if n%2 != 0:
            print(n)
for n in range(0,n):
    if n%2 != 0:
        print(sum([n**2]))

'''
n = int(input("Please insert the value you want to calculate\n"))
assert n >0
r = float(sum(n**2 for n in range (0,n) if n% 2 !=0))
print(r)
