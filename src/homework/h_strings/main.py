import strings

def main():
    exit = False
    first_run = True
    while (exit != True):

        if (first_run == True):
            print("Choose one:")
            print("1-Hamming Distance")
            print("2-Dna Complement")
            print("3-Exit")
            print("[1/2/3]")
            first_run = False

        selection = input()
        if (selection == "1"):
            print(strings.get_hamming_distance(input("Enter DNA string 1 "), input("Enter DNA string 2 ")))
            exit = True
        elif (selection == "2"):
            print(strings.get_dna_complement(input("Enter DNA string ")))
            exit = True
        elif (selection == "3"):
            exit = True
        else:
            print("Please use [1/2/3]")

main()
