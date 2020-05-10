# table_printer
# the catch here is that the data needs to be 'rotated' for the report.
# you find the longest string in a row and then use that (plus one) aa the wdith for the column

#    apples Alice  dogs
#   oranges   Bob  cats
#  cherries Carol moose
#    banana David goose

def findLongestInList(l):

    longestLength = 0
    for s in l:
        if len(s) > longestLength:
            longestLength = len(s)
    return(longestLength)


def printTable(tableData):
    # table is a list of lists  of strings
    # craete a list to hold the lenght of the long string in each list.
    colWidths = [0] * len(tableData)

    reportWidth = len(tableData)
    reportHeight = len(tableData[0])
    # print("Report Width: {0}, Height: {1}".format(reportWidth, reportHeight))

    for i in range(len(tableData)):
        # print (findLongestInList(tableData[i]))
        colWidths[i] = findLongestInList(tableData[i])
        # print (str(colWidths[i]))

    for i in range(reportHeight):
        for j in range(reportWidth):
            # print("{0},{1}".format(i, j))
            # do not forget the + 1 fudge factor
            print(tableData[j][i].rjust(colWidths[j] + 1), end='')

        # need a carriage return
        print()
    return(0)

### Main ################################
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)

    