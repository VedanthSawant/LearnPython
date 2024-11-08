# Write a code to draw a square

from turtle import Turtle, Screen

myTurtle = Turtle()
myTurtle.shape("turtle")
myTurtle.color("red")
for _ in range(4):
    myTurtle.forward(100)
    myTurtle.right(90)

myScreen = Screen()
myScreen.exitonclick()