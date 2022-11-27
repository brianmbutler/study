from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False

colors = ['red', 'orange', 'yellow','green', 'blue', 'purple']
all_turtles = []

user_input = screen.textinput('Make your bet!?', 'Which turtle will win the race? Enter a color: ')

for color in range(len(colors)):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[color])
    new_turtle.goto(x=-230, y = (150 - (color * 50)))
    all_turtles.append(new_turtle)
#W = forwards, S = backwards A= counter_clockwise, d= clockwise c= clear drawing, reset drawing



if user_input:
    is_race_on = True

while is_race_on:
   
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color >= user_input:
                print(f"You've won!  The {winning_color} turtle is the winner!")
            else:
                print(f"You've lose! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick()