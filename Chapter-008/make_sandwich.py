# make_sandwich.py

# Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input, such as:

# Using inputMenu() for a bread type: wheat, white, or sourdough.
# Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
# Using inputYesNo() to ask if they want cheese.
# If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
# Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
# Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
# Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.

# Note
# The tricky part of this is thed data structures, and how to index into them.
#
# There is a rouding issue where the sandwich price can be 3.5500000000000003, when it should be 3.55
# There doesn't seem to be a native exact numeric type like currency or decimal()/numeric() in SQL. 
# there is probably a package for that, and that is beyond the scope of this problem.

import pyinputplus as pyip

def buildChoiceList(list, typeName):
    choices = []
    for i in list:
        if (i["typename"] == typeName):
            # print(i["typename"])
            # print(i["name"])
            # print(i["price"])
            choices.append(i["name"])
    return(choices)

def lookupIngredientPrice(list, typeName, name):
    price = None
    for i in list:
        if (i["typename"] == typeName):
            if (i["name"] == name):
                price = i["price"]

    return (price)

def describeSandwich(protein, bread, cheese, extras):

    if (cheese):
        s = "{0} sandwich on {1}, with {2}".format(protein, bread, cheese).capitalize()
    else:
        s = "{0} sandwich on {1}".format(protein, bread).capitalize()


    if (extras):
        s += ' - Extras: '
        for extra in extras:
            s += '{0}, '.format(extra) 

        # trip off the filnal ', ' two characters from the string
        s = s[0:-2]
    else:
        s += ' - Extras: None'

    return(s)

def calculateSandwichPrice(list, protein, bread, cheese, extras):

    price = 0.0
    price += lookupIngredientPrice(list, 'protein', protein) 
    price += lookupIngredientPrice(list, 'bread', bread)

    if (cheese):
        price += lookupIngredientPrice(list, 'cheese', cheese) 

    if (extras):
        for extra in extras:
            price += lookupIngredientPrice(list, 'extra', extra) 

    return(price)




### Main #########
ingredientList = [
    #protein
     {'typename' : 'protein', 'name' : 'chicken', 'price' : 1.00}            
    ,{'typename' : 'protein', 'name' : 'turkey', 'price' : 1.00}            
    ,{'typename' : 'protein', 'name' : 'ham', 'price' : 1.10}            
    ,{'typename' : 'protein', 'name' : 'tofu', 'price' : 0.90}            

    # bread
    ,{'typename' : 'bread', 'name' : 'wheat', 'price' : 1.10}            
    ,{'typename' : 'bread', 'name' : 'white', 'price' : 1.00}            
    ,{'typename' : 'bread', 'name' : 'sourdough', 'price' : 1.25}            

    # cheese
    ,{'typename' : 'cheese', 'name' : 'cheddar', 'price' : 0.25}            
    ,{'typename' : 'cheese', 'name' : 'swiss', 'price' : 0.25}            
    ,{'typename' : 'cheese', 'name' : 'mozzarella', 'price' : 0.25}            

    # extra
    ,{'typename' : 'extra', 'name' : 'mayo', 'price' : 0.10}            
    ,{'typename' : 'extra', 'name' : 'mustard', 'price' : 0.10}            
    ,{'typename' : 'extra', 'name' : 'lettuce', 'price' : 0.50}            
    ,{'typename' : 'extra', 'name' : 'tomato', 'price' : 0.50}            

    ]

# Chicken sandwich on wheat, with cheddar - Extras: mayo, mustard, lettuce, tomato
# price 2.35 + 1.20 = 3.55

# build the lists of choices
breadChoices = buildChoiceList(ingredientList, 'bread')
proteinChoices = buildChoiceList(ingredientList, 'protein')
cheeseChoices = buildChoiceList(ingredientList, 'cheese')

breadChoicePrompt = "What kind of bread would you like?"
proteinChoicePrompt = "What kind of protein would you like?"
cheesePrompt = "Do you want any cheese?"
cheeseChoicePrompt = "What kind of cheese would you like?"

breadChoice = None
proteinChoice = None
cheeseChoice = None

# breadChoice = pyip.inputMenu(prompt = breadChoicePrompt, breadChoices, numbered=True)
print(breadChoicePrompt)
breadChoice = pyip.inputMenu(breadChoices, numbered=True)

print(proteinChoicePrompt)
proteinChoice = pyip.inputMenu(proteinChoices, numbered=True)

print(cheesePrompt)
cheeseIncluded = pyip.inputYesNo()

if (cheeseIncluded == 'yes'):
    print(cheeseChoicePrompt)
    cheeseChoice = pyip.inputMenu(cheeseChoices, numbered=True)


# whata about extras?
# I feel like I need to do them one-by-one
extraChoices = []
for i in ingredientList:
    if (i["typename"] == 'extra'):
        prompt = 'Do you want {0}?'.format(i["name"])
        print(prompt)
        extraIncluded = pyip.inputYesNo()
        if (extraIncluded == 'yes'):
            extraChoices.append(i["name"])

# print(extras)

sandwichCountPrompt = "How many sandwiches would you like?"
print(sandwichCountPrompt)
sandwichCountChoice = pyip.inputInt(min=1) 

sandwichDescription = describeSandwich(proteinChoice, breadChoice, cheeseChoice, extraChoices)

sandwichPrice = calculateSandwichPrice(ingredientList, proteinChoice, breadChoice, cheeseChoice, extraChoices)

orderPrice = sandwichPrice * sandwichCountChoice

print(sandwichDescription)
print("Item Cost:  {0:6,.2f}".format(sandwichPrice))
print("Order Cost: {0:6,.2f}".format(orderPrice))

