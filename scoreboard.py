from turtle import Turtle

filename = "data.txt"

ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        with open(filename, mode="r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.current_score}  High score: {self.high_score}", align=ALIGNMENT, font=FONT)


    def add_point(self):
        self.clear()
        self.current_score += 1
        self.update_scoreboard()

    def reset(self):
        if self.current_score > self.high_score:
            self.high_score = self.current_score
            with open(filename, mode="w") as data:
                data.write(str(self.current_score))
        self.current_score = 0
        self.update_scoreboard()
