import lists, tuples

def list_editor():
    option = 1
    user_list = []
    print("Create a list:")
    while (True):
        if (option == 1):
            print("Enter list number at index", len(user_list))
            user_list.append(int(input("")))
            if (len(user_list) > 3):
                option = int(input("Do you want to enter another value? \n1 Yes \n2 No \n[1 or 2]\n"))
        elif (option == 2):
            break
        else:
            print("You must pick [1 or 2]")
            option = int(input())
    return user_list

def main():
    first_question = True
    while (True):
        if (first_question == True):
            option = int(input("1 Show the list low /high values \n2 Exit \n[1 or 2]\n"))
            first_question = False
        if (option == 1):
            user_list = list_editor()
            print("Lowst value", lists.get_lowest_list_value_list(user_list))
            print("Lowst value", lists.get_highest_list_value_list(user_list))
            break
        elif (option == 2):
            break
        else:
            print("You must pick [1 or 2]")
            option = int(input())

if __name__ == '__main__':
    main()
