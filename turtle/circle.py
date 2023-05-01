import turtle
t = turtle.Turtle()
s = turtle.Screen().bgcolor('black')
t.speed(0)
for i in range(360):
    t.color('yellow')
    t.left(1)
    t.fd(1)
    for j in range(2):
        t.left(2)
        t.circle(100)
