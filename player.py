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

direction = LEFT


def left ():
    global direction
    direction=LEFT
    move()
def right ():
    global direction
    direction=RIGHT
    move()

turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)
turtle.listen()


def move():
    my_pos = player.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction==RIGHT:

        player.goto(x_pos +SQUARE_SIZE, y_pos)
        print ("You moved right!")
    elif direction==LEFT:
        player.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    
turtle.mainloop()
