import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

# Setup screen
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

while game_is_on:
    
    screen.update()
    time.sleep(0.15)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh_loc()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.collide_with_wall():
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    # if head collides with any seg. in tail we 
    # triger game over



screen.exitonclick()