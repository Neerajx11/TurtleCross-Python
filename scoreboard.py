from turtle import Turtle
FONT = ("Courier", 19, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-220, 250)
        self.level = 1
        self.updateScoreboard()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=FONT)

    def levelUp(self):
        self.level += 1

    def gameOver(self):
        self.goto(0, 0)
        self.write("GAMER OVER", align="center", font=FONT)
