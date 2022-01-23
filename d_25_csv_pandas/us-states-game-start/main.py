import turtle

import pandas

image = 'blank_states_img.gif'
screen = turtle.Screen()
screen.title('US States Game')
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv('50_states.csv')

guessed_states = []

while len(guessed_states) < 50:

    answer = screen.textinput(f'{len(guessed_states)}/50 States Correct', 'What\'s another state name?').title()
    if answer == 'Exit':
        missing_states = []
        for state in list(data.state):
            if state not in guessed_states:
                missing_states.append(state)
        missing_states_data = pandas.DataFrame(missing_states)
        missing_states_data.to_csv('states_to_learn.csv')
        break
    if answer in list(data.state):
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())  # .item() gets the first item
        guessed_states.append(answer)

turtle.mainloop()
