import turtle
import time

turtle.tracer(1,0)
mouth=turtle.clone()
turtle.hideturtle()
turtle.setup(700,700)
turtle.penup()
mouth.penup()

clones_list=[]
clones_pos_list=[]
shot_pos=[]

TIME_STEP=1000

turtle.register_shape("mouth.gif")
mouth.shape("mouth.gif")
turtle.bgcolor("black")

x_pos = -300
y_pos = -100

def draw_enemy():
    global x_pos, y_pos
    for row in range(0,5):
        x_pos=-300
        y_pos+=50
        mouth.setposition(x_pos,y_pos)
        for column in range (0,10):
            if column != 0:
                x_pos += 60
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

            
            








