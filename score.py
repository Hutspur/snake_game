from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 12, "bold")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(x=0, y=280)
        self.hideturtle()
        self.color("white")
        self.score_board()

    def score_board(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.score += 1
        self.score_board()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", move=False, align=ALIGNMENT, font=FONT)
