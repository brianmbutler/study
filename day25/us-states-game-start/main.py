import turtle
import pandas as pd

screen = turtle.Screen()
df = pd.read_csv('50_states.csv')


screen.title("U.S. States Game")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

all_states = df['state'].to_list()
guessed_states = []


while len(guessed_states) < 50:
    
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States Guessed", "What's another state's name?" ).title()
    guessed_states.append(answer_state)

    if answer_state == 'Exit':
        # states_to_learn = []
        states_to_learn = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         states_to_learn.append(state)

        new_data = pd.DataFrame(states_to_learn)
        new_data.to_csv('states_to_learn.csv')

        break
    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = df[df['state'] == answer_state]
        x = state['x']
        y = state['y']
        t.goto(int(x), int(y))
        t.write(f'{answer_state}', move=False, align='center', font=('Arial', 8, 'normal'))





turtle.mainloop()