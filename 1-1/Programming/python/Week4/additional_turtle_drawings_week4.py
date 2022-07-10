
from swampy.TurtleWorld import *
import math

# ----------- ADDITIONAL DRAWING EXAMPLES --------------
#You are encouraged to experiment and come up with various shapes as below
def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)


def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    n = int(arc_length / 4) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n

    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)

def position_1(t):
    pu(t)
    fd(t,500)
    rt(t)
    fd(t,100)
    lt(t)
    pd(t)

def position_2(t):
    pu(t)
    fd(t,500)
    rt(t)
    fd(t,100)
    lt(t)
    rt(t,90)
    fd(t,350)
    lt(t)
    pd(t)

def shape(t):
    x = 0.7
    y = 0.3
    for i in range(250):
        lt(t,10)
        #print mod
        #arc(bob,50,360)
        fd(t,y)
        polygon(t,5,x)
        x+=0.7
        y+=0.4

def shape2(t):
    x = 0.7
    y = 0.3
    for i in range(144):
        mod = i+1%6
        lt(t,10)
        #print mod
        arc(t,50,360)
        fd(t,20)
        polygon(t,mod,x)
        x+=1
        y+=2

def shape3(t):
    x = 20
    y = 10
    for i in range(250):

        lt(t,x)
        arc(t,x,360)
        #polygon(t,5,x)
        x+=5
        y+=5




# world = TurtleWorld()
# bob = Turtle()
# Turtle.set_delay(bob, 0.0000000000001)
# position_1(bob)
# shape(bob)
# wait_for_user()
#
# world2 = TurtleWorld()
# rob = Turtle()
# Turtle.set_delay(rob, 0.0000000000001)
# set_color(rob,'yellow')
# set_pen_color(rob,'red')
# position_1(rob)
# shape2(rob)
# wait_for_user()
#
# world3 = TurtleWorld()
# tob = Turtle()
# Turtle.set_delay(tob, 0.0000000000001)
# position_1(tob)
# shape3(tob)
# wait_for_user()



def fibonacci_circles(t):
    x = 1
    y = 1

    for i in range(15):
        z = x+y
        arc(t,z,360)
        lt(t,10)
        temp = x
        x = y
        y = temp + y

def fibonacci_squares(t):
    x = 1
    y = 1
    for i in range(15):
        z = x + y
        print z
        fd(t, z)
        lt(t, 90)
        for i in range(2):
            fd(t, y)
            lt(t, 90)
            fd(t, z)
            lt(t, 90)
        temp = x
        x = y
        y = temp + y





world3 = TurtleWorld()
tob = Turtle()
Turtle.set_delay(tob, 0.0000000000001)
position_2(tob)
fibonacci_circles(tob)
wait_for_user()

# world4 = TurtleWorld()
# bot = Turtle()
# Turtle.set_delay(bot, 0.0000000000001)
# position_1(bot)
# fibonacci_squares(bot)
# wait_for_user()

def special(t):
    degree = 360
    r=100
    x = 1
    for i in range(180):

        rt(t, 10)
        # fd(t,20)
        arc(t,x,360)

        if x<60:
            x+=1

        elif x<90:
            x+=1.5

        else:
            x+=2


def special2(t):
    x = 1
    for i in range(180):

        rt(t, 10)
        # fd(t,20)
        # polygon(t,7,100)

        polygon(t,9,i)
        # polygon(t,9,x)
        # x+=1.5



# world4 = TurtleWorld()
# bot = Turtle()
# Turtle.set_delay(bot, 0.01)
# position_1(bot)
# special2(bot)
# wait_for_user()
