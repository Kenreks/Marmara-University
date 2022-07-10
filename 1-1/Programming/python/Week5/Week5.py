
"""
Week 5 Lecture script
"""

#Check and set your current directory
import os
cwd=os.getcwd() #This is your current working directory
print cwd

import os
preferred_dir="C:\Users\Mujde\Documents\ISTANBUL_SEHIR_UNI" \
              "\ENGR 101_SPRING 2018_HMA\Week 5" #Please set yours properly
os.chdir(preferred_dir) #Now you have changed your working directory to your preferred directory
#as you defined above. Please set yours properly!
cwd=os.getcwd()
print cwd

#SLIDE 8: Conditional Execution
x=18
if x > 0:
    print 'x is positive'
if x < 0:
    print 'x is negative'

#SLIDE 9: Alternative Execution
x=7
if x %2== 0:
    print "x is even"
else:
    print "x is odd"

#SLIDE 11: Chained conditional
x=7
y=7
if x < y:
    print "x is less than y"
elif x > y:
    print "x is greater than y"
else:
    print "x and y are equal"

# SLIDE 13: Chained conditional
x = 5
if x == 2:
    print "x is 2"
elif x <= 6:
    print "x is less than or equal to 6"
elif x > 3:
    print "x is greater than 3"

x = 11 #11
if x <= 2:
    print "x is less than or equal to 2"
elif x > 2 and x<10:
    print "x is greater than 2 and less than 10"
else:
    print "x is greater than 10"

# SLIDE 14: Nested conditional
x=10
y=7
if x == y:
    print 'x and y are equal'
else:
    if x < y:
        print 'x is less than y'
    else:
        print 'x is greater than y'

# SLIDE 14: Turn nested conditional into chained conditional
x=10
y=7
if x == y:
    print 'x and y are equal'
elif x != y and x < y:
    print 'x is less than y'
else:
    print 'x is greater than y'


# SLIDE 15
x=2
if x>0:
    if x<10:
        print "x is between 0 and 10"


if x>0 and x<10:
    print "x is between 0 and 10"

# SLIDE 18: Keyboard Input
input = raw_input()
print input
print type(input)

# SLIDE 19: Keyboard Input
prompt = 'What is 2 times 2?:  '
answer = raw_input(prompt)
print answer
print type(answer)

#You can also specify raw_input().encode('utf8') to convert to string

prompt = 'What is 2 times 2?:  '
answer = raw_input(prompt)
print answer
print type(answer)
if int(answer)==4:
    print "Correct answer"
else:
    print "Wrong answer"

# SLIDE 21: Break
while True:
    line = raw_input('> ')
    if line == 'done':
        break
    print line
print 'Finished!'

while True:
    line = raw_input('> ')
    if line != 'done':
        print line
        continue
    else:
        break
print 'Finished!'

#BREAK and CONTINUE can be used BOTH for FOR & WHILE loops
# SLIDE 23:Print odd numbers only
for i in range(0,10,1):
    if i%2==0:
        continue
    print i

#SLIDE 24:MODULUS operator
remainder = 7 % 3
print remainder

#SLIDE 25:Multiple assignment
bruce = 5
print bruce,#REMEMBER side-side print: the comma at the end of the print statement suppresses a new line
bruce = 7
print bruce

print bruce==5
print bruce==7

a = 5
b = a  # a and b are now equal
print "a=",a, ",b=",b
a = 3   # a and b are no longer equal
print "a=",a, ",b=",b
b=a
print "a=",a, ",b=",b

#SLIDE 27: UPDATING VARIABLES
x=3
x=x+1
print x

#SLIDE 31: RETURN
# A function to return tax_rate of salary amount
def subtract_tax(Sal):
    if Sal>=5000: tax_rate=0.1
    else: tax_rate=0.05
    return tax_rate

print subtract_tax(6000)

tax_ratio=subtract_tax(4000)
print tax_ratio

#SLIDE 33: Exercise 1
def divider(int1,int2,int3):
    for i in range(1,int1+1):
        if i%int2==0:
            print str(i)," is divisible by ", str(int2)
        if i%int3==0:
            print str(i)," is divisible by ", str(int3)
divider(8,2,3)

#SLIDE 34: Exercise 2
def isprime(n):
    for i in range(2,n):
        if n%i==0:
            print str(n), " is not a prime number"
            return
        else:
            prime=1
    if prime==1:
        print str(n), " is a prime number"

isprime(10)
isprime(919)
isprime(7)
isprime(11)

def isprime2(n):
    for i in range(2,n):
        if n%i==0:
            print str(n), " is not a prime number"
            return
    print str(n), " is a prime number"
isprime2(50)
isprime2(19)
isprime2(37)


#SLIDE 35: Exercise 3
def countdown(n1,n2):
    for k in range(n1,n2-1,-1):
        if k!=n2-1:
            print k
        else:
            break
countdown(15,8)
countdown(8,15)

def countdown2(n1,n2):
    if n1>n2:
        new1=n1
        new2=n2
    else:
        new1=n2
        new2=n1
    for k in range(new1,new2-1,-1):
        if k!=new2-1:
            print k
        else:
            break

countdown2(8,15)


