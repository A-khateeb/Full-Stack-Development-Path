import re

batbat = re.compile(r'Bat(mobile|man|bat|copter)')

mo = batbat.search("Batman and Wheel!")

print("The String found is :"+mo.group())

print(mo.groups(3))
