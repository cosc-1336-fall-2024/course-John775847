def get_lowest_list_value_tuple(input_tuple):
    lowest_value = input_tuple[0]
    for index in range(len(input_tuple)):
        if (lowest_value > input_tuple[index]):
            lowest_value = input_tuple[index]
    return lowest_value

def get_highest_list_value_tuple(input_tuple):
    highest__value = input_tuple[0]
    for index in input_tuple:
        if (highest__value < index):
            highest__value = index
    return highest__value
