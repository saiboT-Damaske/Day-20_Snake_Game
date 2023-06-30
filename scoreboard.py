from turtle import Turtle

SCOREBOARD_POS = (0, 270)
ALIGNMENT = "center"
FONT = ('Courier', 15, "normal")


class Score(Turtle):

    def __init__(self):
        self.score_count = 0
        self.highscore = 0
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_POS)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score_count} HIGH SCORE: {self.highscore}", font=FONT, align=ALIGNMENT)

    def point_up(self):
        self.score_count += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score_count > self.highscore:
            self.highscore = self.score_count
        self.score_count = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER\nYour score was: {self.score_count}", font=FONT, align=ALIGNMENT)
