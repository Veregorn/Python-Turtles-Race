from turtle import Turtle, Screen
import random

# Setup screen size config
screen = Screen()
screen.setup(width=500, height=400)

# Setup a list of colors for the different turtles
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Setup an empty array for the turtle objects
turtles = []

# This is a variable to control the height where a turtle is located
height = -125

# Setup a counter to go throw the array
counter = 0

# Setup a variable to exit the race loop
is_race_on = False

# Setup a variable to set the winner of the race
winner = ''

# Loop to create turtles and locate them
for color in colors:
    turtles.append(Turtle(shape="turtle"))
    turtles[counter].pencolor(color)
    turtles[counter].fillcolor(color)
    turtles[counter].penup()
    turtles[counter].goto(x=-230, y=height)
    height += 50
    counter += 1

# Show the modal window
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Once user has selected a color, the race can start
if user_bet:
    is_race_on = True

# Race loop
while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)
        # Check if turtle has won
        if turtle.xcor() >= 250:
            winner = turtle.pencolor()
            is_race_on = False

# Check if user has won the bet
print(f"{winner} turtle has won the race!")

if user_bet == winner:
    print("You win the bet :-)")
else:
    print("You lose the bet :-(")


screen.exitonclick()