import dictionary, sets

def main():
    option = int(input("1-Add or Update Item \n2-Delete Item \n3-Exit \n"))
    user_dictionary = {}
    while(True):
        if option == 1:
            dictionary.add_inventory(user_dictionary, "Widget" + input("Widget number "), int(input("Widget value ")))
            option = int(input("1-Add or Update Item \n2-Delete Item \n3-Exit \n"))
        elif option == 2:
            dictionary.remove_inventory_widget(user_dictionary, "Widget" + input("Widget number "))
            option = int(input("1-Add or Update Item \n2-Delete Item \n3-Exit \n"))
        elif option == 3:
            break
        else:
            option = int(input("You must pick [1, 2, 3] "))

if __name__ == '__main__':
    main()

