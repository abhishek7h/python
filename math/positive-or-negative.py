def main():
    num = int(input("Enter the number you would like to check: "))

    if num < 0:
        print(f"{num} is a negative number.")
    else: 
        print(f"{num} is a positive number.")

    repeat = input("Would you like to run again? (y/n): ")
    if repeat == "y":
        main()
    elif repeat == "n":
        exit()
main()
