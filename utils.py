""" utils.py
Helper functions.
"""

def find_by_name(name, items):
    """ Searches a list of items for an item with a name that matches the provided name.
    
    :param name (string): The name to search for.
    :param items (objects with object.name): The list of items to be searched.

    :returns the found item
    """

    for current_item in items:
        if current_item.name == name:
            return current_item
    
    return None