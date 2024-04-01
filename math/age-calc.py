def main():

    bday = int(input('In which year were you born? '))

    age = 2024 - bday

    print(f'You are {age} years old.')

    if age >= 18:
        print(f'PS: Since you are {age} years old, you are legally an adult. ')
    else:
        print(f'PS: You are legally not an adult, since you are {age}.')

    repeat = input("> Would you like to run again? y/n ")
    if repeat == "y":
        main()
    elif repeat == "n":
        exit()


main()
