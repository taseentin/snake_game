from turtle import Turtle

class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 230)
        self.write(arg=f"Score : {self.score}", align="center", font= ("Arial", 18, "normal"), move=False)

    def hitt(self):
        self.clear()
        self.score+=1
        self.write(arg=f"Score : {self.score}", align="center", font=("Arial", 18, "normal"), move=False)
    def game_over(self):
        self.color("white")
        self.goto(0, 0)
        self.write(arg=f"GAME OVER!!!!!!!:(", align="center", font=("Arial", 18, "normal"), move=False)