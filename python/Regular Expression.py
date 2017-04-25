import re


phone_number_reg = re.compile(r'(\d\d\d-)\?\d\d\d-\d\d\d\d')
print("Please enter a Phone number")
mo = phone_number_reg.search(input())
print("The Phone number that is found is : "+mo.group())
print(mo.group(0))
print(mo.group(1))
#print(mo.group(2))
print(mo.groups())
###areacode , mainNumber , extention = mo.groups()
#print(areacode)
#print(mainNumber)
#print(extention)
###