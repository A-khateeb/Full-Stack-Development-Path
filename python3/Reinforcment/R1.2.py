def is_even(n):
    if n%2 == 0:
        return True
    else:
        return False

c = int(input("Insert the value to check"))
r = is_even(c)
print(r)
