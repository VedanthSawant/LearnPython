import colorgram
from turtle import Turtle, Screen
import random

colors = colorgram.extract('image.jpg', 30)
color_list = []
for item in colors:
    myColor = item.rgb
    myTuple = (myColor.r, myColor.g, myColor.b)
    color_list.append(myTuple)

y_axis = -350
myTurtle = Turtle()
myTurtle.penup()
myTurtle.hideturtle()
myTurtle.goto(-370, y_axis)
myTurtle.speed("fastest")

myScreen = Screen()
myScreen.colormode(255)

for row in range(26):
    for col in range(20):
        index = random.randint(0, len(color_list) - 1)
        myTurtle.color((color_list[index]))
        myTurtle.pendown()
        myTurtle.dot(20)
        myTurtle.penup()
        myTurtle.forward(50)
    y_axis += 30
    myTurtle.goto(-370, y_axis)


myScreen = Screen()
myScreen.colormode(255)
myScreen.exitonclick()
