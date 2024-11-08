from turtle import Turtle, Screen
import random

def random_color():
    r = random.random()  # Random value for red (0 to 1)
    g = random.random()  # Random value for green (0 to 1)
    b = random.random()  # Random value for blue (0 to 1)
    return r, g, b

myTurtle = Turtle()
myTurtle.speed("fastest")

for angle in range(0, 361, 5):
    myTurtle.color((random_color()))
    myTurtle.circle(100)
    myTurtle.setheading(angle)


myScreen = Screen()
myScreen.exitonclick()
