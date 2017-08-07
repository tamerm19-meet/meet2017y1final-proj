import turtle
turtle.tracer(1,0)
mouth=turtle.clone()
turtle.hideturtle()
turtle.setup(700,700)
turtle.penup()
mouth.penup()

stamp_list=[]
stamp_pos_list=[]
shot_pos=[]

turtle.register_shape("mouth.gif")
mouth.shape("mouth.gif")
turtle.bgcolor("black")

###################
def draw_enemy():
    y_pos=-100
    for number_in_rows in range(0,5):
        x_pos=-300
        for row in range (0,20):
            mouth.stamp()
            mouth_stamps=mouth.clone()
            mouth_stamps.goto(x_pos,y_pos)
            stamp_list.append(mouth_stamps)
            stamp_pos_list.append(mouth_stamps.pos)
            x_pos+=30
        y_pos+=50
draw_enemy()

def move_enemy():
    y2_pos=0
    x2_pos=-30
    while shot_pos in stamp_pos_list!=True:
        mouth_stamps.goto(x2_pos,y2_pos)
        x2_pos+=60
        while shot_pos in moth_stamo_pos==False:
            mouth_stsamps.goto(x2_pos,y2_pos)
            x2_pos-=60
move_enemy()
    
    
    





