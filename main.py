from turtle import Screen
import time
import snake
from food import Food
from score import ScoreBoard

screen = Screen()
screen.title("Snake Legend")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
score_board = ScoreBoard()
snake = snake.Snake()
food = Food()
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

gaming = True
while gaming:
    screen.update()
    time.sleep(0.5)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.update()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        gaming = False
        score_board.game_over()

    # Detect collision with snake body
    for body in snake.squares[1:]:
        if snake.head.distance(body) <= 10:
            gaming = False
            score_board.game_over()


screen.exitonclick()
