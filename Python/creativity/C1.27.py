def factors(n):
    k = 1
    temp = []
    while k * k < n:
        if n % k == 0:
            yield k
            temp.append(n // k)
        k += 1
    if k * k == n:
        yield k
    for i in reversed(temp):
        yield i
