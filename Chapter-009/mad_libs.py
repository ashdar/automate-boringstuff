# mad_libs.py

import os
from pathlib import Path

inputFilePath = Path.cwd() / 'chapter-009' / 'mad_libs_input.txt'
outputFilePath = Path.cwd() / 'chapter-009' / 'mad_libs_output.txt'
print('Input path: ' + str(inputFilePath))
print('Output path: ' + str(outputFilePath))

# open the input file, read the contents and close the file

# inputFile = open('.\\mad_libs_input.txt')
inputFile = open(inputFilePath)
templateString = inputFile.read()
inputFile.close()

# get the works from user
adjectiveWord = "tasty"
nounWord = 'lamp'
adverbWord = 'slowly'
verbWord = 'pushed'

# Note that if there are two (or more) occurrences of a keyword, 
# the user will be asked for two (or more) words

# FIXME: this doesn't handle punctuation or multiple sentences. 
templateString = templateString.replace('.','')
outputString = ''
for i in templateString.split(' '):
    # print(i)
    # replace the words
    if (i == 'ADJECTIVE'):
        adjectiveWord = input('Enter an adjective:')
        outputString += adjectiveWord
    elif (i == 'NOUN'):
        nounWord = input('Enter a noun:')
        outputString += nounWord
    elif (i == 'ADVERB'):
        adverbWord = input('Enter an adverb:')
        outputString += adverbWord
    elif (i == 'VERB'):
        verbWord = input('Enter a verb:')
        outputString += verbWord
    else:
        outputString += i

    outputString += ' '

# trim the last space and add the final '.' period.
outputString = outputString[0:-1]
outputString += '.'

# print the string with replaced
print(outputString)

# open the output file, write the new string and close the file
outputFile = open(outputFilePath,'w')
outputFile.write(outputString)
outputFile.close()
