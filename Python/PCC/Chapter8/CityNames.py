def city_name(city , country):
    re =  '"' + city + ', ' + country + '"'
    return re

l = city_name('Jerusalem' , 'Palestine')
print(l)
l = city_name('Amman' , 'Jordan')
print(l)
l = city_name('Istanbul' , 'Turkey')
print(l)
