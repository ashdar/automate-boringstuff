# .SYSOPSIS
#  One of the practice projects near the end of Chapter 4.
#
# .LINK
# https://automatetheboringstuff.com/2e/chapter4/
# this points to the chapter that contains this exercise 

import copy

# I added another column here, on the extreme left, all characters are '.'
# this makes the otput look a little cleaner
grid = [['.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', 'O', 'O', '.', '.', '.'],
        ['.', 'O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O', '.'],
        ['.', '.', 'O', 'O', 'O', 'O', 'O'],
        ['.', 'O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', '.', '.'],
        ['.', '.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.']]

# Requirement #1 Copy the grid
gridCopy = copy.copy(grid)

# Requirement #2: Print the image. 
# The web page shows the image rotated, though the text doesn't make this clear
height = len(gridCopy)
width = len(gridCopy[0])

# this was just for debugging
# print(height) # 9
# print(width) # 7
# print(gridCopy[0][0])

# we print the grid, 'rotated' 270 degrees
for i in range(width):
    for j in range(height):
        print(gridCopy[j][i], end='')
    # move down to the next line
    print()
