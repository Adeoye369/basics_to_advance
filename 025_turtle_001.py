from turtle import Turtle, Screen

tur = Turtle()
screen  = Screen()


def turn_left():
    new_heading = tur.heading() + 10
    tur.setheading(new_heading) # or tur.left(10)

def turn_right():
    new_heading = tur.heading() - 10
    tur.setheading(new_heading) # or tur.right(10)

def clear():
    tur.clear()
    tur.penup()
    tur.home()


screen.listen()

# onkey is a higher order function, it takes in other functions
screen.onkey(key="d", fun=lambda : tur.forward(10)) 
screen.onkey(key="a", fun=lambda : tur.backward(10)) 
screen.onkey(key="s", fun=turn_left) 
screen.onkey(key="w", fun=turn_right) 
screen.onkey(key="c", fun=clear) 
screen.exitonclick()