#! python3
# backupToZip.py - Copies an entire folder and its contents into
# a ZIP file whose filename increments.

import zipfile
import os


def backupToZip(folder,
                Verbose=True):

    # Back up the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder)   # make sure folder is absolute

    if (Verbose):
        print("Verbose: Source of backup is => " + folder)

    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    if (Verbose):
        print("Verbose: Zipfile name is => " + zipFilename)

    # Create the ZIP file.
    print(f'Creating {zipFilename}...')
    backupZip = zipfile.ZipFile(zipFilename, 'w')


    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')

        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            print(f'Adding file {filename}...')
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue   # don't back up the backup ZIP files

            backupZip.write(os.path.join(foldername, filename))

    backupZip.close()

    print('Done.')

# Main program starts here
backupToZip('.\\delicious')
