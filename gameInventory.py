import os
import sys

# This is the file where you must work. Write code in the functions, create new functions,
# so they work according to the specification


# Displays the inventory.
def display_inventory(inventory):
    '''
    Prints out inventory or error message
        @param inventory dict The inventory of items and number of items
        @return void
    '''

    if type(inventory) is dict:
        if len(inventory) > 0:
            print('Inventory:')
            for item in inventory:
                print(inventory[item], str(item))
            print('Total number of items:', sum(inventory.values()))
        else:
            print('Empty inventory!')
    else:
        print('Input is not a dictionary!')


# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    '''
    Adds new items based on a list to the inventory (same items are grouped and sumed up between the 2 inputs)
        @param inventory dict Initial inventory
        @param added_items list List of items to be added to inventory
        @return dict The updated inventory
    '''

    if type(inventory) is dict and type(added_items) is list:
        if len(added_items) > 0:
            # create a dictionary from added_items list
            items_mod = {}
            for item in set(added_items):
                items_mod[str(item)] = added_items.count(item)
            # merge the 2 dictionaries
            for item in items_mod:
                inventory[str(item)] = inventory.get(item, 0) + items_mod[item]
    else:
        print('Inventory needs to be a dictionary, added items must be a list.')
        exit()

    return inventory


# Takes your inventory and displays it in a well-organized table with
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory)
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None):
    '''
    Prints inventory in a nice format. User can choose to see it in ascending, descending order or unordered.
        @param inventory dict The dictionary of items as keys and their numbers as values to be printed nicely.
        @param order string or None Order of items chosen by user: "count,desc", "count,asc" or None by default
        @return void
    '''

    if type(inventory) is dict:
        if len(inventory) > 0:

            # calculate table length
            key_length = 0
            key_length = max(max(map(len, inventory)), len('item name'))
            value_length = 0
            value_length = max(max([len(str(value)) for value in list(inventory.values())]), len('count'))
            total_length = 0
            total_length = key_length + value_length + 10

            # arrange items to be printed
            if order == 'count,desc':
                ordered_inv = [(key, inventory[key]) for key in sorted(inventory, key=inventory.get, reverse=True)]
            elif order == 'count,asc':
                ordered_inv = [(key, inventory[key]) for key in sorted(inventory, key=inventory.get, reverse=False)]
            else:
                ordered_inv = [(key, inventory[key]) for key in inventory]

            # print ordered inventory:

            # header
            print('Inventory:')
            print('count'.rjust(value_length + 5), 'item name'.rjust(key_length + 5), sep='')
            print('-' * total_length)

            # body
            for item, number in ordered_inv:
                print(str(number).rjust(value_length + 5), str(item).rjust(key_length + 5), sep='')

            # footer
            print('-' * total_length)
            print('Total number of items:', sum(inventory.values()))

        else:
            print('Empty inventory!')
    else:
        print('Inventory must be a dictionary.')


# Imports new inventory items from a file
# The filename comes as an argument, but by default it's
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename="import_inventory.csv"):
    '''
    Imports new inventory items from a file
        @param inventory dict The inventory to be imported into
        @param filename string Name of the from which items will be added to inventory
        @return dict New inventory containing all elements from original inventory and from file
    '''

    inventory_to_be = []

    # open file as read-only and convert first line to a list
    fullname = os.path.join(os.path.dirname(__file__), filename)
    try:
        with open(fullname, 'r', encoding='utf-8') as f:
            inventory_to_be = f.readlines()[0].strip().split(',')
    except:
        print('An error occured while opening the file.')
        exit()

    # add inventory_to_be items to inventory
    if type(inventory) is dict:
        if len(inventory_to_be) > 0:
            inventory = add_to_inventory(inventory, inventory_to_be)
    else:
        print('Inventory must be a dictionary.')
        exit()

    return inventory


# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text
# with comma separated values (CSV).
def export_inventory(inventory, filename="export_inventory.csv"):
    '''
    Exports the inventory into a .csv file.
        @param inventory dict The inventory of which items will be exported
        @param filename string Name of the file that will contain the exported items
        @return void
    '''

    inventory_to_export = []

    # make list from inventory (from dict)
    if type(inventory) is dict:
        if len(inventory) > 0:
            for key in inventory:
                inventory_to_export.extend([str(key)] * inventory[key])
        else:
            print('Empty inventory, nothing to print.')
            exit()
    else:
        print('Inventory is not a dictionary, cannot be printed.')
        exit()

    # write list to filename
    # fullname = os.path.join(os.path.dirname(__file__), filename)
    fullname = '/'.join([os.path.dirname(os.path.abspath(sys.argv[0])), filename])
    try:
        with open(fullname, "w", encoding='utf-8') as newfile:
            newfile.write(','.join(inventory_to_export))
    except:
        print('An error occured while trying to export inventory.')
        exit()


def main():
    '''
    Main function, contains logic to implement Game Inventory exercise
        @return void
    '''

    inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    display_inventory(inv)
    print('\n')

    inv = add_to_inventory(inv, dragon_loot)
    display_inventory(inv)
    print('\n')

    print_table(inv, order='count,desc')
    print('\n')

    inv = import_inventory(inv)
    print_table(inv, 'count,desc')
    export_inventory(inv)


if __name__ == '__main__':
    main()
