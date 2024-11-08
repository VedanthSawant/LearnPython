from turtle import Turtle, Screen
import random
myTurtle = Turtle()

def random_color():
    r = random.random()  # Random value for red (0 to 1)
    g = random.random()  # Random value for green (0 to 1)
    b = random.random()  # Random value for blue (0 to 1)
    return r, g, b

myTurtle.penup()
myTurtle.goto(-100, 200)
myTurtle.pendown()

for num in range(3, 11):
    myTurtle.color(random_color())
    sum_of_angles = (num - 2) * 180
    angle = sum_of_angles / num
    for repeat in range(num):
        myTurtle.forward(100)
        myTurtle.right(180-angle)

myScreen = Screen()
myScreen.exitonclick()
