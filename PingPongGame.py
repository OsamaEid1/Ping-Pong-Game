import turtle

# set the screen of the game
wind = turtle.Screen()
wind.title("Ping Pong Game By Osama")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# set the first paddle
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.shapesize(5, 1)
paddle1.color("red")
paddle1.penup()
paddle1.goto(350, 0)

# set the second paddle
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.shapesize(5, 1)
paddle2.color("blue")
paddle2.penup()
paddle2.goto(-350, 0)

# set the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.dx = 0.2
ball.dy = 0.2

# set score section
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(0, 260)
score.hideturtle()
score_of_player1 = 0
score_of_player2 = 0
winning_score = 2
score.write("player 1: 0    player 2: 0", align="center", font=("Currier", 24, "normal"))


# movement of the first paddle
# move to UP
def move_paddle1_to_up():
    y = paddle1.ycor()

    if y == 250:  # Check if the paddle reach to the top of the screen
        y = y
    else:
        y += 25

    paddle1.sety(y)


# move to Down
def move_paddle1_to_down():
    y = paddle1.ycor()

    if y == -250:  # Check if the paddle reach to the bottom of the screen
        y = y
    else:
        y -= 25

    paddle1.sety(y)


# movement of the second paddle
# move to UP
def move_paddle2_to_up():
    y = paddle2.ycor()

    if y == 250:  # Check if the paddle reach to the top of the screen
        y = y
    else:
        y += 25

    paddle2.sety(y)


# move to Down
def move_paddle2_to_down():
    y = paddle2.ycor()

    if y == -250:  # Check if the paddle reach to the bottom of the screen
        y = y
    else:
        y -= 25

    paddle2.sety(y)


# keyboard bindings
wind.listen()  # make the screen waiting for keys pressing

# paddle1
wind.onkeypress(move_paddle1_to_up, "Up")  # excecute the function when press on Up key
wind.onkeypress(move_paddle1_to_down, "Down")  # excecute the function when press on Down key

# paddle2
wind.onkeypress(move_paddle2_to_up, "w")  # excecute the function when press on w key
wind.onkeypress(move_paddle2_to_down, "s")  # excecute the function when press on s key

# movement of the ball


while True:
    wind.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # when ball reach to the top and bottom borders
    if ball.ycor() > 290:
        # ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.dy *= -1

    # when player1 lose
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        # increase score of player2
        score.clear()
        score_of_player2 += 1
        if score_of_player2== winning_score:
            ball.hideturtle()

            winner = turtle.Turtle()
            winner.speed(0)
            winner.color("green")
            winner.hideturtle()
            winner.goto(0, 0)
            winner.write("Winner Is Player 2", align="center", font=("Cairo", 32, "normal"))
            break
        else:
            score.write("player 1: {}    player 2: {}".format(score_of_player1, score_of_player2), align="center",
                    font=("Currier", 24, "normal"))

    # when player2 lose
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score.clear()
        score_of_player1 += 1
        if score_of_player1 == winning_score:
            ball.hideturtle()

            winner = turtle.Turtle()
            winner.speed(0)
            winner.color("green")
            winner.hideturtle()
            winner.goto(0, 0)
            winner.write("Winner Is Player 1", align="center", font=("Cairo", 32, "normal"))
            break
        else:
            score.write("player 1: {}    player 2: {}".format(score_of_player1, score_of_player2), align="center",
                        font=("Currier", 24, "normal"))

    # paddle1 hit the bll
    if (350 > ball.xcor() > 340) and ((ball.ycor() < paddle1.ycor() + 40) and (ball.ycor() > paddle1.ycor() - 40)):
        ball.setx(330)
        ball.dx *= -1

    # paddle2 hit the bll
    if (-350 < ball.xcor() < -340) and ((ball.ycor() < paddle2.ycor() + 40) and (ball.ycor() > paddle2.ycor() - 40)):
        ball.setx(-330)
        ball.dx *= -1
