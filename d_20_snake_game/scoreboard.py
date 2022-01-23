from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.up()
        self.setposition(0, 280)
        self.score = 0

    def update(self):
        self.write(f'Score: {self.score}', align='center', font=('Georgia', 14, 'bold'))

    def increase_score(self):
        self.clear()
        self.update()
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=('Arial', 14, 'bold'))
