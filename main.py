import time
from turtle import Screen
from snake import Snake
from food import Food
from score import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.title('My snake game')
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.listen()
screen.onkey(key='a', fun=snake.left)
screen.onkey(key='s', fun=snake.down)
screen.onkey(key='d', fun=snake.right)
screen.onkey(key='w', fun=snake.up)

game_is_on = True
while game_is_on:
    snake.move()
    time.sleep(0.1)

    # Detect collision with food
    if snake.head.distance(food.pos()) <= 20:
        food.reset_pos()
        snake.extend()
        score_board.add_score()

    # Detect Collision with wall
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        score_board.reset()
        snake.reset_snake()

    # Detect Collision with body
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score_board.reset()
            snake.reset_snake()

    screen.update()

screen.exitonclick()
