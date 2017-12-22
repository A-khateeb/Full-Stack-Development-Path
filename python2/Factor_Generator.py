'''
def factors(n):
    for k in range(1,n+1):
        if n % k == 0:
            yield k
    return 0

c =factors(100)
print(c)

for factors in factors(100):
    print(factors(100))

'''
def factor(n):
    while k*k <n:
        if n%k==0:
            yield k
            yield n //k
            k+=1
        if k*k == n:
            yield k

print(factor(100))
