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


