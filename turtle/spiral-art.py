import turtle
turtle.bgcolor('black')
t = turtle.Turtle()
colours = ['red', 'dark red']

for number in range(400):
    t.forward(number+1)
    t.right(89)
    t.pencolor(colours[number % 2])
    turtle.speed(0)
turtle.done()
