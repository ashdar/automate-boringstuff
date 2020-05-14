#! python3
# strong_password_detection.py - Uses regular expressions to make sure the password string it is passed is strong

# Strong Password Detection
# Write a function that uses regular expressions to make sure the password 
# string it is passed is strong. 
# 
# A strong password is defined as one that 
#   1. Is at least eight characters long
#   2. contains both uppercase and lowercase characters
#   3. has at least one digit. 
# You may need to test the string against multiple regex patterns to validate its strength.

### Tool functions #########
import inspect
def WriteVerbose(Verbose, Message):
    """Mimic Powershell Write-Verbose
    Returns None"""

    if (Verbose):
        print(str(inspect.stack()[1].function) + ':' + Message)


import re
def IsStrongPassword (pwd, Verbose = False):
    '''Uses regular expressions to make sure the password string it is passed is strong
    Returns boolena'''

    IsStrong = False

    # A strong password is defined as one that 
    #   1. Is at least eight characters long
    #   2. contains both uppercase and lowercase characters
    #   3. has at least one digit. 

    AcceptableLength = 8

    # match 8 or more of any word character. 'word' characters include digits
    regexLength = re.compile('\w{8,}')
    regexLower = re.compile('[a-z]')
    regexUpper = re.compile('[A-Z]')
    regexDigit = re.compile('[0-9]')

    # using len() isn't really in the spirit of this exercize, so...
    # if (len(pwd) >= AcceptableLength):
    mo = regexLength.search(pwd)
    if (mo != None):
        Message = 'Password is an acceptable length.'
        WriteVerbose(Verbose, Message)

        mo = regexLower.search(pwd)
        if (mo != None):
            Message = 'Password has one or more lower case characters.'
            WriteVerbose(Verbose, Message)

            mo = regexUpper.search(pwd)
            if (mo != None):
                Message = 'Password has one or more upper case characters.'
                WriteVerbose(Verbose, Message)

                # third test is 1 ore more digits
                mo = regexDigit.search(pwd)
                if (mo != None):
                    Message = 'Password has one or more digit characters.'
                    WriteVerbose(Verbose, Message)
                    IsStrong = True
                else:
                    Message = 'Password has no digit characters.'
                    WriteVerbose(Verbose, Message)
            else:
                Message = 'Password has no upper case characters.'
                WriteVerbose(Verbose, Message)
        else:
            Message = 'Password has no lower case characters.'
            WriteVerbose(Verbose, Message)
    else:
        Message = 'FAILS:Password is less than {0} characters long.'.format(AcceptableLength)
        WriteVerbose(Verbose, Message)


    return (IsStrong)
### main starts here #########
# newPassword = input()
newPasswords = ['2short','LONGENOUGH','longenough','longENUFF','zer0ENUFF']
for newPassword in newPasswords:
    # print('Password Under Test->{0}<-'.format(newPassword))
    IsStrong = IsStrongPassword(newPassword)
    if (IsStrong):
        print('Password Under Test->{0}<- is strong.'.format(newPassword))
    else:
        print('Password Under Test->{0}<- is weak.'.format(newPassword))
    