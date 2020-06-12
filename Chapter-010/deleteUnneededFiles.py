#! python3
# deleteUnneededFiles.py - deletes unneeded files.

import shutil
import os
from pathlib import Path



def deleteUnneededFiles( 
                folder,
                maxAllowableSize,
                Verbose = True):

    if (Verbose):
        print("Verbose: Folder is => " + folder)
        print("Verbose: maxAllowableSize is => " + str(maxAllowableSize))

    for foldername, subfolders, filenames in os.walk(folder):
        # print(f'Adding files in {foldername}...')
        for filename in filenames:
            fullFileName = Path(foldername, filename)
            fileSize = os.path.getsize(fullFileName)
            if (fileSize > maxAllowableSize):
                print(f'Whatif: File is {fileSize} bytes, deleting file -> {fullFileName}')
                # this is commented out for obvious reasons...
                # os.remove(fullFileName)
            else:
                if (Verbose):
                    print(f'Verbose: File is under {maxAllowableSize} bytes, skipping file -> {fullFileName}')

    print('Done.')

# Main program starts here
maxAllowableSize = 20
deleteUnneededFiles('.\\delicious', maxAllowableSize)
