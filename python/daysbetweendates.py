def nextDay(year, month,day):
    if day < 30:
        return year, month, day+1
    else:
        if month < 12:
            return year, month+1, 1
        else:
            return year+1,1,1


def dayIsBefore(year1,month1,day1,year2,month2,day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1<day2
    return False


def daysBetweenDates(year1,month1,day1,year2,month2,day2):

    assert not dayIsBefore(year2,month2,day2,year1,month1,day1)
    days = 0
    while dayIsBefore(year1,month1,day1,year2,month2,day2):
        year1 , month1, day1 = nextDay(year1, month1, day1)
        days = days +1

    return days



print (daysBetweenDates(2010,11,12,2012,11,12))
print (daysBetweenDates(1991,7,30,2017,4,2))
print (daysBetweenDates(2017,7,30,2017,4,2))