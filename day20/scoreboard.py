from turtle import Turtle

class Scoreboard(Turtle):
    def __init__ (self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.goto(0,280)
        self.display()
        self.color('white')
        self.hideturtle()
      
    def increase_score(self):
        self.score += 1
        self.clear()
        self.display()

    def display(self):
        self.clear()
        self.write(arg=f'Score: {self.score} High Score {self.high_score}', move=False,align='Center',font=('Courier',12,'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f'GAME OVER!', move=False,align='Center',font=('Courier',12,'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(f'{self.high_score}'))