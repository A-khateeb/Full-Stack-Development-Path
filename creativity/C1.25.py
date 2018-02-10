def removes(a):
    s = a.replace(',','')
    l = s.replace("'","")
    return l


r = "Let's talk about milk, "
p = removes(r)
print(p)
