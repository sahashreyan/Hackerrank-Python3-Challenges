import turtle
t = turtle.Turtle()
wn = turtle.Screen()
wn.bgcolor("Black")
t.speed(0)
t.color("White")
for i in range(1625):
    t.fd(6+i)
    t.right(91)
    i+=2
turtle.done()
