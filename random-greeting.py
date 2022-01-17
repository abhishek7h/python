import random 

name = input("What is your name? ")

greetings = ["Hey", "Hello", "Hi"]

greeting = random.choice(greetings)

print (greeting + ", " + name)


