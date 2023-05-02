from turtle import Turtle, Screen
t = Turtle()
screen = Screen()

t.pensize(8)

def move_forward():
    t.speed(0)
    t.forward(10)

def move_backward():
    t.backward(10)
    t.speed(10)

def move_right():
    t.right(10)

def move_left():
    t.left(10)


screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")

screen.exitonclick()