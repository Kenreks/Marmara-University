"""
Week 6 Lecture script
"""

#Check and set your current directory
import os
cwd=os.getcwd() #This is your current working directory
print cwd

import os
preferred_dir="C:\Users\Mujde\Documents\ISTANBUL_SEHIR_UNI" \
              "\ENGR 101_SPRING 2019_HMA\Week 6" #Please set yours properly
os.chdir(preferred_dir) #Now you have changed your working directory to your preferred directory
#as you defined above. Please set yours properly!
cwd=os.getcwd()
print cwd

#SLIDE 16: Fruitful functions
import math
def area(radius):
    area = math.pi * radius**2
    print area
    return area

print area(3)

#SLIDE 17: Fruitful functions
def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
print absolute_value(1)
print absolute_value(-1)

#SLIDE 18: Write a compare function that
# returns 1 if x > y
# returns 0 if x == y
# returns -1 if x < y
def comparison(x,y):
    if x>y:
        result=1
    elif x<y:
        result=0
    else:
        result=-1
    return result

print comparison(2,1)
print comparison(1,2)
print comparison(1,1)

#SLIDE 19: Void function versus fruithful function
def void_func():
    print 2
def fruitful_func():
    return 2

a = void_func()
print 'the value of a:', a

b = fruitful_func()
print 'the value of b:', b

#SLIDE 20: Boolean functions
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

print is_divisible(6,2)
print is_divisible(6,4)

#SLIDE 22: Boolean functions
def is_divisible2(x, y):
    return x % y == 0
print is_divisible2(6,2)
print is_divisible2(6,4)

#SLIDE 23:
x=5
y=2
if is_divisible2(x, y): #or if is_divisible(x, y) == True
    print str(x), ' is divisible by ',str(y)
else:
    print str(x), ' is NOT divisible by ', str(y)

#SLIDE 27:Recursion
def countdown(n):
    if n<=0:
        print "Done!"
    else:
        print n
        countdown(n-1)

countdown(5)

#SLIDE 30:Recursion
def sumNumbers(n):
    if n == 1:
        return 1
    else:
        return n + sumNumbers(n-1)

print sumNumbers(3)

#SLIDE 48:Random module
import random
print random.random()  # float x, 0.0 <= x < 1.0
print random.uniform(1, 10) # float x, 1.0 <= x < 10.0
print random.randint(1, 10)  # integer x, 1 <= x <= 10
print random.randrange(0, 10, 2) # Even int from 0 to 10
print random.choice('abcdef')  # Choose a random element

#SLIDE 52:More recursion
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

print factorial(3)

#SLIDE 54:More recursion
def fibonnaci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)

print fibonnaci(10)

import random
rand=random.randint(0,10)
print rand
def guess():
    prompt="Enter a number between o and 10: "
    usernum=int(raw_input(prompt))
    print usernum
    if usernum==rand:
        print "Good guess"
        return
    else:
        if usernum>rand:
            print "Enter a smaller number"
        else:
            print "Enter a larger number"
        guess()
guess()

