'''
h = ["Udacity", "Uello"]

for i in h:
    if "U" in h[0]:
        return h[i]

'''
def measure_Udacity(p):
    count = 0
    for i in p:
        if i[0] == "U":
            count = count +1
    return count

print (measure_Udacity(["Hdacity","UHello"]))
print (measure_Udacity(['Umika','Umberto']))
