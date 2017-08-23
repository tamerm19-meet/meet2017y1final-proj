import turtle

turtle.tracer(1,0)

turtle.setup(700, 700)

pos_list = []
stamp_list = []

SQUARE_SIZE = 20


player = turtle.clone()
turtle.hideturtle()
turtle.register_shape("pitaBread2.gif")
player.shape('pitaBread2.gif')
player.penup()
player.goto(0,-275)


LEFT_ARROW = "Left" 
RIGHT_ARROW = "Right"
LEFT = 2
RIGHT = 3
IDLE = 0

direction = LEFT

## Dan comment: Make direction that's an idle state - don't move at all

def left ():
    global direction
    if player.pos()[0] > -300:   #dan added
        direction=LEFT
    else:
        direction = IDLE
    move()
def right ():
    global direction
    if player.pos()[0] < 300:  #dan added
        direction=RIGHT
    else:
        direction = IDLE
    move()

turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()


def move():
    global direction
    my_pos = player.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    if direction==RIGHT:
        player.goto(x_pos +SQUARE_SIZE, y_pos)
        print ("You moved right!")
    elif direction==LEFT:
        player.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction == IDLE:
        pass
    
##    #_______________musa start_____________________________
##    if my_pos[0] > -300 and my_pos[0] < 300:
##     #___________________musa end_____________________________
##        if direction==RIGHT:
##            player.goto(x_pos +SQUARE_SIZE, y_pos)
##            print ("You moved right!")
##        elif direction==LEFT:
##            player.goto(x_pos - SQUARE_SIZE, y_pos)
##            print("You moved left!")
##
## #_________________________musa start____________________________           
##    elif my_pos[0] <= -300 or my_pos[0] >= 300:
##        player.goto(x_pos, y_pos)
##        if direction == RIGHT:
##            player.goto(x_pos-25, y_pos)
##        
##        elif direction == LEFT:
## if x_pos + SQUARE_SIZE < 300 and x_pos - SQUARE_SIZE > -300:
##            player.goto(x_pos+25, y_pos)
###__________________________musa end_________________________________


phlaphel = turtle.clone()
turtle.register_shape("Falafel.gif")
turtle.register_shape("ketchup.gif")
phlaphel.shape('Falafel.gif')
phlaphel.penup()

ball_shot = False
def player_shot():
    global ball_shot

    if ball_shot == False:
        shot = player.pos()
        x_pos = shot[0]
        y_pos = shot[1]
        #phlaphel.goto(shot)
        phlaphel.goto(x_pos, y_pos + 20)
        phlaphel.showturtle()
        phlaphel.shape("Falafel.gif")
        ball_shot = True

def ketchup():
    global ball_shot

    if ball_shot == False:
        shot = player.pos()
        x_pos = shot[0]
        y_pos = shot[1]
        #phlaphel.goto(shot)
        phlaphel.goto(x_pos, y_pos + 20)
        phlaphel.showturtle()
        phlaphel.shape("ketchup.gif")
        ball_shot = True

def shotBullet():
    global ball_shot

    if ball_shot == True:
        phlaphel.goto(phlaphel.pos()[0], phlaphel.pos()[1] + 20)

    if phlaphel.pos()[1] >= 300:
        ball_shot = False
    
    turtle.ontimer(shotBullet, 10)

shotBullet()

turtle.onkeypress(player_shot, 'z')
turtle.onkeypress(ketchup, 'x')

turtle.mainloop()    
 
