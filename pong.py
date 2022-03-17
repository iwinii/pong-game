import turtle
import winsound
import os
import platform

wn = turtle.Screen()
wn.title("Pong by Iza & Karol")
wn.bgcolor('pink')
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = 0.5

# Ball
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("square")
ball2.color("green")
ball2.penup()
ball2.goto(0, 0)
ball2.dx = -0.5
ball2.dy = 0.5

# Paddle_a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle_b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(350, 0)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A:  0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function
def play_bounce_sound():
    if platform.system() == 'Windows':
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    pass

def paddle_move(paddle, ymove):
    y = paddle.ycor()
    y += ymove
    paddle.sety(y)


def paddle_a_up():
    paddle_move(paddle_a, 20)


def paddle_a_down():
    paddle_move(paddle_a, -20)


def paddle_b_up():
    paddle_move(paddle_b, 20)


def paddle_b_down():
    paddle_move(paddle_b, -20)


wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Move the ball
    ball2.setx(ball2.xcor() + ball2.dx)
    ball2.sety(ball2.ycor() + ball2.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        play_bounce_sound()

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        play_bounce_sound()

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A:  {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball2.ycor() > 290:
        ball2.sety(290)
        ball2.dy *= -1
        play_bounce_sound()

    if ball2.ycor() < -290:
        ball2.sety(-290)
        ball2.dy *= -1
        play_bounce_sound()

    if ball2.xcor() > 390:
        ball2.goto(0, 0)
        ball2.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A:  {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball2.xcor() < -390:
        ball2.goto(0, 0)
        ball2.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if paddle_a.ycor() > 250:
        paddle_a.sety(250)
    if paddle_a.ycor() < -250:
        paddle_a.sety(-250)
    if paddle_b.ycor() > 250:
        paddle_b.sety(250)
    if paddle_b.ycor() < -250:
        paddle_b.sety(-250)

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (
            ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        play_bounce_sound()

    if (ball.xcor() < -340 and ball.xcor() > -350) and (
            ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        play_bounce_sound()

    if (ball2.xcor() > 340 and ball2.xcor() < 350) and (
                ball2.ycor() < paddle_b.ycor() + 40 and ball2.ycor() > paddle_b.ycor() - 40):
            ball2.setx(340)
            ball.dx *= -1
            play_bounce_sound()

    if (ball2.xcor() < -340 and ball2.xcor() > -350) and (
                ball2.ycor() < paddle_a.ycor() + 40 and ball2.ycor() > paddle_a.ycor() - 40):
            ball2.setx(-340)
            ball2.dx *= -1
            play_bounce_sound()

    # AI Player
    if ball.xcor() > ball2.xcor():
        if paddle_b.ycor() < ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b_up()

        elif paddle_b.ycor() > ball.ycor() and abs(paddle_b.ycor() - ball.ycor()) > 10:
        paddle_b_down()
    else:
        if paddle_b.ycor() < ball2.ycor() and abs(paddle_b.ycor() - ball2.ycor()) > 10:
        paddle_b_up()

        elif paddle_b.ycor() > ball2.ycor() and abs(paddle_b.ycor() - ball2.ycor()) > 10:
        paddle_b_down()
