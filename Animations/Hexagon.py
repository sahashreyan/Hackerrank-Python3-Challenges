import turtle

colors = ["red","blue","green","orange","pink","white"]
t=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor("black")
t.speed(25)
for i in range(250):
    t.pencolor(colors[i%6])
    t.forward(i*1.5)
    t.left(59)
    t.width(3)
    
    