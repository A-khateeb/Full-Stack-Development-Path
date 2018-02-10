def distint(data):
    lenDist= len(data)
    setDist = len(set(data))
    if setDist == lenDist :
        return True
    else:
        return False

da = [1,2,3,4,5,6,7,7]
print(distint(da))

da1 = [1,2,3,4,5,6,7]
print(distint(da1))
