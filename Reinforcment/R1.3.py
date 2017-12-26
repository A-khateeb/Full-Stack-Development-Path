def minmax(data):
    dMin = dMax = data[0]
    for a in data[1:]:
        if(a<dMin):
            dMin = a
        elif(a>dMax):
            dMax = a

    return dMin, dMax
if __name__ == '__main__':
    dataset = input("Please insert the data\n")
    data = [float(d) for d in dataset.split()]
    datamax= minmax(data)
    print("min:{}, max:{}".format(datamax[0],datamax[1]))
