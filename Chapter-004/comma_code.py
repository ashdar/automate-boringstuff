# .SYNOPSIS
# Writes a 'pretty' list with an oxford comma
#
# .NOTES
# I added the 'use oxford comma' parameter, for fun.
#


def format_comma_code(items, use_oxford_comma=False, debug=False):
    """Build a string from a list of times and make sure it has an 'and'
    Returns string."""

    if items == []:
        # FIXME: I do not think this is a great way to communicate 'something odd happened' to the caller.
        buff = '---noitems---'
        return(buff)
    else:
        buff = ''
        length_of_list = len(items)
        if (debug):
            print('Debug: debug is ' + str(debug))
            print('Debug: length_of_list is ' + str(length_of_list))
            print('Debug: use_oxford_comma is ' + str(use_oxford_comma))

        if length_of_list == 1:
            buff = items[length_of_list - 1]
        # elif length_of_list == 2:
        #     buff = l[length_of_list - 2] + ' and ' + l[length_of_list - 1]
        else:
            for i in range(length_of_list - 1):
                buff += items[i]
                if i != length_of_list - 2:
                    buff += ', '

            if use_oxford_comma:
                buff += ','

            buff += ' and ' + items[length_of_list - 1]
        # we want something like this:
        # 'apples, bananas, tofu, and cats'
        # 'apples and bananas'
        # 'apples'
        return(buff)


# main starts here =========
noList = []
goodList = ['apples', 'bananas', 'tofu', 'cats']
# goodList = ['apples', 'bananas', 'tofu']
doubleList = ['apples', 'bananas']
singleList = ['apples']


print('Test: No items')
print('The returned string is: ' + format_comma_code(noList))
print('')
print('Test: Four items')
print('The returned string is: ' + format_comma_code(goodList))
print('')
print('Test: Two items')
print('The returned string is: ' + format_comma_code(doubleList))
print('')
print('Test: A single item')
print('The returned string is: ' + format_comma_code(singleList))
print('')
print('Test: Four items, with an oxford comma')
print('The returned string is: ' +
      format_comma_code(goodList, use_oxford_comma=True))
# this is the same as just providing True in the correct location
# print('The returned string is: ' + format_comma_code(goodList, True))

# if you wanted some debugging output, you'd do this:
# print('The returned string is: ' + format_comma_code(goodList, True, debug=True))
