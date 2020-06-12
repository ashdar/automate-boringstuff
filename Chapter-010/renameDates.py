#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import shutil
import os
import re
from pathlib import Path

WhatIf = True
Verbose = False

# print("cwd: " + str(Path.cwd()))

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?) # all text before the date
       ((0|1)?\d)-                     # one or two digits for the month
       ((0|1|2|3)?\d)-                 # one or two digits for the day
       ((19|20)\d\d)                   # four digits for the year
       (.*?)$                          # all text after the date
       """, re.VERBOSE)

#  Loop over the files in the working directory.

for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # Skip files without a date.
    if mo == None:
        continue

    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    if (Verbose):
        print(f'Verbose:BeforePart:' + beforePart)

    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + \
        monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    if (WhatIf):
        print(f'Whatif: Rename "{amerFilename}" to "{euroFilename}"')
    else:
        # Rename the files.
        print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
        # shutil.move(amerFilename, euroFilename)   # uncomment after testing



