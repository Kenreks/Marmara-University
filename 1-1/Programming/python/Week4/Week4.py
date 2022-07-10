"""
Week 4 Lecture script
"""

#Check and set your current directory
import os
cwd=os.getcwd() #This is your current working directory
print cwd

import os
preferred_dir="C:\Users\Mujde\Documents\ISTANBUL_SEHIR_UNI" \
              "\ENGR 101_SPRING 2018_HMA\Week 4" #Please set yours properly
os.chdir(preferred_dir) #Now you have changed your working directory to your preferred directory
#as you defined above. Please set yours properly!
cwd=os.getcwd()
print cwd

#SLIDE 10&11: Boolean expressions
a=True
print type(a)
b="true"
print type(b)

print type(False)
print type("False")

#SLIDE 12: Relational Operators
print 5=5 #syntax error
print 5==5 #true
print 60>=5 #true
print 7<=10 #true
print 7=<10 #syntax error

#SLIDE 14&15: Logical Operators
print 5<2 and 10>3 #false
print 5<2 or 10>3 #true
print not 2>5 #true
print not 10>5 #false

print False and True
print False or True

print False and True or True
print (False and True) or True

print False and True or not True and False
print (False and True) or ((not True) and False)

#SLIDE 20: While Loop
for i in range(4, 8, 2):
    print i #4,6

k=4
while k<8:
    print k
    k=k+2



#SLIDE 21: Countdown using while loop
def countdown(n):
    while n>0:
        print n
        n=n-1
    print "Done!"

countdown(4)

def countdown2(n):
    for i in range(n,0,-1):
        print i
    print "Done!"

countdown2(4)

#SLIDE 23: sum the numbers between a and d
def sum_numbers(a,b):
    summed=0
    for i in range(a,b+1):
        summed=summed+i
    print summed

sum_numbers(2,4)
sum_numbers(4,2)

def sum_numbers2(a,b):
    count=a
    summed=0
    while count<=b:
        summed = summed + count
        count=count+1
    print summed

sum_numbers2(2,4)
sum_numbers2(4,2)
#SLIDE 24: average function
"""Create a function that takes two integers n and p as inputs and
prints the average of numbers from p to n (inclusive). You cannot use
any built-in functions or anything that we haven’t learnt so far.
>> take_avg(1,100)
The average of numbers between 1 and 100 is 50.5
"""
def take_avg(n,p):
    sum=0
    k=0.0
    for i in range(n,p+1,1):
        sum=i+sum
        k=k+1.0
    print k
    print sum
    aver=sum/k
    print "The average of numbers between ", str(n)," and ", str(p)," is ",str(aver)
take_avg(1,100)

def take_avg2(n,p):
    sum=0
    k=n
    while k<=p:
        sum=k+sum
        k=k+1.0
    print k
    print sum
    aver=sum/(k-1)
    print "The average of numbers ", str(n)," and ", str(p)," is ",str(aver)

take_avg2(1,100)