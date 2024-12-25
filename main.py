import turtle
from turtle import Turtle, Screen
import random

def get_random_color():
    return tuple(random.randint(0, 255) for _ in range (3))

turtle.colormode(255)
timmy = Turtle()

n = 3

while n <= 10:

    timmy.pencolor(get_random_color())
    for _ in range(n):
        timmy.forward(100)
        timmy.right(360 / n)
    n += 1




# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)
# timmy.right(90)
# timmy.forward(100)

# for _ in range(25):
#     timmy.pendown()
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)


my_screen = Screen()
my_screen.exitonclick()
