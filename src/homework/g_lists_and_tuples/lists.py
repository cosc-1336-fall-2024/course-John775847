def get_lowest_list_value_list(input_list):
    lowest_value = input_list[0]
    for index in range(len(input_list)):
        if (lowest_value > input_list[index]):
            lowest_value = input_list[index]
    return lowest_value

def get_highest_list_value_list(input_list):
    highest__value = input_list[0]
    for index in input_list:
        if (highest__value < index):
            highest__value = index
    return highest__value

# Demonstrating two ways to do the same thing. I believe the get_highest_list_value_list function is more "built-in" than the other.
