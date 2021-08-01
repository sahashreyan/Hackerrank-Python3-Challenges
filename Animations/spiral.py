import turtle
colors = ["red","blue","green","orange","pink","white","yellow"]
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(0)
screen.bgcolor("black")
for x in range(300):
    t.pencolor(colors[x%7])
    t.width(3)
    t.forward(x)
    t.left(20)
    

