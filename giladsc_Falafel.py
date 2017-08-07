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

draw_enemy()

def move_enemy():
    global x_pos, y_pos
    
move_enemy()
            
            








