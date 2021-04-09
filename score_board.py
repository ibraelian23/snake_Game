from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.score = 0
        with open("data.txt", mode="r") as data:
           self.highest = int(data.read())
        self.write(f"Score : {self.score}  Highest Score : {self.highest}", False, align="center", font=("Arial", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}  Highest Score : {self.highest} ", False, align="center", font=("Arial", 18, "normal"))

    def game_over(self):
        self.highest_score()
        self.clear()
        self.write(f"Score : {self.score}  Highest Score : {self.highest} ", False, align="center", font=("Arial", 18, "normal"))

        # self.goto(0, 0)
        # self.write("Game Over", False, align="center", font=("Arial", 24, "normal"))
        # print(self.highest)

    def highest_score(self):
        if (self.score > self.highest):
            self.highest = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highest}")
        self.score = 0

