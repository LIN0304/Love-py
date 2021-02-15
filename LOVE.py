
import turtle
turtle.bgcolor("black")
# Creating a turtle object(pen)
pen = turtle.Turtle()
pen.pencolor("red")
# Defining a method to draw curve
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)
# Defining method to draw a full heart
def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()
# Defining method to write text
def txt():
    pen.up()
    pen.setpos(-68, 95)
    pen.down()
    pen.color('black')
    pen.write("I love my laptop", font=("Verdana", 12, "bold"))
heart()
while True:
    txt()
    pen.ht()
