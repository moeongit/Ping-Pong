import turtle
import os

class Window:
    def __init__(self, width, height, title, bgcolor):
        self.window = turtle.Screen()
        self.window.title(title)
        self.window.bgcolor(bgcolor)
        self.window.setup(width = width, height = height)
        self.window.tracer(0)
    
    def update(self):
        self.window.update()

class Paddle:
    def __init__(self, position):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.shapesize(stretch_wid=4.5, stretch_len=0.5)
        self.paddle.penup()
        self.paddle.goto(position, 0)

    def move_up(self):
        y = self.paddle.ycor()
        y += 25
        self.paddle.sety(y)

    def move_down(self):
        y = self.paddle.ycor()
        y -= 25
        self.paddle.sety(y)

class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(3)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 2
        self.ball.dy = 2

    def update(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball.dy *= -1
            os.system("afplay bounce.wav&")
        
        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.ball.dy *= -1
            os.system("afplay bounce.wav&")

        if self.ball.xcor() > 390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
        
        if self.ball.xcor() < -390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1

class Pen:
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 260)
        self.pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "normal"))

    def update_score(self, score_a, score_b):
        self.pen.clear()
        self.pen.write("Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

class PingPongGame:
    def __init__(self):
        self.window = Window(800, 600, "Maatez's PingPong Game", "black")
        self.paddle_a = Paddle(-350)
        self.paddle_b = Paddle(350)
        self.ball = Ball()
        self.score_a = 0
        self.score_b = 0
        self.pen = Pen()

        self.window.window.listen()
        self.window.window.onkeypress(self.paddle_a.move_up, "w")
        self.window.window.onkeypress(self.paddle_a.move_down, "s")
        self.window.window.onkeypress(self.paddle_b.move_up, "Up")
        self.window.window.onkeypress(self.paddle_b.move_down, "Down")

    def game_loop(self):
        while True:
            self.ball.update()
            self.window.update()

            if self.ball.ball.ycor() > 290:
                self.pen.pen.write("eiesiuisdgf")
                self.ball.ball.sety(290)
                self.ball.ball.dy *= -1

            if self.ball.ball.ycor() < -290:
                self.ball.ball.sety(-290)
                self.ball.ball.dy *= -1

            if self.ball.ball.xcor() > 380:
                self.ball.ball.goto(0, 0)
                self.ball.ball.dx *= -1
                self.score_a += 1
                self.pen.update_score(self.score_a, self.score_b)

            if self.ball.ball.xcor() < -380:
                self.ball.ball.goto(0, 0)
                self.ball.ball.dx *= -1
                self.score_b += 1
                self.pen.update_score(self.score_a, self.score_b)

            if (self.ball.ball.xcor() > 340 and self.ball.ball.xcor() < 350) and \
                    (self.ball.ball.ycor() < self.paddle_b.paddle.ycor() + 40 and
                     self.ball.ball.ycor() > self.paddle_b.paddle.ycor() - 40):
                self.ball.ball.setx(340)
                self.ball.ball.dx *= -1
                os.system("afplay bounce.wav&")

            if (self.ball.ball.xcor() < -340 and self.ball.ball.xcor() > -350) and \
                    (self.ball.ball.ycor() < self.paddle_a.paddle.ycor() + 40 and
                     self.ball.ball.ycor() > self.paddle_a.paddle.ycor() - 40):
                self.ball.ball.setx(-340)
                self.ball.ball.dx *= -1
                os.system("afplay bounce.wav&")
            
game = PingPongGame()
game.game_loop()