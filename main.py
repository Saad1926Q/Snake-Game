from turtle import Screen,Turtle
import snake
import time
import food
import scoreboard
screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake=snake.Snake()
food=food.Food()
score_board=scoreboard.ScoreBoard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        score_board.score+=1
        score_board.print_score()

    #detect collision with wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>280 or snake.head.ycor()<-290:
        game_is_on=False
        score_board.game_over()

    for segment in snake.segments:
        if segment!=snake.head:
            if snake.head.distance(segment)<10:
                game_is_on=False
                score_board.game_over()

screen.exitonclick()