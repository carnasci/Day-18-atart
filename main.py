import turtle
from turtle import Turtle, Screen
import random

def get_random_color():
    return tuple(random.randint(0, 255) for _ in range (3))

turtle.colormode(255)
timmy = Turtle()

# n = 3
#
# while n <= 10:
#
#     timmy.pencolor(get_random_color())
#     for _ in range(n):
#         timmy.forward(100)
#         timmy.right(360 / n)
#     n += 1

# timmy.pensize(3)
# timmy.speed("fast")
#
# def move_left():
#     timmy.left(90)
#     timmy.forward(15)
#
# def move_right():
#     timmy.right(90)
#     timmy.forward(15)
#
# def move_forward():
#     timmy.forward(15)
#
# def move_backward():
#     timmy.backward(15)
#
# directions = [move_left, move_right, move_backward, move_forward]
#
# for _ in range(50):
#     timmy.pencolor(get_random_color())
#     direction = random.choice(directions)
#     direction()

#CHALLENGE 5

timmy.speed("fastest")
# n = 0
#
# while n <= 360:
#
#     for _ in range(100):
#         timmy.color(get_random_color())
#         timmy.circle(100)
#         n += 5
#         timmy.left(n)

def draw_spirograph(size_of_gap):

    for _ in range(int(360 / size_of_gap)):
        timmy.color(get_random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(5)

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
