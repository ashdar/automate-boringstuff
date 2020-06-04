#!python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcb.pyw list - Loads all keywords to clipboard.
#
#        FIXME: Add this for the end-of-chapter exercise
#        py.exe mcb.pyw delete <keyword> - Deletes keyword from stored keywords
import pyperclip
import sys
import shelve

Verbose = True

mcbShelf = shelve.open('.\\chapter-009\\mcb')

# remember, argv is zero based. with the first item being the name of the program
# print(sys.argv[0])

if len(sys.argv) >= 4:
    if (Verbose):
        print('Verbose: This program does not understand more than two arguments. Ever.')
elif len(sys.argv) == 3:
    if (sys.argv[1].lower() == 'save'):
        # Save clipboard content.
        mcbShelf[sys.argv[2]] = pyperclip.paste()
        print('Verbose: Keyword ' + sys.argv[2] + ' copied from clipboard to shelf')
    elif (sys.argv[1].lower() == 'delete'):
        # Save clipboard content.
        del mcbShelf[sys.argv[2]]
        if (Verbose):
            print('Verbose: Keyword ' + sys.argv[2] + ' deleted from shelf')
    else:
        if (Verbose):
            print('Verbose: Two Argument Syntax error?')

elif len(sys.argv) == 2:
    # TODO: List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        if (Verbose):
            print('Verbose: List copied to clipboard: ' + str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        if (Verbose):
            print('Verbose: Keyword ' + sys.argv[1] + ' copied from shelf to clipboard')
    else:
        if (Verbose):
            print('Verbose: One Argument Syntax error?')


mcbShelf.close()


# Here are the remnants of the first clip program, from an earlier chapter.
# TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
#         'busy': """Sorry, can we do this later this week or next week?""",
#         'upsell': """Would you consider making this a monthly donation?"""}
#
# 
# if len(sys.argv) < 2:
#     print('Usage python mclip.py [keyphrase] -copy phrase text to clipboard')
#     sys.exit()

# # the first command line arg is the phrase
# keyphrase = sys.argv[1]


# if keyphrase in TEXT:
#     pyperclip.copy(TEXT[keyphrase])
#     print('Text for \'' + keyphrase + '\' copied to clipboard.')
# else:
#     print('There is no text for \'' + keyphrase + '\'')
