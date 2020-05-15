#Date Detection
#Write a regular expression that can detect dates in the DD/MM/YYYY format. 
# Assume that the days range from 01 to 31, 
# the months range from 01 to 12, and 
# the years range from 1000 to 2999. 
# Note that if the day or month is a single digit, it’ll have a leading zero.

# The regular expression doesn’t have to detect correct days for each month 
# or for leap years; it will accept nonexistent dates like 31/02/2020 or 31/04/2021.
#  
# Then store these strings into variables named month, day, and year, and 
# write additional code that can detect if it is a valid date. 
#
# April, June, September, and November have 30 days, 
#
# February has 28 days, and the rest of the months have 31 days. 
#
# February has 29 days in leap years. Leap years are every year evenly divisible by 4, 
# except for years evenly divisible by 100, unless the year is also evenly divisible by 400. 
#
# The book says:
# Note how this calculation makes it impossible to make a reasonably sized regular 
# expression that can detect a valid date.
# 
# This seems questionable. See https://www.regular-expressions.info/dates.html
# which gets a good deal closer than what we do here. At a minimum, their solution 
# would reduce false-positives that would need to be weeded out.

import re

def ParseDate(StringToParse):
    """Detect dates formatted DD/MM/YYYY. This does not verify that they are actually dates.
    Returns [string] day, [string] month, [string] year """
    dd='dd'
    mm='mm'
    yyyy='yyyy'


    # This regex finds three groups.
    # Working this out was a PITA. I used regex101.com to troubleshoot.
    # I skimmed this 
    # https://www.regular-expressions.info/dates.html
    # note there is a specific line for dd-mm-yyyy near the bottom of the page.
    # the key things from reading that were:
    #   1. Their solution limits months, days and years to a much smaller range than my requirements do
    #   2. I should be grouping my slashes in a [] list
    #   3. regex101.com helped me realize that I my parenthesization for the 2nd group was wrong:
    #       a. ([\d]){1,2} is wrong
    #       a. ([\d]{1,2}) is correct

    # regex = re.compile(r'([\d]{1,2})')
    # regex = re.compile(r'([\d]{1,2})[\/]([\d]){1,2}')
    # regex = re.compile(r'([\d]{1,2})[\/]([\d]{1,2})')
    regex = re.compile(r'([\d]{1,2})[\/]([\d]{1,2})[\/]([\d]{4})')
    mo = regex.search(StringToParse)

    # this would work OK, but the line I actually use seems cleaner (to me)
    # dd = mo.group(1)
    # mm = mo.group(2)
    # yyyy = mo.group(3)

    # this line assigns each of the three groups to variables, 
    # which is just a conveniance to return them with the obvious syntax
    dd,mm,yyyy = mo.groups()
    return(dd, mm, yyyy)

def IsLeapYear(yyyy):
    """Takes a string with a four-digit year and checks to see if it is a leap year
    Returns boolean"""

    IsLeap = False
    # Leap years are every year evenly divisible by 4, 
    # except for years evenly divisible by 100, 
    # unless the year is also evenly divisible by 400. 
    # 
    # IOW, per Wikipedia:
    # The years 1600, 2000 and 2400 are leap years, 
    # while 1700, 1800, 1900, 2100, 2200 and 2300 are not leap years.


    if (int(yyyy) % 4 == 0):
        # if (int(yyyy) % 100 != 0):
        #     if (int(yyyy) % 400 == 0):
        IsLeap = True

    return(IsLeap)

def IsValidDate(dd,mm,yyyy):

    IsValid = False
    
    # April, June, September, and November have 30 days, 
    #
    # February has 28 days (plus leap year issues), 
    # 
    # and the rest of the months have 31 days. 
    if  (mm in ['04','06','09','11']):
        if (int(dd) <= 30):
            IsValid = True
    elif (mm in ['02']):
        # FIXME: leap years
        if (int(dd) <= 28):
            IsValid = True
    else:
        if (int(dd) <= 31):
            IsValid = True

    return(IsValid)

### Main #########

testCasesForGoodLeapYears = [1600, 2000, 2016, 2020, 2400]
testCasesForBadLeapYears = [1700, 1800, 1900, 2019, 2100, 2200, 2300]

print('Test #1: Leap Years')
for i in testCasesForGoodLeapYears:
# for i in range(1995,2015):
    Is = IsLeapYear(str(i))
    if (Is):
        print('{0} is a leap year.'.format(i))
    else:
        print('{0} is not a leap year.'.format(i))

print('Test #2: Not leap years')
for i in testCasesForBadLeapYears:
# for i in range(1995,2015):
    Is = IsLeapYear(str(i))
    if (Is == False):
        print('{0} is a leap year.'.format(i))
    else:
        print('{0} is not a leap year.'.format(i))


testCasesForBadDates = [
    '31/02/2020','31/04/2021'
    ]

testCasesForGoodDates = [
    '01/01/2020','29/02/2020'
    ]

testCasesForGoodLeapYearDates = [
    '29/02/2020'
    ]
testCasesForGoodLeapYearDates = [
    '29/02/2020'
    ]


print('Test #3')
# for tc in testCasesForBadDates:
#     day, month, year = ParseDate(tc)
#     print (month, day, year)

    # is that a valid date? 
