
import turtle

turtle.tracer(1, 0)

#How big the python shell window is:
SIZE_X=700
SIZE_Y=700
turtle.setup(SIZE_X, SIZE_Y)

turtle.hideturtle()
turtle.bgcolor("black")
#Edges and Borders:

UP_EDGE = 300s
DOWN_EDGE = -300
RIGHT_EDGE = 300
LEFT_EDGE = -300

edgy_turtle=turtle.clone()
edgy_turtle.speed(0)
edgy_turtle.hideturtle()
edgy_turtle.color("white")
edgy_turtle.penup()

##############################################################################

def create_border():
    edgy_turtle.pensize(10)

    edgy_turtle.goto(UP_EDGE, RIGHT_EDGE)

    edgy_turtle.pendown()
    
    edgy_turtle.right(90)
    for i in range (4):
        edgy_turtle.forward(600)
        edgy_turtle.right(90)
        
create_border()

#This is the starving kid:
def starving_kid():
    turtle.register_shape("starvingKids.gif")
    starving_kid1=turtle.clone()
    starving_kid1.shape("starvingKids.gif")
    starving_kid1.pu()
    starving_kid1.showturtle()
    starving_kid1.goto(30, 310)
starving_kid()
#score:
n = 0
def score():
    score_turtle=turtle.clone()
    score_turtle.hideturtle
    score_turtle.pu()
    score_turtle.color("white")
    score_turtle.goto(-295, 305)
    score_turtle.write("Score: " + str(n), font=("Arial", 24, "normal"))

    
score()

def accessories():
    acc = turtle.clone()
    acc.showturtle()
    acc.color("white")
    acc.hideturtle()
    acc.pu()
    acc.goto(-350, -300)
    acc.pd()
    acc.pensize(10)
    acc.goto(-300, -300)
    acc.goto(-300, -350)
    acc.pu()
    acc.goto(350, -300)
    acc.pd()
    acc.goto(300, -300)
    acc.goto(300, -350)
    acc.pu()
    acc.goto(-350, 300)
    acc.pd()
    acc.goto(-300, 300)
    acc.goto(-300, 350)
    acc.pu()
    acc.goto(350, 300)
    acc.pd()
    acc.goto(300, 300)
    acc.goto(300, 350)
accessories()

clockVar = 0

def clock():
    global clockVar
    clockVar += 1

    checkClock()
    turtle.ontimer(clock, 1000)

def checkClock():
    global clockVar
    if clockVar == 2:
        quit()

clock()

h=0
def highscore():
    high=turtle.clone()
    high.color("white")
    high.hideturtle()
    high.pu()
    high.goto(-290, -340)
    high.write("Highscore: " + str(h), font=("Aerial", 24, "normal"))

highscore()

############################################################################


