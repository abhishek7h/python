import random

number = random.randint(1,5)

while True:
    q = int(input("Guess a number between 1 and 5: "))
    if q == number:
        print("You guessed it!")
        break
    else:
        print("Try again!")