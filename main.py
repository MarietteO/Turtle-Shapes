import turtle as t
import random

tim = t.Turtle()

colours = ["red", "blue","green", "yellow", "purple", "magenta", "cyan", "orange"]

x = 3

while x < 11:
    tim.pencolor(random.choice(colours))
    for _ in range(x):
        tim.rt(360/x)
        tim.forward(100)
    x +=1

screen = Screen()
screen.exitonclick()
