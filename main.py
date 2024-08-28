import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv("50_states.csv")

score = 0
guess_state = []

while len(guess_state) < 50:
    state_series = states['state']
    state_count = len(state_series)
    answer = screen.textinput(title=f"Guess new state: {score}/{state_count}",
                              prompt="What's an other state's name ?").title()

    if answer == "Exit":
        missing_state = [state for state in state_series.to_list() if state not in guess_state]
        new_learn_states = pandas.DataFrame(missing_state)
        new_learn_states.to_csv("new_learn_states.csv")
        break
    if state_series.isin([answer]).any():
        row = states[states['state'] == answer].iloc[0]  # Get the first matching row
        guess_state.append(answer)
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(row.x.item(), row.y.item())  # Access the values directly
        t.write(f"{answer}")
    else:
        print("clear the input")

screen.mainloop()
