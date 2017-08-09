import turtle
from turtle import *
turtle.setup(700,700)

screen = Screen()
turtle.penup()
def gameOver():
    screenMinX = -screen.window_width()/2
    screenMinY = -screen.window_height()/2
    screenMaxX = screen.window_width()/2
    screenMaxY = screen.window_height()/2
    screen.bgcolor("black")
    goto(0, screenMaxY - 350)
    color('grey')
    write("GAME OVER!!", align="center", font=("Arial",50))

    color('black')
    
    turtle.stamp()
    turtle.register_shape("ppp.gif")
    turtle.shape("ppp.gif")
    turtle.goto(200,-200)
    turtle.stamp()
    
gameOver()
