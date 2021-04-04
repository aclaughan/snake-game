from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_score()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        message = f"score: {self.score} high score: {self.high_score}"
        self.write(
                message,
                align = ALIGNMENT,
                font = FONT
                )

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_score()
        self.update_scoreboard()

    def save_score(self):
        with open("data", "w") as score_file:
            score_file.write(self.high_score)

    def read_score(self):
        with open("data") as score_file:
            self.high_score = int(score_file.readline())

    def reset(self):
        self.score = 0
        self.update_scoreboard()


    # def game_over(self):
    #     self.home()
    #     self.write("G A M E   O V E R", align=ALIGNMENT, font = FONT)
