import turtle
#import time
import random

turtle.tracer(1,0)
mouth=turtle.clone()
mouth_shot=turtle.clone()
turtle.hideturtle()
turtle.setup(700,700)
turtle.penup()
mouth.penup()

clones_list=[]
clones_pos_list=[]
shot_stamp_pos=[]

TIME_STEP=500

turtle.register_shape("mouth.gif")
mouth.shape("mouth.gif")
turtle.bgcolor("black")

x_pos = -300
y_pos = -100

def draw_enemy():
    global x_pos, y_pos
    for row in range(0,5):
        x_pos=-280
        y_pos+=50
        mouth.setposition(x_pos,y_pos)
        for column in range (0,14):
            if column != 0:
                x_pos += 40
                mouth.goto(x_pos, y_pos)
                
            mouth_clone=mouth.clone()
            clones_list.append(mouth_clone)
            clones_pos_list.append(mouth_clone.pos()) 
    mouth.hideturtle()
draw_enemy()
count = 0
def move_enemy_right():
    global count
    for clone in clones_list:
        (x_pos,y_pos) = clone.pos()
        clone.goto(x_pos+10,y_pos)

    count += 1
    if count%5==0:
        move_enemy_left()
    else:
        turtle.ontimer(move_enemy_right,TIME_STEP)

def move_enemy_left():
    global count
    for clone in clones_list:
        (x_pos,y_pos) = clone.pos()
        clone.goto(x_pos-10,y_pos)

    count+=1
    if count%5==0:
        move_enemy_right()
    else:
        turtle.ontimer(move_enemy_left,TIME_STEP)

move_enemy_right()

############################
mouth_shot.color("yellow")
def enemy_shot():
    mouth_shot_clones=mouth_shot.stamp()
    shot_stamp_pos.append(mouth_shot_clones)
    mouth_shot_clones=random.randint(0, len(clones_pos_list)-1
                                     
enemy_shot()
##    random.randint(shot_pos)=random.randint(clones_pos_list)
##    
##enemy_shot()
##
##def enemy_shot_movement():
##    mouth_shot.backward()                             
            








