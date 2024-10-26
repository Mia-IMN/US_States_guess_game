from turtle import Turtle, Screen
import pandas

turtle = Turtle()
timmy = Turtle()
timmy.hideturtle()
timmy.penup()

screen = Screen()
screen.title("Name the States")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
game_is_on = True
total = 0
guessed_states = []
file = pandas.read_csv("50_states.csv")

while game_is_on:

    my_prompt = screen.textinput(f"{total}/50 State Guessed", "Name a US state you know")
    my_prompt_proper = my_prompt.title()

    num = -1

    if my_prompt_proper == "Exit":
        game_is_on = False

    if my_prompt_proper == "End":
        break

    for state in file.state:
        num += 1
        if state == my_prompt_proper:
            row = file[file.state == my_prompt_proper]
            row_list = row.to_dict()
            xcor = row_list['x']
            ycor = row_list['y']
            timmy.goto(xcor[num], ycor[num])
            timmy.write(state, align="center", font=("Arial", 8, "normal"))
            total += 1
            if state not in guessed_states:
                guessed_states.append(state)

    if total == 50:
        game_is_on = False

num = -1
for state in file.state:
    num += 1
    if state not in guessed_states:
        timmy.color("red")
        row = file[file.state == state]
        row_list = row.to_dict()
        xcor = row_list['x']
        ycor = row_list['y']
        timmy.goto(xcor[num], ycor[num])
        timmy.write(state, align="center")

screen.exitonclick()