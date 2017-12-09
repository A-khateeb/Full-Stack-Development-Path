def containers(datas, targets):
    for items in datas:
        if items == targets:
            print(targets)
            print("Hit")
        return True
    return False

dataset = [2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9,2,3,4,5,6,7,8,9]
containers(dataset,1)
