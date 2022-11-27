from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def clockwise():
    tim.right(5)

def counter_clockwise():
    tim.left(5)

def clear():
    tim.reset()

screen.listen()
screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_backward)
screen.onkey(key='a', fun=counter_clockwise)
screen.onkey(key='d', fun=clockwise)
screen.onkey(key='c', fun=clear)

#W = forwards, S = backwards A= counter_clockwise, d= clockwise c= clear drawing, reset drawing


screen.exitonclick()