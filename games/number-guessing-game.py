# Thanks to the help of discord.gg/python

import random

num1 = int(input("Enter the minimum number: "))
num2 = int(input("(Larger numbers makes the game harder) Enter the maximum number: "))

number = random.randint(num1, num2)

while True:
    q = int(input("Guess a Number between the numbers you selected: "))
    if q == number:
        print ("You guessed it!")
        break
    else:
        print ("Nope, try again!")