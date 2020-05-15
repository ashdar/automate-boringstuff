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
        #     if (int(yyyy) % 400 == 0):
        IsLeap = True

        if (int(yyyy) % 100 == 0):
            IsLeap = False

        if (int(yyyy) % 400 == 0):
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
        # leap years get 29 days in '02'
        if (IsLeapYear(yyyy)):
            if (int(dd) <= 29):
                IsValid = True
        else: 
            if (int(dd) <= 28):
                IsValid = True
    else:
        if (int(dd) <= 31):
            IsValid = True

    return(IsValid)

### Main #########

testCasesForLeapYears = [
    1600, 2000, 2400
    , 2016,2020
    ]
testCasesForNotLeapYears = [
    1700, 1800, 1900, 2100, 2200, 2300
    , 2017, 2018, 2019
    ]

# print('Test #0: Leap Years')

# i = 2019
# Is = IsLeapYear(str(i))
# if (Is):
#     print('{0} is a leap year.'.format(i))
# else:
#     print('{0} is not a leap year.'.format(i))

# print('Test #1: Leap Years')
# for i in testCasesForLeapYears:
# # for i in range(1995,2015):
#     Is = IsLeapYear(str(i))
#     if (Is):
#         print('Test OK:{0} is a leap year.'.format(i))
#     else:
#         print('Test FAIL:{0} is not a leap year.'.format(i))

# print('Test #2: Not leap years')
# for i in testCasesForNotLeapYears:
# # for i in range(1995,2015):
#     Is = IsLeapYear(str(i))
#     if (Is == False):
#         print('Test OK:{0} is not a leap year.'.format(i))
#     else:
#         print('Test FAIL:{0} is a leap year.'.format(i))


# testCasesForBadDates = [
#     '31/02/2020','31/04/2021'
#     ]

testCasesForGoodDates = [
    '01/01/2020','29/02/2020'
    ]

testCasesForGoodLeapYearDates = [
    '29/02/2020'
    ]
testCasesForGoodLeapYearDates = [
    '29/02/2020'
    ]


# print('Test #3: testCasesForBadDates: Not a valid date')
# for i in testCasesForBadDates:
#     day, month, year = ParseDate(i)
#     # print (month, day, year)
#     Is = IsValidDate(day, month, year)
#     if (Is == False):
#         print('Test OK:{0} is not a valid date.'.format(i))
#     else:
#         print('Test FAIL:{0} is a valid date.'.format(i))

    # is that a valid date? 

import unittest

# FIXME: I am in the middle of trying to convert this to test cases/clases


class TestStringMethods(unittest.TestCase):

    def test_ForBadDates(self):
        testCasesForBadDates = [
            '31/02/2020','31/04/2021'
            ,'13/13/2020'
            ]

        for i in testCasesForBadDates:
            with self.subTest(i=i):
                day, month, year = ParseDate(i)
                Is = IsValidDate(day, month, year)
                self.assertFalse(Is, "'{0}' is not a valid date".format(i))

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
