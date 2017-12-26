def multiplier(n,m):
    if n%m == 0:
        return True
    else:
        return False

n = int(input("Insert the first value"))
m = int(input("Insert the second value"))
c = multiplier(n,m)
print("Return the result",c)
