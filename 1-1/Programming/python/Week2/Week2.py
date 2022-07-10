"""
Week 2 Lecture script
"""

#Check and set your current directory
import os
cwd=os.getcwd() #This is your current working directory
print cwd

import os
preferred_dir="C:\Users\Mujde\Documents\ISTANBUL_SEHIR_UNI" \
              "\ENGR 101_SPRING 2018_HMA\Week 2" #Please set yours properly
os.chdir(preferred_dir) #Now you have changed your working directory to your preferred directory
#as you defined above. Please set yours properly!
cwd=os.getcwd()
print cwd

#SLIDE 4: Variables
pi = 3.1415926535897931
print pi
print type(pi)

#SLIDE 5:Integer vs. Float Division
print 3/5
print 5/3
print 6/3
print 6/4

print 3/5.0
print 5.0/3
print 6.0/3.5
print 6/4.0

#SLIDE 8:Order of operations
print 4*5-1/3/2*9+1
print (4*5)-((1/3/2)*9)+ 1
print (4*5)-((1/3)/(2*9))+ 1
print (4*5)-((1/3.0)/(2.0*9))+ 1

#SLIDE 9: String operations
print 'a'+'b'
print "a"*3

#SLIDE 15: Functions
def testing():
    print "This is week 2."
    print "We are studying functions."
testing()



def repeat_function():
    testing()
    print "break"
    testing()
repeat_function()

#SLIDE 19: Functions with arguments
def print_twice(x):
    print x
    print x

print_twice('ENGR 211')

import math
print math.sin(90*pi/180) #Built in function with 1 argument
print math.pow(2,3) #Built in function with 2 arguments

#SLIDE 20: Arguments and local variables in functions
def student(first,last): #first and last are arguments
    full = first + " " + last #local variable
    print_twice(full) # was defined before

name1 = "red"
name2 = "kit"
student(name1, name2)


print full #should give error as was local variable

def print_twice(x):
    print x
    print x
    print full #should give error as was local variable

print_twice('ENGR 211')

#SLIDE 23: Type Conversion
print int("32")
print type(int("32"))

print int("hello")#error
print int("2.39") #error
print round(float("2.39"))

print float(32)
print str(32.45)
print type(str(32.45))

#SLIDE 24-25: Math function
import math
print math.sqrt(4)

degrees=90
x = math.sin(degrees/360.0 * 2 * math.pi)
print x

#SLIDE 26:Exercise 5 – Part 1 (Chapter 3)
print 3,4 #side to side print
print 3,"\n",4 #print in a new line
print 3,"\t",4 #tab distance


print "printing"+"\n"+"test" #print in a new line
print "printing"+"\t"+"test" #two words seperated by a tab
print "printing"+"this"+"test" #side by side

print 2+"students" #error
print str(2)+"students"
print str(2)+" students"
print str(2)+" "+"students"

#Exercise
def do_twice(f): # A function that takes a function as an argument and calls it TWICE
    f()
    f()

def do_four(f):# A function that takes a function as an argument and calls it FOUR TIMES
    do_twice(f)
    do_twice(f)

def print_beam():
    print '+ - - - - -',

def print_post():
    print '|          ',

def print_beams(): #one line of beam done
    do_twice(print_beam)
    print '+'


def print_posts():#middle line done
    do_twice(print_post)
    print '|'

def print_row(): #top halve done
    print_beams() #what it does is actually below three lines, leave it commented please
    #print '+ - - - - -',
    #print '+ - - - - -',
    #print '+'
    do_four(print_posts)

def print_grid():#totally done
    do_twice(print_row)
    print_beams() #last row

print_grid()

#SLIDE 27:Further Exercises
"""
1. Write a function that takes a string and an integer
as input (string, y). The function should print the string y times,
and each time the string should be written in a new line.

e.g: print_str('exercise',3) should return below:
exercise
exercise
exercise

"""
def print_str(my_str,y):
    z=my_str+"\n"
    w=z*y
    print w
print_str('exercise',3)


"""
2. Write a function called percentage that takes the percentage for two given numbers.

e.g: percentage(80,60,25) should return:
25% of 80 is 20.0
25% of 60 is 15.0
"""
def percentage(number1,number2,per):
    first = number1*per/100.0
    second = number2*per/100.0
    print str(per) + "% of " + str(number1) + " is " + str(first)
    print str(per) + "% of " + str(number2) + " is " + str(second)
percentage(80,60,25)

"""
3.Write a function that takes four arguments x1, y1, x2, y2 where each
(x, y) pair refers to a point on a 2D Cartesian plane and prints the distance between the two points
(x1, y1)and(x2, y2). You are encouraged to use functions from the math module.

e.g. cartes(3,4,5,6) should give 2.828
"""
def cartes(x1,y1,x2,y2):
    import math
    distance=math.sqrt((x1-x2)**2+(y1-y2)**2)
    print (distance)
cartes(3,4,5,6)