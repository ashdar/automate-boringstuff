#! python3
# fillInTheGaps.py - renames files to match a sequence

# format of the names of the files will be:
# spam-00.txt
# where 000 will be a number left-padded with zeros

import shutil
import os
from pathlib import Path
import glob


Verbose = True 

prefix = 'spam'
extension = '.txt'

# Make it easy on myself, just move to the dir with the test files
# print(os.getcwd())
os.chdir(".\\Chapter-010\\FillInTheGapsTestFiles")
# print(os.getcwd())

# this probably isn't hte best algorthm, but it works OK
# Fixme: I am not going to go above and beyond to implment the 'insert'
# functionality that is mentioned in the problem.

for i in range(1,100):
    # print(i)
    # iAsString = f'{i:03}'

    iTrialFileName = prefix + '-' + f'{i:02}' + extension
    
    # if (Verbose):
    #     print('Verbose: Trying ' + iTrialFileName)

    if (os.path.isfile(iTrialFileName) ):
        if (Verbose):
            print('Verbose: File ' + iTrialFileName + ' exists.')
    else:
       if (Verbose):
            print('Verbose: File ' + iTrialFileName + ' does NOT exist.')
            files = glob.glob(prefix + '-*' + extension)
            # print(files)
            for file in files:
                # print(file)
                if (file > iTrialFileName):
                    print('Renaming ' + file + ' to ' + iTrialFileName)
                    shutil.move(file, iTrialFileName)
                    break # should take us to the next loop
                else:
                    if (Verbose):
                        print('Verbose: ' + file + ' is already named/sequenced correctly')


        # find the first file witha a matching name > iTrialFileName 
        # rename that file. 
        # restart the loop


