# Snake in Python, originally made by TokyoEdtech on YouTube
# The goal was to code "snake" in python version 3. When the script is running, it should open up a window like the image above.
# That window is where the game will be played.
# The snake, or eel in this case, will be stationary at the beginning and must be moved with the W, A, S, or D keys in order to start.
# The player will control the green square and must collect the food, the maroon circles, in order to grow and obtain more points.
# The player must avoid hitting the walls and the eel's body as doing so would result in the game ending.

# based on: TokyoEdtech (2018) Python (Version 3) https://www.youtube.com/watch?v=BP7KMlbvtOo

import turtle
import time
import random

delay = 0.1

# Score (tells the starting score for the first game)
score = 0
high_score = 0

# 1) Setting up the screen (what the actual game will look like/the window where the game is played)
wn = turtle.Screen()
wn.title("Eel Game")
wn.bgcolor("dark turquoise")
wn.setup(width=600, height=600)
wn.tracer(0) # turns off screen updates

# 2) Snake Head (the player themselves, what we control)
# turtle is used to display the turtle itself, therefore the physical description must be coded
eel = turtle.Turtle()
eel.speed(0)
eel.shape("square")
eel.color("dark green")
eel.penup()
eel.goto(0,0)
eel.direction = "stop"

# Food/apple
# what the player uses to grow
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("maroon")
food.penup()
food.goto(0,100)

# the new growth that the snake/eel gets after eating the "food". 1 segment is added after eating 1 piece of food
segments = []

# Pen (write text)
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("midnight blue")
pen.penup()
pen.hideturtle() # hides the actual pen, allows so that only the text itself is visible
pen.goto(0, 260)
pen.write("Score: 0   High Score: 0", align="center", font=("Arial", 22, "normal"))


# Functions --> first part makes it so that the eel can't go backwards on itself and die that way. ie, if you're going up, you can't go back directly down.
def go_up():
    if eel.direction != "down":
        eel.direction = "up"

def go_down():
    if eel.direction != "up":
        eel.direction = "down"

def go_left():
    if eel.direction != "right":
        eel.direction = "left"

def go_right():
    if eel.direction != "left":
        eel.direction = "right"

# this is what allows the eel to move
def move():
    if eel.direction == "up":
        y = eel.ycor()
        eel.sety(y + 20)
    
    if eel.direction == "down":
        eel.sety(eel.ycor() - 20)

    if eel.direction == "left":
        x = eel.xcor()
        eel.setx(x - 20)
    
    if eel.direction == "right":
        eel.setx(eel.xcor() + 20)

# Keyboard bindings --> looks for inputs from the keyboard (w, a, s, d keys), the actual controls for the game.
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Main game loop --> the actual code that takes the visual aspects and applies the gameplay to it. More specifically, this is where the challenge of the gameplay comes from such as the eel growing, the eel dying, the score being tracked, etc.
while True:
    wn.update()

    # Check for border collision --> one of the possible ways to die which is hitting the border of the game window
    if eel.xcor()>290 or eel.xcor()<-290 or eel.ycor()>290 or eel.ycor()<-290:
        time.sleep(1)
        eel.goto(0,0)
        eel.direction = "stop"

        # Hide segments --> when the eel dies, all progress is lost, therefore the eel has to start growing again. This just hides the previous segments that were obtained from the previous round.
        for segment in segments:
            segment.goto (1000, 1000)

        # Clear the segments list --> similar to the code above, except this actually removes the body segments from the head of the eel
        segments.clear() 

        # Reset the score --> when the eel dies, that game round is over so the score must go back to 0
        score = 0

        # Reset the delay --> because of turtle, the game eventually begins to lag a bit. To make up for that, the gameplay speeds up slightly the longer the eel gets. Once the eel dies, it isn't necessary to speed up so the speed of it goes back to its original rate.
        delay = 0.1

        # Update the score display --> This is were the score can be updated each time the food is eaten by the eel
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Arial", 22, "normal"))


    # Check for collision with food --> what actually allows the eel to interact with the food so that it doesn't just stay in one place.
    if eel.distance(food) < 20:
        # Move the food to random spot --> after the eel touches the food, the food will move to a randomly generated point. necessary to have import random at the top in order to have randomly generated points
        x = random.randint(-290,290)
        y = random.randint(-290,290)
        food.goto(random.randint(-290,290),random.randint(-290,290))

        # Add a segment --> the code that adds a new body segment to the eel after eating the food
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("yellow green")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten delay --> to make up for the lag from turtle when new body segments are added.
        delay -= 0.001

        # Increase the score --> causes the score to increase once the eel gets the food
        score += 10

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align="center", font=("Arial", 22, "normal"))

    # Move end segments first in reverse order (huh?)
    # I'm still a little confused about what this exactly does but basically it tells where to put the new body segment after the eel eats the food. essentially, the body will grow behind the head and follow after it and the body will appear to stay in its place instead of gliding across the screen.
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where the head is --> the first segment obtained. 
    if len(segments) > 0:
        x = eel.xcor()
        y = eel.ycor()
        segments[0].goto(x,y)

    move()

    # Check for head collision w/ body segments --> another way the player can die, if the eel turns and hits its body
    for segment in segments:
        if segment.distance(eel) < 20:
            time.sleep(1)
            eel.goto(0,0)
            eel.direction = "stop"

             # Hide segments
            for segment in segments:
                segment.goto (1000, 1000)

            # Clear the segments list
            segments.clear() 

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

    time.sleep(delay) # allows the player to see the eel at the start screen
# One thing I noticed is that the game really only works if it stays in a minimized window.
# When in a larger window, the eel will still die within the borders of the minimized window.
# There might be someway to change it so that both the minimized and maximized windows can be playable.
# I assume that would be controlled in the first step, where the margins of the game are made and where the border collision control is
wn.mainloop()