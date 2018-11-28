# Simple 'falling skies' game in python3
# Original Guide from Christian Thompson AKA @TokyoEdTech

import turtle
import os
import random

score = 0
lives = 3

wn = turtle.Screen()
wn.title("Falling Skies by Sky")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)

# Add the player
player = turtle.Turtle()
player.speed(0)
player.penup()
player.shape("square")
player.color("white")
player.goto(0, -250)
player.direction = "stop"

# Create list of good_guy
good_guys = []

# Add the good_guy
for _ in range(8):
    good_guy = turtle.Turtle()
    good_guy.speed(0)
    good_guy.speed = random.randint(1, 4)
    good_guy.penup()
    good_guy.shape("circle")
    good_guy.color("blue")
    good_guy.goto(-100, 250)
    good_guys.append(good_guy)


# Create list of bad_guy
bad_guys = []

# Add the bad_guy
for _ in range(10):
    bad_guy = turtle.Turtle()
    bad_guy.speed(0)
    bad_guy.speed = random.randint(1, 4)
    bad_guy.penup()
    bad_guy.shape("circle")
    bad_guy.color("red")
    bad_guy.goto(100, 250)
    bad_guys.append(bad_guy)

# Make the Pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, 260)
font = ("Courier", 24, "normal")
pen.write("Score: {}   Lives: {}".format(score, lives), align="center", font=font)

# Functions
def go_left():
    player.direction = "left"


def go_right():
    player.direction = "right"


# Keyboard Binding
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")


while True:
    # Update screen
    wn.update()

    # Move the player
    if player.direction == "left":
        x = player.xcor()
        x -= 3
        player.setx(x)

    if player.direction == "right":
        x = player.xcor()
        x += 3
        player.setx(x)
    
    # Move the good guys
    for good_guy in good_guys:
        y = good_guy.ycor()
        y -= good_guy.speed
        good_guy.sety(y)

        # Check if good_guy off screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good_guy.goto(x, y)

        # Check for a collision with the player
        if good_guy.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            good_guy.goto(x, y)
            score += 10
            pen.clear()
            pen.write("Score: {}   Lives: {}".format(
                score, lives), align="center", font=font)

    # Move the bad guys
    for bad_guy in bad_guys:
        y = bad_guy.ycor()
        y -= bad_guy.speed
        bad_guy.sety(y)

        # Check if bad_guy off screen
        if y < -300:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)

        # Check for a collision with the player
        if bad_guy.distance(player) < 20:
            x = random.randint(-380, 380)
            y = random.randint(300, 400)
            bad_guy.goto(x, y)
            score -= 10
            lives -= 1
            pen.clear()
            pen.write("Score: {}   Lives: {}".format(
                score, lives), align="center", font=font)

    


wn.mainloop()
