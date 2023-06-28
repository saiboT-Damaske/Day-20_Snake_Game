import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Wer hat die längste Schlange?")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        print("mmmhhhhmmhh")
        food.refresh()
        snake.extend()
        score.point_up()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # detect tail collision
    # if head collides with any tail segment
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
