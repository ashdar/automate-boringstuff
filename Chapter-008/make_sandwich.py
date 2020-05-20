# make_sandwich.py

# Write a program that asks users for their sandwich preferences. The program should use PyInputPlus to ensure that they enter valid input, such as:

# Using inputMenu() for a bread type: wheat, white, or sourdough.
# Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
# Using inputYesNo() to ask if they want cheese.
# If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or mozzarella.
# Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
# Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
# Come up with prices for each of these options, and have your program display a total cost after the user enters their selection.

import pyinputplus as pyip

ingredientList = [
    # bread
    {'typename' : 'bread', 'name' : 'wheat', 'price' : 1.10, 'include':False}            
    ,{'typename' : 'bread', 'name' : 'white', 'price' : 1.00, 'include':False}            
    ,{'typename' : 'bread', 'name' : 'sourdough', 'price' : 1.25, 'include':False}            
    #protein
    ,{'typename' : 'protein', 'name' : 'chicken', 'price' : 1.00, 'include':False}            
    ,{'typename' : 'protein', 'name' : 'turkey', 'price' : 1.00, 'include':False}            
    ,{'typename' : 'protein', 'name' : 'ham', 'price' : 1.10, 'include':False}            
    ,{'typename' : 'protein', 'name' : 'tofu', 'price' : 0.90, 'include':False}            
    # cheese
    ,{'typename' : 'cheese', 'name' : 'cheddar', 'price' : 0.25, 'include':False}            
    ,{'typename' : 'cheese', 'name' : 'swiss', 'price' : 0.25, 'include':False}            
    ,{'typename' : 'cheese', 'name' : 'mozzarella', 'price' : 0.25, 'include':False}            

    # extra
    ,{'typename' : 'extra', 'name' : 'mayo', 'price' : 0.10, 'include':False}            
    ,{'typename' : 'extra', 'name' : 'mustard', 'price' : 0.10, 'include':False}            
    ,{'typename' : 'extra', 'name' : 'lettuce', 'price' : 0.50, 'include':False}            
    ,{'typename' : 'extra', 'name' : 'tomato', 'price' : 0.50, 'include':False}            

    ]

countOfSandwich = 0

# fixme: this is a dumb way to provide the set of choices. 
# I should pull them out of the data structure, that means rotating the stucture a bit.
breadChoices = ['wheat', 'white', 'sourdough']
proteinChoices = ['chicken', 'turkey', 'ham', 'tofu']
cheeseChoices = ['cheddar','swiss','mozarella']


breadChoicePrompt = "What kind of bread would you like?"
proteinChoicePrompt = "What kind of protein would you like?"
cheesePrompt = "Do you want any cheese?"
cheeseChoicePrompt = "What kind of cheese would you like?"


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
else:
    cheeseChoice = None


# print(cheeseIncluded)

print(breadChoice)
print(proteinChoice)
print(cheeseIncluded)
print(cheeseChoice)



