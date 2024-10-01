import repetition

exit = False

while (exit==False):
    option = input("Would you like to get a factorial or add the sum of odd numbers? [F/S] ")
    if (option == "f" or option == "F"):
        number_to_factorial =  int(input("Enter a number "))
        print("Your answer is:", repetition.get_factorial(number_to_factorial))
        exit = True
    elif (option == "s" or option == "S"):
        number_to_add_odds = int(input("Enter a number "))
        print("Your answer is:", repetition.sum_odd_numbers(number_to_add_odds))
        exit = True
    else:
        print("Please type S or N ")
