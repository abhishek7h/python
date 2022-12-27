def main():
    import random

    rolled = random.randint(1, 6)
    print(f"> You rolled: {rolled}")

    repeat = input("> Would you like to roll again? y/n ")
    if repeat == "y":
        main()
    elif repeat == "n":
        exit()
main()
