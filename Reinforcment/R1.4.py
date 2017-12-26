def SumSquare(k):
    assert k >0 
    return sum(x**2 for x in range(k))
k = input("Please insert the number")
print("The SQR is {}".format(SumSquare(int(k))))
