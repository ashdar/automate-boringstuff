#!python3
# mclip.py - a mulit-clipboard program



TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}


# print(TEXT)

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage python mclip.py [keyphrase] -copy phrase text to clipboard')
    sys.exit()

# the first command line arg is the phrase
keyphrase = sys.argv[1] 


if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for \'' + keyphrase + '\' copied to clipboard.')
else:
    print('There is no text for \'' + keyphrase + '\'')