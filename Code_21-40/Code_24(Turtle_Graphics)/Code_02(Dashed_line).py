# Write a code to draw a dashed line

from turtle import Turtle, Screen

myTurtle = Turtle()
myTurtle.penup()
myTurtle.goto(-300,0)
myTurtle.pendown()
for _ in range(25):
    myTurtle.forward(10)
    myTurtle.penup()
    myTurtle.forward(10)
    myTurtle.pendown()

myScreen = Screen()
myScreen.exitonclick()