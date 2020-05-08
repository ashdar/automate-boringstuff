# inventory.py

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print("{0}\t{1}".format(v,k))
        item_total += v

    print("Total number of items: " + str(item_total))

# first part of project
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
# displayInventory(stuff)

# second part of project
def addToInventory(inventory, addedItems):
    
    for item in addedItems:
        print(item)
        # this fails if an instance of the item doesn't exist in inventory
        # inventory[item] += 1

        # if we don't have an instance of this item yet, add it
        if (item not in inventory.keys()):
             inventory[item]=0


        inventory[item] += 1

    return(inventory)

### Main #########
inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(inv)
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)