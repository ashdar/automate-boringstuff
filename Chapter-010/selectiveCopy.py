#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import shutil
import os
from pathlib import Path



def selectiveCopy(fileExtension, 
                sourceFolder,
                targetFolder,
                Verbose = True):

    # Back up the entire contents of "folder" into a ZIP file.

    sourceFolder = os.path.abspath(sourceFolder)   # make sure folder is absolute
    targetFolder = os.path.abspath(targetFolder)   # make sure folder is absolute

    if (Verbose):
        print("Verbose: Source Folder is => " + sourceFolder)
        print("Verbose: Target Folder is => " + targetFolder)
        print("Verbose: File Extension is => " + fileExtension)

    for foldername, subfolders, filenames in os.walk(sourceFolder):
        # print(f'Adding files in {foldername}...')
        for filename in filenames:
            if filename.endswith(fileExtension):
                sourceFileName = Path(foldername, filename)
                # print(f'Copying file -> {filename} to {targetFolder}...')
                print(f'Copying file -> {sourceFileName} to {targetFolder}...')
                shutil.copy(sourceFileName, targetFolder )
                # shutil.copy(sourceFolder / filename , targetFolder / filename)
            else:
                print(f'Skipping file -> {filename}')


    print('Done.')

# Main program starts here
selectiveCopy('.txt', '.\\delicious', '.\\delicious-target')
