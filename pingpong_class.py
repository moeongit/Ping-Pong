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

class PingPongGame:
    def __init__(self):
        self.window = Window(800, 600, "Maatez's PingPong Game", "black")
        self.paddle_a = Paddle(-350)
        self.paddle_b = Paddle(350)
    
    def game_loop(self):
        while True:
            self.window.update()
            
game = PingPongGame()
game.game_loop()