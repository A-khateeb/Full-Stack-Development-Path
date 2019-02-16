def isLeapYear(year):
    if year%400 == 0:
        return True
    if year%100 == 0:
        return False
    if year%4 == 0:
        return True
    return False 

def daysInMonth(year, month):
    if month==1 or month==3 or month==5 or month==7 \
     or month==8 or month==10 or month==12:
        return 31
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            else:
                return 28
        else:
            return 30



def dayIsBefore(year1,month1,day1,year2,month2,day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1< day2
    return False

def nextDay(year, month, day):
    if day < daysInMonth(year,month):
        return year, month, day+1
    else:
        if month < 12:
            return year, month+1, 1
        else:
            return year+1, 1,1

def daysBetweenDates(year1,month1,day1,year2,month2,day2):
    assert not dayIsBefore(year2,month2,day2,year1,month1,day1)
    days = 0
    while dayIsBefore(year1,month1,day1,year2,month2,day2):
        year1,month1,day1 = nextDay(year1,month1,day1)
        days = days+1
    return days


def test():
    assert daysBetweenDates(2013,1,1,2013,1,1)==0
    assert daysBetweenDates(2013,1,1,2013,1,2)== 1
    assert  nextDay(2013,1,1)==(2013,1,2)
    assert  nextDay(2014,12,31)==(2015,1,1)
    assert  nextDay(2015,1,31)==(2015,2,1)
    assert nextDay(2013,2,29) == (2013,3,1)
    assert nextDay(2013,9,31)==(2013,10,1)
    assert daysBetweenDates(2016,1,1,2016,12,31) == 365
    assert daysBetweenDates(2013,1,1,2013,12,31) == 364
    print ("We did it")
