#! python3
# regex_strip.py - Write a function that takes a string and does the same 
# thing as the strip() string method. 
# If no other arguments are passed other than the string to strip, then 
# whitespace characters will be removed from the beginning and end of the string. 
# Otherwise, the characters specified in the second argument to the function 
# will be removed from the string


# Notes
# \s is any whitespace character, including spactes, tables and newlines

import re

# FIXME: str is a dumb name. Think of a better one?
def RegExStrip(ToStrip, Pattern = None):

    buffer = 'INIT'

    # Note: use of pipe lets us tring the start and then end at the same exectuion
    # this is much cleaner than doing it twice, which was my first implementation.
    # the main difference between None and !None is that we use a default pattern

    if (Pattern == None):
        # use a default pattern
        _Pattern = '^[\s]*|[\s]*$'

    else:
        # use a patten based on what the caller passed to us.
        # I presume that the value of Pattern could be totally wierd and wrong,
        # leding to compile() valures.
        _Pattern = '^' + '[' + Pattern + ']*' + '|'+ '[' + Pattern + ']*$' 

    regEx = re.compile(_Pattern)
    buffer = regEx.sub('',ToStrip)

    return(buffer)


### Main ##########
print("Set #1:")
# this just strips spaces off the ends.
# spaces in the middle are left alone.
testCases = ['no removal', '  front removal', 'rear removal   ']
for testCase in testCases:
    print('->' + RegExStrip(testCase) + '<-')

print("Set #2:")
# this strips a few digits from the ends. 
# digits in the middle are left alone.
testCases = ['no rem0val', '423front rem0val', 'rear rem0val424']
for testCase in testCases:
    print('->' + RegExStrip(testCase, '024') + '<-')

print("Set #3:")
# this strips a few digits from the ends. 
# digits in the middle are left alone.
testCases = ['no rem0val', '423front rem0val', 'rear rem0val324']
for testCase in testCases:
    print('->' + RegExStrip(testCase, '\d') + '<-')
