# Date Detection
# Write a regular expression that can detect dates in the DD/MM/YYYY format.
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

import unittest
import re


def ParseDate(StringToParse):
    """Detect dates formatted DD/MM/YYYY. This does not verify that they are actually dates.
    Returns [string] day, [string] month, [string] year """
    dd = 'dd'
    mm = 'mm'
    yyyy = 'yyyy'

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
    dd, mm, yyyy = mo.groups()
    return(dd, mm, yyyy)


def IsValidLeapYear(yyyy):
    """Takes a string with a four-digit year and checks to see if it is a leap year
    Returns boolean"""

    # Leap years are every year evenly divisible by 4,
    # except for years evenly divisible by 100,
    # unless the year is also evenly divisible by 400.
    #
    # IOW, per Wikipedia:
    # The years 1600, 2000 and 2400 are leap years,
    # while 1700, 1800, 1900, 2100, 2200 and 2300 are not leap years.

    # Most years are not leap years
    IsLeap = False
    
    # every 4 years is a leap year
    if (int(yyyy) % 4 == 0):
        IsLeap = True

        # the last day of the century is not a leap year
        if (int(yyyy) % 100 == 0):
            IsLeap = False

        # unless it's every fourth century
        if (int(yyyy) % 400 == 0):
            IsLeap = True

    return(IsLeap)


def IsValidDate(dd, mm, yyyy):
    """Finds if a dd, mm, yyyy comprise a valid date
    Returns boolean"""
    
    IsValid = False

    # April, June, September, and November have 30 days,
    # February has 28 days (plus leap year issues),
    # and the rest of the months have 31 days.

    # there is a case for each of the twelve months
    # If we are passed a ficticious thirteenth month, IsValid 
    # will remain false and that's what gets handed back to the caller
    if (mm in ['04', '06', '09', '11']):
        if (int(dd) >= 1 and int(dd) <= 30):
            IsValid = True
    elif (mm in ['02']):
        # leap years get 29 days in '02'
        if (IsValidLeapYear(yyyy)):
            if (int(dd) >= 1 and int(dd) <= 29):
                IsValid = True
        else:
            if (int(dd) >= 1 and int(dd) <= 28):
                IsValid = True
    elif (mm in ['01','03','05','07','08','10','12']):
        if (int(dd) >= 1 and int(dd) <= 31):
            IsValid = True

    return(IsValid)

### Main #########


class TestStringMethods(unittest.TestCase):


# FIXME: Split tests for ParseDate() and IsValidDate()
# Testing IsVAlidDate() is one thing. 
# Testing ParseDate is a different thing, even if you rely on IsValidDate() to check that you hav a good date.
    def test_ParseDate_Bad(self):
        testCases = [
            '31/02/2020', '31/04/2021'
        ]

        for i in testCases:
            with self.subTest(i=i):
                day, month, year = ParseDate(i)
                Is = IsValidDate(day, month, year)
                self.assertFalse(Is, "'{0}' is not a valid date".format(i))

    def test_LeapYear_Bad(self):
        testCases = [
            # in the far past
            1700, 1800, 1900
            # right about now
            , 2017, 2018, 2019, 2021, 2022, 2023
            # in the far future
            , 2100, 2200, 2300
        ]

        for i in testCases:
            with self.subTest(i=i):
                Is = IsValidLeapYear(i)
                self.assertFalse(
                    Is, "'{0}' is not a valid leap year".format(i))

    def test_ParseDate_Good(self):
        testCases = [
            '01/01/2020'            # This is a valid leap day
            , '29/02/2020'
        ]

        for i in testCases:
            with self.subTest(i=i):
                day, month, year = ParseDate(i)
                Is = IsValidDate(day, month, year)
                self.assertTrue(Is, "'{0}' is not a valid date".format(i))

    def test_LeapYear_Good(self):
        testCases = [
            # in the (distant?) paste
            1600, 2000      # in the past
            , 2016, 2020    # in the future
            , 2400
        ]

        for i in testCases:
            with self.subTest(i=i):
                Is = IsValidLeapYear(i)
                self.assertTrue(Is, "'{0}' is a valid leap year".format(i))
    

    def test_ValidDate_Bad(self):
        testCases = [
            # this has a bad month
            {'day' : 1, 'month' : 13, 'year' : 2020}            
            # this has a bad month
            ,{'day' : 1, 'month' : 0, 'year' : 2020}            
            # this has a bad day
            ,{'day' : 0, 'month' : 1, 'year' : 2020}            
            # this also has a bad day
            ,{'day' : 50, 'month' : 1, 'year' : 2020}            
            # This is NOT a valid leap day
            ,{'day' : 29, 'month' : 2, 'year' : 2021}            
            ]

        for i in testCases:
            with self.subTest(i=i):
                Is = IsValidDate(i['day'], i['month'], i['year'])
                self.assertFalse(Is, "'{0}/{1}/{2}' is not a valid date".format(i['day'], i['month'], i['year']))

    def test_ValidDate_Good(self):
        # !!!IsValidDate takes three strings, it doesn't work property against integer values!!!
        testCases = [
            # This is a valid leap day
            {'day' : '01', 'month' : '01', 'year' : '2020'}            
            ,{'day' : '29', 'month' : '02', 'year' : '2020'}            
            ]

        for i in testCases:
            with self.subTest(i=i):
                Is = IsValidDate(i['day'], i['month'], i['year'])
                self.assertTrue(Is, "'{0}/{1}/{2}' is a valid date".format(i['day'], i['month'], i['year']))
### Main #########

# To run this, with tests, from a command line in a pwsh shell:
# pushd chapter-007 ; python -m unittest -v  date_detection.py ; popd


if __name__ == '__main__':
    unittest.main()
