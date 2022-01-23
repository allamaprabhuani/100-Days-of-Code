from turtle import Turtle

ALIGN = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.retrieve_high_score()
        self.hideturtle()
        self.color('white')
        self.up()
        self.setposition(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} | High Score: {self.high_score}', align=ALIGN, font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.setposition(0, 0)
            self.color('turquoise')
            self.clear()
            self.write(f'NEW HIGH SCORE: {self.high_score}!!!', align=ALIGN, font=FONT)
            self.setposition(0, 260)
            self.color('white')
            self.write(f'Score: {self.score} | High Score: {self.high_score}', align=ALIGN, font=FONT)
        else:
            self.update_scoreboard()
        self.score = 0
        self.save_high_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def save_high_score(self):
        with open('highscore.txt', 'w') as f:
            f.write(f'{self.high_score}')

    def retrieve_high_score(self):
        with open('highscore.txt') as f:
            self.high_score = int(f.read())
