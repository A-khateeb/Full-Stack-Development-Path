cities = {
'Jerusalem':{'Population':500000,'State':'Palestine'},
'Cairo ':{'Population':1600000,'State':'Egypt'},
'Istanbul':{'Population':200000,'State':'Turkey'},
}
for city,info in cities.items():
    print("\nCity Name " + city)
    print("Information ")
    for a,b in info.items():
        print(str(a) +" " + str(b))
