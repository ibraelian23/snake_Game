from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
score_board=ScoreBoard()



screen.listen()
screen.onkey(fun=snake.pointing_upward, key="Up")
screen.onkey(fun=snake.pointing_downward, key="Down")
screen.onkey(fun=snake.pointing_left, key="Left")
screen.onkey(fun=snake.pointing_right, key="Right")


game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# detect collision
    if(snake.snake_head.distance(food) < 15):
        food.refresh()
        snake.extend()
        score_board.increase_score()

# detect collision with wall
    if(snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or snake.snake_head.ycor() < -280):
        # game_is_on=False
        score_board.game_over()
        snake.snake_reset()


# detect collision with tail
    for segment in snake.squares[1:]:
        if(snake.snake_head.distance(segment) < 10):
            # game_is_on = False
            score_board.game_over()
            snake.snake_reset()


screen.exitonclick()
