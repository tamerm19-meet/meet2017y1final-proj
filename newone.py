
import turtle

xclick = 0
yclick = 0

def click():
    turtle.onscreenclick(variables) 

def variables(rawx,rawy):
    global xclick
    global yclick
    xclick = int(rawx//1)
    yclick = int(rawy//1)
    print(xclick)
    print(yclick)

click()
