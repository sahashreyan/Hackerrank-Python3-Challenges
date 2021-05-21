from turtle import *
speed(10)
bgcolor("black")
color('red', 'yellow')
begin_fill()
def main():
    print('Painting the Cartoon... ')
    turtle.screensize(800,600)
    turtle.position(-20,10)
while True:
    forward(450)
    left(170)
    if abs(pos())<1:
        break

end_fill()
done()
