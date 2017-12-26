def factor(n):
    result = []
    for k in range(1,n+1):
        if n%k == 0:
            result.append(k)
    return result

print(factor(100))
print(factor(1000))
print(factor(20))
print(factor(7))
