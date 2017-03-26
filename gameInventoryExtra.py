# Adds to the inventory dictionary a list of items from added_items. Alternative way.
def add_to_inventory(inventory, added_items):
    '''
    Adds new items based on a list to the inventory (same items are grouped and sumed up between the 2 inputs)
        @param inventory dict Initial inventory
        @param added_items list List of items to be added to inventory
        @return dict The updated inventory
    '''
    if type(inventory) is dict and type(added_items) is list:
        if len(added_items) > 0:
            # create a dictionary from added_items
            items_mod = {}
            for item in set(added_items):
                items_mod[item] = added_items.count(item)
            # merge the 2 dictionaries
            updated_inventory = {
                key: inventory.get(key, 0) + items_mod.get(key, 0) for key in set(inventory) | set(items_mod)
            }
        else:
            updated_inventory = inventory
    else:
        print('Inventory needs to be a dictionary, added items must be a list.')
        exit()
    return updated_inventory
