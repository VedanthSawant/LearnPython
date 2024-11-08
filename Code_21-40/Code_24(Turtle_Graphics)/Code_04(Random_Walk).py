from turtle import Turtle, Screen
import random

def random_color():
    r = random.random()  # Random value for red (0 to 1)
    g = random.random()  # Random value for green (0 to 1)
    b = random.random()  # Random value for blue (0 to 1)
    return r, g, b

direction = [0, 90, 180, 270]
myTurtle = Turtle()
myTurtle.pensize(9)
myTurtle.speed("fastest")

for _ in range(1000):
    myTurtle.color((random_color()))
    myTurtle.forward(10)
    myTurtle.setheading(direction[random.randint(0, 3)])

myScreen = Screen()
myScreen.exitonclick()
