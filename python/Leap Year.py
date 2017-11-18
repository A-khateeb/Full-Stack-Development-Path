def is_leap_baby(day,month,year):
    if day == 29 and month == 2:

        if year%4 !=0:
            return False

        elif year%100 !=0:
            return  True

        elif year%400 !=0:
            return False

        else:
            return True
    else:
        return False



def output(status,name):
    if status:
        print("%s is one of an extremely rare species. He is a leap year baby!" % name)
    else:
        print ("There's nothing special about %s's birthday. He is not a leap year baby!" % name)


output(is_leap_baby(29, 2, 1996), 'Calvin')

output(is_leap_baby(19, 6, 1978), 'Garfield')
#>>>There's nothing special about Garfield's birthday. He is not a leap year baby!

output(is_leap_baby(29, 2, 2000), 'Hobbes')
#>>>Hobbes is one of an extremely rare species. He is a leap year baby!

output(is_leap_baby(29, 2, 1900), 'Charlie Brown')
#>>>There's nothing special about Charlie Brown's birthday. He is not a leap year baby!

output(is_leap_baby(28, 2, 1976), 'Odie')
#>>>There's nothing special about Odie's birthday. He is not a leap year baby!