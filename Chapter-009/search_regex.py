# search_regex.py

# Write a program that opens all .txt files in a folder 
# and searches for any line that matches a user-supplied regular expression. 
# The results should be printed to the screen.

from pathlib import Path
import re
import os

searchDir = Path.cwd() / 'chapter-009'
# print(searchDir)

# print(list(searchDir.glob('*.txt')))

# regex = re.compile(r'([\d]{1,2})[\/]([\d]{1,2})[\/]([\d]{4})')
regex = re.compile(r'NOUN')

for filePath in searchDir.glob('*.txt'):
    print("Searching->" + os.path.basename(filePath))
    file = open(filePath)
    lineNumber = 1
    for line in file:
        lineNumber += 1
        mo = regex.search(line)
        if (mo):
            filePath
            print(os.path.basename(filePath) + '(' + str(lineNumber) + '): ' + line)
    file.close()