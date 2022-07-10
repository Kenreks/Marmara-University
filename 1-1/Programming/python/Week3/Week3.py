"""
Week 3 Lecture script
"""

#Check and set your current directory
import os
cwd=os.getcwd() #This is your current working directory
print cwd

import os
preferred_dir="C:\Users\Mujde\Documents\ISTANBUL_SEHIR_UNI" \
              "\ENGR 101_SPRING 2018_HMA\Week 3" #Please set yours properly
os.chdir(preferred_dir) #Now you have changed your working directory to your preferred directory
#as you defined above. Please set yours properly!
cwd=os.getcwd()
print cwd

# SLIDE 13:
# import everything in TurtleWorld module in swampy package
from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
fd(bob,100) # move forward 100 units (pixels)
lt(bob, 90) # turn 90 degrees left
fd(bob,100) # move forward 100 units (pixels)
wait_for_user()

# SLIDE 14&15:
#Modify the program to draw a square.
from swampy.TurtleWorld import * #It is ok to import this once at the beginning of the script
world = TurtleWorld() #It is ok to create this once
bob = Turtle()  #It is ok to create this once
fd(bob,100) # move forward 100 units (pixels)
lt(bob) # turn by default 90 degrees left
fd(bob,100) # move forward 100 units (pixels)

lt(bob) # turn 90 degrees left
fd(bob,100) # move forward 100 units (pixels)

lt(bob) # turn 90 degrees left
fd(bob,100) # move forward 100 units (pixels)
lt(bob, 60) # turn 60 degrees left
wait_for_user()

#Slide 17:
for i in range(4):
    print "Hello"

#Slide 18&19:For loop syntax
for i in range(0,4,1):
    print i

for i in range(0,4):
    print i

for i in range(0,4,2):
    print i

for i in range(4):
    print i

#Slide 21:Let the turtle draw square using for loop
from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
for i in range(4):
    fd(bob,100)
    lt(bob)
wait_for_user()

# Slide 23: Encapsulation
# draw a square of size 100
def square(t):
    for i in range(4):
        fd(t, 100)
        lt(t)

from swampy.TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
square(bob)
wait_for_user()

# Slide 26: Generalization
# Draw a square of size length; the length parameter to be given by the user
def square(t, length):
    for k in range(4):
        fd(t, length)
        lt(t)
    wait_for_user()
from swampy.TurtleWorld import *
world = TurtleWorld()
ray = Turtle()
square(ray, 60)


# Slide 28: Generalization
# draw a polygon with n edges of a given size
def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)
    wait_for_user()

from swampy.TurtleWorld import *  # It is ok to create this once
world = TurtleWorld()  # It is ok to create this once
my_turtle = Turtle()

polygon(my_turtle,n=4,length=100)# This draws a 7-sided polygon with side length 70.

# Slide 29: Generalization
#polygon(t=my_turtle,n=8,length=70)# This draws a 7-sided polygon with side length 70.


# Slide 31: Exercise 3
def digits(a,b,c,d):
    num=int(str(a)+str(b)+str(c)+str(d))/c
    print num
digits(1,2,3,5)

# Slide 32: Exercise 4
def print_even(even1,even2):
    for i in range(even1+2,even2,2):
        print i
print_even(12,18)



# Slide 33: Exercise 5

def print_right_tri(num_rows):
    for j in range(num_rows):
         x='.'*j
         y=" "*(num_rows-j-1)#-1 to leave less space on LHS at the bottom line
         print y,x
print_right_tri(5)
print_right_tri(10)

# Slide 34: Exercise 6

def write_M (my_turtle):
    import math
    lt(my_turtle,90)
    fd(my_turtle, 100)
    rt(my_turtle,90+45)
    fd(my_turtle, 100*math.sqrt(2))
    lt(my_turtle,90)
    fd(my_turtle, 100*math.sqrt(2))
    rt(my_turtle,90+45)
    fd(my_turtle, 100)
    wait_for_user()

from swampy.TurtleWorld import *
world = TurtleWorld()
turtie = Turtle()
write_M(turtie)

def write_U (my_turtle):
    lt(my_turtle,90)
    fd(my_turtle, 100)
    rt(my_turtle,180)
    fd(my_turtle, 100)
    lt(my_turtle,90)
    fd(my_turtle, 100)
    lt(my_turtle,90)
    fd(my_turtle, 100)
    wait_for_user()
from swampy.TurtleWorld import *
world = TurtleWorld()
turtie = Turtle()
write_U(turtie)