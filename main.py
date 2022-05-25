from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


def toggle_pause():
    global game_is_paused
    if game_is_paused:
        game_is_paused = False
    else:
        game_is_paused = True


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(toggle_pause, "space")

game_is_on = True
game_is_paused = False

while game_is_on:
    if not game_is_paused:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            score.add_point()

        # Detect collision with wall
        if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
            score.reset()
            snake.reset()

        # Detect collision with tail
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                score.reset()
                snake.reset()
    else:
        screen.update()


screen.exitonclick()
