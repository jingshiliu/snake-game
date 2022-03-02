from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Times New Roman', 24, 'normal')
TEXT_COLOR = 'pink'


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score') as best_score:
            self.high_score = int(best_score.read())
        self.penup()
        self.hideturtle()
        self.speed('fastest')
        self.goto(0, 270)
        self.color(TEXT_COLOR)
        self.display_score()

    def add_score(self):
        self.score += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open('high_score', mode='w') as best_score:
                best_score.write(str(self.high_score))
        self.display_score()
        self.score = 0

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game Over.", align=ALIGNMENT, font=FONT)
