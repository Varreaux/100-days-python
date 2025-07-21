import turtle
import pandas

screen = turtle.Screen()
screen.title("morgan's state game")
canvas = screen.getcanvas()
canvas.focus_force()

image = "Day25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


guess = screen.textinput("User guess", "Name a state")
data = pandas.read_csv("Day25/50_states.csv")
states = data.state.to_list()
continue_game = True

states_found = 0
found = []
not_found = []
while continue_game:
    for state in states:
        if guess.lower() == state.lower():
            name = turtle.Turtle()
            name.teleport(int(data[data.state==state].x), int(data[data.state==state].y))
            name.color("black")
            name.write(state, False, "center", ("Arial", 18, "normal"))
            name.hideturtle()
            if state not in found:
                found.append(state)
                states_found+=1
            break

    if states_found == 50 or guess.lower() == "exit":
        continue_game = False
        break
    guess = screen.textinput(f"{states_found}/50", "Name a state")

if guess.lower() == "exit":
    for state in states:
        if state not in found:
            not_found.append(state)
    df = pandas.DataFrame(not_found, columns=["states not found"])
    df.to_csv("Day25/states_not_found.csv", index=False)
    exit()
else:
    name.teleport(0,0)
    name.color("green")
    name.write("Congratz! You found all of them!", False, "center", ("Arial", 35, "normal"))
screen.exitonclick()

