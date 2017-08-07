import turtle
turtle.setup(700,700)
##num=1
##def fun(x,y):
##    turtle.onclick("right-click")
##    turtle.onclick(fun,btn=1,add=None)
##
##turtle.onkey(fun,"space")
##turtle.listen
##turtle.onclick(turtle.goto)
##print("play game")
##



from turtle import *
screen = Screen()
turtle.penup()

screenMinX = -screen.window_width()/2
screenMinY = -screen.window_height()/2
screenMaxX = screen.window_width()/2
screenMaxY = screen.window_height()/2

screen.bgcolor("black")
goto(0, screenMaxY - 200)
color('grey')
write("The Pita Hero!!", align="center", font=("Arial",20))
goto(0, screenMaxY - 215)
write("Use the arrow keys to move and 'x' to fire katchup and 'y' to fire Falafel", align="center")
turtle.hideturtle()
goto(0,screenMaxY- 350)
write("Play game",align="center",font=("Ariel",20))

#i have to make the go/fire/fire1 functions

screen.onkey(go, 'up')
screen.onkey(fire, 'x')
screen.onkey(fire1,'y')
screen.listen()

play()






