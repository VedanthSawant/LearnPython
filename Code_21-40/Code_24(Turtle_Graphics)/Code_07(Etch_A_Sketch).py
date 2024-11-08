from turtle import Turtle, Screen

def moveForward():
    myTurtle.forward(20)

def moveBackward():
    myTurtle.back(20)

def moveCountClockwise():
    myTurtle.left(20)

def moveClockwise():
    myTurtle.right(20)

def clearScreen():
    myTurtle.clear()
    myTurtle.reset()

def on_key_press(key, func):
    # Register both lowercase and uppercase for the given key
    myScreen.onkey(fun=func, key=key.lower())
    myScreen.onkey(fun=func, key=key.upper())

myTurtle = Turtle()
myScreen = Screen()
myScreen.listen()
on_key_press("w", moveForward)
on_key_press("s", moveBackward)
on_key_press("a", moveCountClockwise)
on_key_press("d", moveClockwise)
on_key_press("c", clearScreen)
myScreen.exitonclick()