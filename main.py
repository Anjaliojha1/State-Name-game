import turtle
import pandas
data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()



screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)


# # To know the coordinates of each states
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
guess_state = []
while len(guess_state) < 50:

    answer_state = screen.textinput(title=f"{len(guess_state)}/50 Guess the State",prompt="What's another state's name? ").title()
    print(answer_state)



    if answer_state == "Exit":
        missing_states = []
        for s in all_state:
            if s not in guess_state:
                missing_states.append(s)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States to learn.csv")

        break

    if answer_state in all_state:
        guess_state.append(answer_state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x),  int(state_data.y))
        t.write(state_data.state.item())

# states to learn


turtle.mainloop()
