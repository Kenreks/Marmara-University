
# ENGR 101 Introduction to Programming
# Practice Session Week 5

from swampy.TurtleWorld import *
import math

# ex.1

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

# ex.2
def count_ind(x):
    while True:
        i = 0
        while i<x:
            print i,
            i+=1
        i-=1
        while i > -1:
            print i,
            i-=1
        print ''

# count_ind(4)

# ex.3
def counter(x):
    k=0
    count=0
    a=0
    while a<10:
        while k<x:
            print k,
            k+=1

        while k>0:
            k-=1
            print k,
        count += 1
        print "Turn : " + str(count)
        a +=1
# counter(4)

def counter_v2(x):
    turns = 10
    for i in range(1, turns+1):

        for j in range(x):
            print j,

        for k in range(x-1, -1, -1):
            print k,

        print " Turn : " + str(i)

# counter_v2(4)

# ex.4

def valid_input(var):
    if var == 1:
        print "True"
    elif var == 0:
        print "False"
    else:
        print "Invalid Input"

# valid_input(1)

# ex. 5
def is_string(x, y, z):
    if type(x) == str:
        print x + " is a string"

    if type(y) == str:
        print y + " is a string"

    if type(z) == str:
        print z + " is a string"


# is_string("hello",2,"5")

# ex.6
def isIsosceles(x, y, z):
    if x == y or x == z or y == z :
        print "True"
     #   return True

# isIsosceles(12,12,11)

# ex. 7
def power_of_two(x):
   a=0
   while a<x:
       print 2**a
       a+=1
# power_of_two(10)

# ex. 8
from swampy.TurtleWorld import *

def forward(t):
    size = 50
    fd(t, size)
    fd(t, size)
    bk(t, size)
    fd(t, size)
    fd(t, size)

def mehter_walk(t):
    while True:
        forward(t)
        lt(t, 90)

# world = TurtleWorld()
# bob = Turtle()
# Turtle.set_delay(bob, 1)
#
# mehter_walk(bob)
# wait_for_user()


# ex.9
def speed_up(t,speed):
    x=0
    while x<speed: # while True: (would mean loop infinitely)
        x+=1
        Turtle.set_delay(t, 1.0/x)

        for i in range(4):
            fd(t, 80)
            lt(t, 90)

# world = TurtleWorld()
# rob = Turtle()
# speed_up(rob, 1000)
# wait_for_user()

# ex.10
def useless(x):
    a = x
    while a>0:
        a-=1
        if a==20:
            a=100
        print a
# useless(100)

# ex.11
def thing_1(thing1):
    if thing1 >10:
        print "OKEY"
    else:
        print "NOT OKEY"

def thing_2(thing1):
    if thing1 > 10:
        print "This is first"
    if thing1 < 25:
        print "this is second"
    else:
         print "This is third"

thing1 = 20
# thing_1(thing1)
# thing_2(thing1)


# ex.12

# x=True
# y=False
# z=True
# if x==y or z!=x :
#     print "First Condition"
# elif x==z and y!=z:
#     print "Second Cndition"
#
# Second Condition is the answer

# ex. 13
def max_num(x, y, z):
    if x>y:
        if x>z:
           print x

    elif y>z:
        print y

    else:
        print z
# max_num(1, 4, 3)

# ex.14:
def percentage_to_letter(n):
    if n>=80 and n<=100:
        print "Letter grade for " + str(n) + "%" + " is A"
    elif n>=70 and n<=79:
        print "Letter grade for " + str(n) + "%" + " is B"
    elif n>=60 and n<=69:
        print "Letter grade for " + str(n) + "%" + " is C"
    elif n>=50 and n<=59:
        print "Letter grade for " + str(n) + "%" + " is D"
    elif n>=0 and n<=49:
        print "Letter grade for " + str(n) + "%" + " is F"
    else:
        print "Invalid Input"
# percentage_to_letter(78)


# ex.15:
def take_avg(n, p):
    sum = 0
    for i in range(n,p+1):
        sum = sum + i
    avg = sum/float(p-n+1)
    print "The average of the numbers from " + str(n) + " to " + str(p) + " is " + str(avg)
# take_avg(1, 100)



# ex.16:
#with for
def fibonacci(n):
     a,b = 0,1
     for i in range(n-1):
      a,b = b,a+b
     print a
     # return a
#fibonacci(10)


def fibonacci2(n):
    a = 0
    b = 1
    for i in range(n - 1):
        temp = a
        a = b
        b = b + temp
    print b
# fibonacci(10)


def fibonacci_with_while(n):
    a,b=1,1
    k=0
    while k <n-1:
        a,b=b, a+b
        k+=1
    return a
#print fibonacci_with_while(6)

def fibonacci_with_while2(n):
    a = 0
    b = 1
    k = 0
    while k < n-1:
        temp = a
        a = b
        b = b + temp
        k = k + 1
    print a
# fibonacci_with_while2(10)

# ex.17:
def func1():
    x = True
    y = False
    z = False

    if (not x) or ((x and y) and z):
        print x
    else:
        print ((not z) or ((not x) and y))

# func1()

# ex.18:

# D dollars per hour
# T hours per day
# N number of days per month

def subtract_tax(salary):
    if salary < 5000:
        return salary*0.05
    else:
        return salary*0.1

def net_salary(d, n, t):
    total = t * d * n
    net = total - subtract_tax(total)
    print "Kemal's salary is " + str(int(net))

# net_salary(30, 20, 9)


# SECOND VERSION WITHOUT USING a subtract_tax
def net_salary2(d, n, t):
    total = t * d * n

    if total < 5000:
        tax = total*0.05
    else:
        tax = total*0.1

    net = total - tax
    print "Kemal's salary is " + str(int(net))

# net_salary2(30, 20, 9)


# ex.19:
def countdown1(n1,n2):
    for k in range(n1,n2,-1):
        print k
# countdown1(15,8)

def countdown(n1,n2):
    for k in range(n1,n2,-1):
        if k!=n2:
            print k
        else:
            break
#countdown(15,8)
