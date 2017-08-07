import turtle

turtle.tracer(1, 0)

#How big the python shell window is:
SIZE_X=700
SIZE_Y=700
turtle.setup(SIZE_X, SIZE_Y)

turtle.hideturtle()
turtle.bgcolor("black")
#Edges and Borders:

UP_EDGE = 300
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
turtle.register_shape("starvingKids.gif")
starving_kid1=turtle.clone()
starving_kid1.shape("starvingKids.gif")
starving_kid1.pu()
starving_kid1.showturtle()
starving_kid1.goto(0, 310)

#score:
def score():
    score_turtle=turtle.clone()
    score_turtle.hideturtle
    score_turtle.pu()
    score_turtle.goto(0, 0)
    score_turtle.showturtle()
    score_turtle.color("white")
    score_turtle.goto(-330, 305)
    score_turtle.write("Score:", font=("Arial", 24, "normal"))
    score_turtle.goto(-230, 305)
    #n is the SCORE! this IS IMPORTANT!
    score_turtle.write(n, font=("Aerial", 24, "normal"))

    
score()

def accessories():
    turtle_acc=turtle.clone()
    turtle_acc.pu()
    turtle_acc.goto(-350, -350)


























