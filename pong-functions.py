import turtle

wn = turtle.Screen()
wn.title("Pong by Iza & Karol")
wn.bgcolor('pink')
wn.setup(width=800, height=600)
wn.tracer(0)


# Function
def create_ball():
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 0.05
    ball.dy = 0.05
    return ball


def create_paddle(x, y):
    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_len=1, stretch_wid=5)
    paddle.penup()
    paddle.goto(x, y)
    return paddle


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


ball = create_ball()
paddle_a = create_paddle(-350, 0)
paddle_b = create_paddle(350, 0)

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

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1


# Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1