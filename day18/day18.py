import turtle as t
import random

tim = t.Turtle()
tim.shape('turtle')
tim.color('blue')
tim.pensize(10)
tim.speed('fastest')
t.colormode(255)
color = ()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r,g,b)

# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

#colors = ['red', 'blue','green']
directions = [0, 90, 180, 270]

for _ in range(200):
    tim.tilt(5)
    tim.circle(100)
    color = random_color()
    tim.pencolor(color)
   # tim.setheading(random.choice(directions))












screen = Screen()
screen.exitonclick()