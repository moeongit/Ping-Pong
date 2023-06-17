import turtle

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
        self.paddle.shapesize(stretch_wid=5, stretch_len=1)
        self.paddle.penup()
        self.paddle.goto(position, 0)

    def move_up(self):
        y = self.paddle.ycor()
        y += 20
        self.paddle.sety(y)

    def move_down(self):
        y = self.paddle.ycor()
        y -= 20
        self.paddle.sety(y)

class Ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(3)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)
        self.ball.dx = 0.2
        self.ball.dy = 0.2

    def update(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball.dy *= -1
        
        if self.ball.ycor() < -290:
            self.ball.sety(-290)
            self.ball.dy *= -1

        if self.ball.xcor() > 390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1
        
        if self.ball.xcor() < -390:
            self.ball.goto(0, 0)
            self.ball.dx *= -1

class PingPongGame:
    def __init__(self):
        self.window = Window(800, 600, "Maatez's PingPong Game", "black")
        self.paddle_a = Paddle(-350)
        self.paddle_b = Paddle(350)
        self.ball = Ball()

        self.window.window.listen()
        self.window.window.onkeypress(self.paddle_a.move_up, "w")
        self.window.window.onkeypress(self.paddle_a.move_down, "s")
        self.window.window.onkeypress(self.paddle_b.move_up, "Up")
        self.window.window.onkeypress(self.paddle_b.move_down, "Down")

    def game_loop(self):
        while True:
            self.ball.update()
            self.window.update()
            
game = PingPongGame()
game.game_loop()