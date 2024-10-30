import dictionary, sets

def list_editor():
    option = 1
    user_list = []
    while (True):
        if (option == 1):
            print("Enter letter at index", len(user_list))
            user_list.append(input(""))
            if (len(user_list) > 3):
                option = int(input("Do you want to enter another value? \n1 Yes \n2 No \n[1 or 2]\n"))
        elif (option == 2):
            break
        else:
            option = int(input("You must select [1 or 2] \n"))
    return user_list

def matrix_editor():
    option = 1
    user_matrix = []
    while (True):
        if (option == 1):
            print("Create list", len(user_matrix))
            user_matrix.append(list_editor())
            if (len(user_matrix) > 3):
                option = int(input("Do you want to create another list? \n1 Yes \n2 No \n[1 or 2]\n"))
        elif (option == 2):
            break
        else:
            option = int(input("You must select [1 or 2] \n"))
    return user_matrix

def main():
    firt_question = True
    while(True):
        if (firt_question == True):
            option = int(input("1 Get p distance matrix \n2 Exit \n[1 or 2] \n"))
            firt_question = False

        if (option == 1):
            user_matrix = matrix_editor()
            p_distance_matrix = dictionary.get_p_distance_matrix(user_matrix)
            print("user matrix", user_matrix)
            print("p distance matrix", p_distance_matrix)
            break
        elif (option == 2):
            break
        else:
            option = int(input("You must select [1 or 2] \n"))

if __name__ == '__main__':
    main()

