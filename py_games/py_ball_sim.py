# Simple Ball simulator in python3
# Original Guide from Christian Thompson AKA @TokyoEdTech


import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("Bouncing Ball Sim")
wn.tracer(0)

balls = []

for _ in range(25):
    balls.append(turtle.Turtle())


colors = ["red", "blue", "yellow", "orange", "green", "white", "purple"]
shapes = ["circle", "triangle", "square"]

for ball in balls:
    ball.shape(random.choice(shapes))
    x = random.randint(-290, 280)
    y = random.randint(200,400)
    ball.goto(x, y)
    ball.color(random.choice(colors))
    ball.penup()
    ball.speed(0)
    ball.dy =  0
    ball.dx = random.randint(-3, 3)
    ball.da = random.randint(-5, 5)

gravity = 0.1

while True:
    wn.update()
    
    for ball in balls:
        ball.dy -= gravity
        ball.rt(ball.da)
        ball.sety(ball.ycor() + ball.dy)

        ball.setx(ball.xcor() + ball.dx)

        # Check for wall collision
        if ball.xcor() > 280:
            ball.dx *= -1
            ball.da *= -1
        
        if ball.xcor() < - 290:
            ball.dx *= -1
            ball.da *= -1

        # Check for a bounce
        if ball.ycor() < - 280:
            ball.dy *= -1
            ball.da *= -1


wn.mainloop()
