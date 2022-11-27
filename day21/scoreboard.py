from turtle import Turtle

class Scoreboard(Turtle):
    def __init__ (self):
        super().__init__()
        self.goto(0,280)
        self.color('white')
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.show_scores()
        self.high_score = 0
       

    def increase_l_score(self):
        self.l_score += 1
        self.clear()
        self.show_scores()
       
    def increase_r_score(self):
        self.r_score += 1
        self.clear()
        self.show_scores()

    def show_scores(self):
        self.goto(-100,200)
        self.write(self.l_score, move=False,align='Center',font=('Courier',80,'normal'))
        self.goto(100,200)
        self.write(self.r_score, move=False,align='Center',font=('Courier',80,'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f'GAME OVER!', move=False,align='Center',font=('Courier',12,'normal'))

   