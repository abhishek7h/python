import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'cyan']

def get_number_of_racers():
    racers=0
    while True:
            racers=input("Enter the number of racers (2 -10): ")
            if racers.isdigit():
                racers = int(racers)
            else: 
                print('Input is not a number. Please try again.')
                continue

            if 2 <= racers <= 10:
                return racers
            else:
                print('Number is not in the range of 2-10. Please try again.')

def race (colors):
    turtles = create_turtles(colors)

    while True:
        for racer in turtles:
            distance = random.randrange(1,20)
            racer.forward(distance)

            x, y = racer.pos()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(racer)]


def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i + 1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles
    


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")

  # create finish line | credit: Griffin Van Beek on YouTube (comment)
    finish = turtle.Turtle()
    finish.color('black')
    finish.shape('arrow')
    finish.speed(0)
    finish.penup()
    finish.setpos(-WIDTH//2, HEIGHT//2 - 20)
    finish.pendown()
    finish.forward(WIDTH)

racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is " + winner + "! GG")
time.sleep(5)
