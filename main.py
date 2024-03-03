import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle = turtle.Turtle()

states_data = pandas.read_csv("50_states.csv")
states = states_data.state.to_list()


def get_coordinates():
    data = (states_data[states_data["state"] == answer_state])
    return int(data.x), int(data.y)


correct_answer = []

while len(correct_answer) < 50:
    answer_state = screen.textinput(title=f"{ len(correct_answer)}/50 Guess the State",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        to_learn_states = [state for state in states if state not in correct_answer]
        to_learn_data = pandas.DataFrame(to_learn_states)
        to_learn_data.to_csv("states_to_learn.csv")
        break

    if (answer_state in states) and (answer_state not in correct_answer):
        correct_answer.append(answer_state)
        turtle.penup()
        turtle.hideturtle()
        turtle.goto(get_coordinates())
        turtle.write(answer_state)

screen.exitonclick()
#  _____get x and y on a click____
# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()