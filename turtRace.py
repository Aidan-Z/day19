import turtle
from turtle import Turtle, Screen
import random
screen = Screen()

racing = False #flag
screen.setup(width=500, height=400) #screen setup
user_bet = screen.textinput(title="bet", prompt="place a bet on who will win: ") #input text prompt window
colors = ['blue', 'red', 'green', 'black', 'purple'] #list of turtle colors
y_positions = [100, 50, 0, -50, -100] #list of starting positions
turtles = [] #empty turtle list

for i in range(0,5): #for i in range of numbers (amount of available colors)
    new_turtle = Turtle(shape='turtle') #generate new_turtle object with shape 'turtle'
    new_turtle.penup() #pen up before moving to start position
    new_turtle.goto(x=-235, y=y_positions[i]) #make instances go to start positon
    new_turtle.color(colors[i]) #loop through colors for each object and assign color
    turtles.append(new_turtle) #each new object appended to turtle list

if user_bet: # "if user_bet exists"
    racing = True #set flag to true to start while loop

while racing:

    for i in turtles: #for each object in list turtles
        if i.xcor() > 230: #if 'x' coordinate is > 230
            racing = False #stop loop
            winner = i.pencolor() #get color of first turtle to pass x230
            if winner == user_bet: #if its the same as user_bet coloor, user wins
                print(f"{winner} was the winner, you win...")

            else:
                print(f"{winner} was the winner, you lose!!")


        random_distance = random.randint(0, 10) #pick a random number (1-10) to use as speed
        i.forward((random_distance)) #turtle.forward by the random distance given









screen.exitonclick()
