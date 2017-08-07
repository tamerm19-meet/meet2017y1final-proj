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
write("The Pita Hero!!", align="center", font=("Arial",50))
goto(0, screenMaxY - 215)
write("CoOl GaMe WiTh CoOl FeAtUrEs...YoU hAvE tO pLaY iT!", align="center")
turtle.hideturtle()
goto(0,screenMaxY- 350)
write("Play game",align="center",font=("Ariel",20))
goto(0,screenMaxY-400)
write("Score table",align="center",font=("Ariel",20))
goto(0,screenMaxY-450)
write("How to play", align="center",font=("Ariel",20))
turtle.register_shape("Falafel.gif")
turtle.shape("Falafel.gif")
turtle.goto(-200, -200)
turtle.stamp()
turtle.register_shape("player.gif")
turtle.shape("player.gif")
turtle.goto(200,-200)
turtle.stamp()
####xclick=0
####yclick = 0
##
##def variables(rawx,rawy):
##    global xclick
##    global yclick
##    xclick = int(rawx//1)
##    yclick = int(rawy//1)
##    print((xclick, yclick))
##
##turtle.onscreenclick(variables)
##
##def check_click():
##    print(xclick, " ", yclick)
##    if xclick >= -75 and xclick <= 75 and yclick > 0 and yclick <= 35:
##        print("game is on")
##
##    turtle.ontimer(check_click, 100)
##
##check_click()


#i have to make the go/fire/fire1 functions

##screen.onkey(go, 'up')
##screen.onkey(fire, 'x')
##screen.onkey(fire1,'y')
##screen.listen()
##play()
