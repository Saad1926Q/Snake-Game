import turtle

class ScoreBoard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.print_score()

    def print_score(self):
        self.clear()
        self.sety(280)
        self.write(f"Score:{self.score}", align="center", font=("Comic Sans MS", 10, "normal"))

    def game_over(self):
        self.sety(0)
        self.write("Game Over!!!", align="center", font=("Comic Sans MS", 20, "normal"))
