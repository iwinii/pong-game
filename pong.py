import turtle

wn = turtle.Screen()
wn.title("Pong by Iza & Karol")
wn.bgcolor('pink')
wn.setup(width=800, height=600)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)


# Function
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
