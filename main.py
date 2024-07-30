from turtle import Turtle, Screen

tim = Turtle()


def move_fd():
    tim.forward(10)


def move_bd():
    tim.back(10)


def turn_cl():
    tim.right(0 + 10)


def turn_ccl():
    tim.left(0 + 10)




screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_fd)
screen.onkey(key="s", fun=move_bd)
screen.onkey(key="d", fun=turn_cl)
screen.onkey(key="a", fun=turn_ccl)
screen.onkey(key="c", fun=screen.clear)
screen.onkey(key="c", fun=tim.reset)
screen.exitonclick()
