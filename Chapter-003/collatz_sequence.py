#.SYNOPSIS
# This is a practice project from the end of Chapter 3

def collatz(number):
    if number % 2 == 0:
        # even, means return whole number which is an int
        r = number // 2
    else:
        r = 3 * number + 1
    
    return(r)

### Main starts here =========
print('Enter an integer:')
choice = int(input())
fresh_choice = True
count_of_loops = 0
while (choice != 1 or fresh_choice):
    choice = collatz(choice)
    print(str(choice))
    fresh_choice = False
    count_of_loops += 1

print("You'll always arrive at 1, but it took {0} collatz(es) that time.".format(count_of_loops))