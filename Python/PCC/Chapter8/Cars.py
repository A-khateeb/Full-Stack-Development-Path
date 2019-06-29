def make_car(model, manufacture, **addition):
    car_profile = {}
    car_profile["Model"] = model
    car_profile["Manufacture"] = manufacture
    for key, value in addition.items():
        car_profile[key]=value
    return car_profile

a = make_car('subaru','outback', color = 'blue', tow_package = True )
print(a)
