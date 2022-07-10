from swampy.TurtleWorld import *
import math


#q1
# def ahmed_bolt(lap, speed):
#     Turtle.set_delay(ahmed, speed)
#     for i in range(lap*2):
#         fd(ahmed, 100)
#         lt(ahmed, 90)
#         fd(ahmed, 100)
#         lt(ahmed, 90)
# world = TurtleWorld()
# ahmed = Turtle()
# ahmed_bolt(1, .01)
# wait_for_user()


#q2

# Instead of writing this sequence which contains parts that repeat itself

# fd(emre, 40)
# bk(emre, 40)
# lt(emre,90)
# fd(emre,40)
# rt(emre, 90)
# fd(emre, 40)   #i see some lines repeat itself so lets make it a loop
# bk(emre, 40)
# lt(emre, 90)
# fd(emre, 40)
# rt(emre, 90)
# fd(emre, 40)


def write_E(t):

    for i in range(2):
        fd(t, 40)
        bk(t, 40)
        lt(t,90)
        fd(t,40)
        rt(t, 90)
    fd(t, 40)
    # this part positions the turtle for writing the next letter
    pu(t)
    fd(t, 10)
    rt(t, 90)
    fd(t, 80)
    lt(t, 90)
    pd(t)

def write_M(t):
    lt(t, 90)
    fd(t,80)
    rt(t, 140)
    fd(t, 80)
    lt(t, 100)
    fd(t, 80)
    rt(t, 140)
    fd(t, 80)
    # this part positions the turtle for writing the next letter
    pu(t)
    lt(t, 90)
    fd(t, 10)
    pd(t)

def write_R(t):
    lt(t, 90)
    fd(t, 60)
    for i in range(40):
        rt(t, 8)
        fd(t, 3)
    bk(t,70)
    rt(t,130)


def write_EMR(t):
    write_E(t)
    write_M(t)
    write_R(t)
    # If you want to write a EMRE
    # write_E(t)


# world = TurtleWorld()
# emre = Turtle()
# # position the turtle
# pu(emre)
# bk(emre,150)
# pd(emre)
# Turtle.set_delay(emre, 0.1)
# write_EMR(emre)
# wait_for_user()



#q3
def get_count(n):
    for j in range(n, -1, -1):
        print(j)

    for i in range(0, n+1):
        print(i)

# get_count(10)


# Additional exercise with one loop creating a mirror image of numbers around zero
def get_count_v2(n):

    for i in range(n*2,-1,-1):
        print abs(i-n)

# print("get_count_v2: ")
# get_count_v2(10)


#q4
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

def polygon(t, n, length):
    angle = 360.0/n
    polyline(t, n, length, angle)


def polyline(t, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def arc(t, r, angle):
    arc_length = 2 * math.pi * r * abs(angle) / 360
    # print arc_length
    n = int(arc_length / 4)+ 1
    # print n
    step_length = arc_length / n
    step_angle = float(angle) / n
    # print step_length*n, step_angle
    # making a slight left turn before starting reduces
    # the error caused by the linear approximation of the arc
    lt(t, step_angle/2)
    polyline(t, n, step_length, step_angle)
    rt(t, step_angle/2)



def drawSnowman(t, h):
    unit = h/9
    arc(t, 4*unit, 360)
    arc(t,4*unit,180)
    lt(t,180)
    arc(t, 3*unit, 360)
    arc(t,3*unit,180)
    lt(t,180)
    arc(t, 2 * unit, 360)
    lt(t,180)
    arc(t, 3 * unit, 180)
    lt(t, 180)
    arc(t, 4 * unit, 180)

# world = TurtleWorld()
# bob = Turtle()
# Turtle.set_delay(bob, 0.01)
# #polygon(bob,5,100)
# position_2(bob)
# # arc(bob,50,360)
# drawSnowman(bob,180)
# wait_for_user()






#q5
def sum_all(n):
    sum = 0
    for i in range(0,n+1,1):
        sum = sum +i
    print sum
# sum_all(10)

#q6
def print_all_even(n1, n2):
    for i in range(n1+2,n2,2):
        print i
# print_all_even(2,10)


#q7
#Error
#True
#True
#False
#False
#Error
#True
#True
#Error

# a = 4
# b = 6
# c = 4
# #print(a = 2) #SyntaxError: invalid syntax
# print(b > 2)
# print(a >= c)
# print(a > b)
# print(b < a)
# #print(a = b) # SyntaxError: invalid syntax
# print(a <= c)
# print(a != b)
# #print(a =< c) # SyntaxError: invalid syntax



#q8
def negatives(n):
    for i in range(0, n - 1, -1):
        print(i)
# negatives(-10)


#q9
def tens_mult(n):
    for i in range(1,11):
        print(i* n)
# tens_mult(10)


#q10
def create_for(a, b):
    max_num = max(a, b)
    min_num = min(a, b)
    for i in range(min_num, max_num + 1):
        print(i)
# create_for(5,1)

#q11
#prints nothing!
# Because the step is 1 and we are iterating negative numbers.
# for i in range(-1, -10, 1):
#     print(i)

# however this will work
# #for i in range(-10, -1, 1):
#     print(i)

#q12
# a = 2
#
# for i in range(a):
#     print(a == 2)





#q13
def triangle_left():
    for i in range(30):
        print((i+1) * '.')
# triangle_left()

#q14

def triangle_right():
    space = 30
    for i in range(30):
        print space * " " + (i+1)* '.'
        space = space - 1
# triangle_right()

#q15
# a = 1
# space = 21
# for i in range(21):
#     print(a * '.' + space * " " +space*" "+ a * '.')
#     a = a + 1
#     space = space - 1
# OR

def two_triangles():
    a = 1
    space = 40
    for i in range(21):
        print(a * '.' + space * " " + a * '.')
        a = a + 1
        space = space - 2
# two_triangles()



#q16
# Prototype v1:

# sayi = 0
# bosluk = 0
# for i in range(1):
#     for i in range(30):
#         sayi = sayi +1
#         bosluk = 30-sayi
#         print sayi*"." + 2*bosluk*" " + sayi*"."
#
#     for i in range(30):
#         sayi = sayi-1
#         bosluk = 30-sayi
#         print sayi*"." + 2*bosluk*" " + sayi*"."

def pattern(n_rep):
    dot = 0
    space = 0
    for i in range(n_rep):
        size = 30
        for i in range(size):
            dot = dot + 1
            space = size - dot
            print dot*"." + 2*space*" " + dot*"."

        # dot = dot + 1
        # space = space-2
        for i in range(size):
            dot = dot-1
            space = size-dot
            print dot*"." + 2*space*" " + dot*"."

# pattern(2)
