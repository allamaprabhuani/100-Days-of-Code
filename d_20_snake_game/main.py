import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Ani\'s snake game')
screen.tracer(0)
SCREEN_EDGE = 290

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.2)
    # for seg in segments:
    #     seg.forward(20)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()

    # Detect collision with walls
    if snake.head.xcor() > SCREEN_EDGE or snake.head.xcor() < -SCREEN_EDGE or snake.head.ycor() > SCREEN_EDGE \
            or snake.head.ycor() < -SCREEN_EDGE:
        scoreboard.game_over()
        game_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            scoreboard.game_over()
    # if head collides with any segment in the tail:
    # trigger game_over

screen.exitonclick()
