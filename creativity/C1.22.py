def product_count(a,b):
    #assert len(a) == len(b)
    return [a[n]*b[n] for n in range(len(a))]

try:
    a = [ l for l in range(6)]
    b = [ m for m in range(5)]
    o = product_count(a,b)
    print(o)
except IndexError:
    print("Don’t try buffer overflow attacks in Python!")
