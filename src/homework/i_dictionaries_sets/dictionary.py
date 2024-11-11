def add_inventory(dictionary, in_key, in_value):
    print("meeow", in_key)
    if in_key in dictionary:
        dictionary[in_key] += in_value
    else:
        dictionary[in_key] = in_value

    return dictionary

def remove_inventory_widget(dictionary, in_key):
    if in_key in dictionary:
        del dictionary[in_key]
        print("Item Deleted")
    else:
        print("Item Not Found")
    return dictionary
