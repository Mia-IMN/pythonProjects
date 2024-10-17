from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move():
    timmy.forward(10)

def move_forward():
    timmy.setheading(0)
    timmy.forward(10)

def move_backward():
    timmy.setheading(180)
    timmy.forward(10)

def move_up():
    timmy.setheading(90)
    timmy.forward(10)

def move_down():
    timmy.setheading(270)
    timmy.forward(10)

def clockwise():
    timmy.setheading(timmy.heading() - 10)
    timmy.forward(10)

def counter_clockwise():
    timmy.setheading(timmy.heading() + 10)
    timmy.forward(10)

def move_left():
    timmy.setheading(timmy.heading() + 10)

def move_right():
    timmy.setheading(timmy.heading() - 10)

def delete():
    timmy.penup()
    timmy.clear()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(move_forward, "Right")
screen.onkey(move_backward, "Left")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(clockwise, "c")
screen.onkey(counter_clockwise, "a")
screen.onkey(move_right, "r")
screen.onkey(move_left, "l")
screen.onkey(move, "space")
screen.onkey(delete, "Delete")
screen.exitonclick()