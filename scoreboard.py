from turtle import Turtle

SCOREBOARD_POS = (0, 270)
ALIGNMENT = "center"
FONT = ('Courier', 15, "normal")



class Score(Turtle):

    def __init__(self):
        self.score_count = 0
        with open("high_score_data.txt", "r") as high_score_file:
            self.high_score = int(high_score_file.read())
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(SCOREBOARD_POS)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score_count} HIGH SCORE: {self.high_score}", font=FONT, align=ALIGNMENT)

    def point_up(self):
        self.score_count += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score_count > self.high_score:
            self.high_score = self.score_count
        self.score_count = 0
        with open("high_score_data.txt", "w") as high_score_file:
            high_score_file.write(f"{self.high_score}")

    def game_over(self):
        print("game over")
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER\nSCORE: {self.score_count} \nHIGH SCORE:{self.high_score}", font=FONT, align="center")
        self.goto(SCOREBOARD_POS)
