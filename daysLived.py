# Credit goes to Websten from forums
# This is a question from Udacity lesson 2.5 intro into computer science
# That I solved. 
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.
def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    if year % 100 == 0 and year % 400 == 0:
        return True
    else:
        return False
    
def daysInMonth(month, year):
    i = 0
    if(month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12):
        i = 31
        return i
    if isLeapYear(year) == False:
        if month == 2:
            i = 28
            return i
        else:
            i = 30
            return i
    if isLeapYear(year) == True:
        if month == 2:
            i = 29
            return i
        else:
            i = 30
            return i
#print daysInMonth(5, 2001)


#print isLeapYear(1900)
           
def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    count = daysInMonth(month, year)
    while(count == 30):
        if day < 30:
            return year, month, day + 1
        else:
            return year, month + 1, 1
    while(count == 28):
        if day < 28:
            return year, month, day + 1
        else:
            return year, month + 1, 1   #month + 1
    while(count == 29):
        if day < 29:
            return year, month, day + 1
        else:
            return year, month + 1, 1 #month + 1
    while(count == 31):
        if day < 31:
            return year, month, day + 1
        else:
            if month == 12:
                return year + 1, 1, 1
            else:
                return year, month + 1, 1
#print nextDay(2012, 4, 30)
                
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days
print daysBetweenDates(1989, 7, 12, 2016, 8, 3)
#print daysBetweenDates(2012, 1, 1, 2012, 2, 28)
#print daysBetweenDates(1900,1,1,1999,12,31)
#print daysBetweenDates(2011,6,30,2012,6,30)
#print daysBetweenDates(1900,1,1,1999,12,31)
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

#test()
