import turtle
import random

timmy = turtle.Turtle()

# generating a pattern of triangle, square, hexagon, heptagon, nonagon, decagon
color = ["gainsboro", "light gray", "silver", "dark gray", "gray", "dim gray", "gray", "light slate gray"]
# num_size = 3
# while num_size < 11:
#     timmy.color(color[num_size-3])
#     angle = 360 / num_size
#     for _ in range(num_size):
#         timmy.right(angle)
#         timmy.forward(90)
#         num_size += 1


# Drawing a spirograph
# timmy.speed(0)
# def spirograph(gap_size):
#     for _ in range(int(360 / gap_size)):
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + gap_size)
#         timmy.color(random.choice(color))
#
# spirograph(5)

# drawing an art work using the principle of random walk
# timmy.hideturtle()
# timmy.speed(0)
# timmy.pensize(10)
# angles = [0, 90, 180, 270]
# for _ in range(200):
#     timmy.color(random.choice(color))
#     timmy.setheading(random.choice(angles))
#     timmy.forward(20)



screen = turtle.Screen()
screen.exitonclick()

