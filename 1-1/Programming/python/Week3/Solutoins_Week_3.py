
# ENGR 101 Introduction to Programming
# Practice Session Week 3

import math

# Question 1

"""           # Errors:
x = 10
function f(): # A function header definition must begin with def 
    y = 2      
    x = x + 1 # UnboundLocalError: local variable 'x' referenced before assignment(x can not be reassigned in the function)
print(x, y)   # NameError: name 'y' is not defined(y is only defined withing the function)
f()
"""
# e.g. this is one possible and correct version
print "\nQuestion 1"
x = 10
def f():
    y = 2
    z = x+1
    print z, y

f()




# Question 2
print "."*30
print "Question 2a"

# Question 2a
# 24, we add (8 + 16)
# 7, we add (3 + 4)

def sum_two_numbers(a,b):
    print(a+b)
sum_two_numbers(8, 16)
sum_two_numbers(3, 4)



print "."*30
print "Question 2b"

# Question 2b
# 9, we add 4 + 5
# 7, we add 3 + 4

a = 4
b = 5
def sum_two_numbers(a,b):
    print(a+b)
sum_two_numbers(a, b)
sum_two_numbers(3, 4)


print "."*30
print "Question 2c"

# Question 2c
# both will be (5) because a, b are specified inside the function.
a = 4
b = 5
def sum_two_numbers(a,b):
    a = 2
    b = 3
    print(a+b)
sum_two_numbers(a, b)
sum_two_numbers(3, 4)



print "."*30
print "Question 3"

# Question 3
a1 = 3
d = 2
def nth_sequence(n):

    a = a1 + (n-1) * d
    print a
nth_sequence(99)



print "."*30
print "Question 4"

# Question 4
def reg_polygon_internal(n):
    sum_of_internal_angles = (n-2) * 180
    print(sum_of_internal_angles)


reg_polygon_internal(3)



print "."*30
print "Question 5"

# Question 5
def square_pro(a , b):
    print(a * b**2)

square_pro("PYTHON", 2)
square_pro(25,5)


print "."*30
print "Question 6"

# Question 6
# NOTE: use math module to calculate the root only.
# formula for the distance:
# d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def distance_bt_2_points(x1, y1, x2, y2):
    d = (x2-x1)**2 + (y2 - y1)**2
    print(math.sqrt(d))

distance_bt_2_points(2, 2, 5, 5)



print "."*30
print "Question 8"

# Question 8
# s
# 125
# 844
# 1.00075...

print(max("sehir"))
print(abs(pow(-5,3)))
print(211*len("engr"))
print(math.sin(math.radians(math.pi/2)**2)+ math.cos(math.radians(math.pi/2)**2))

# math.sin() and math.cos() take inputs in radians
# math.radians() takes as an input degrees and coverts them to radians
# math.degrees() takes as an input radians and coverts them to degrees
# e.g.
# print math.sin(math.pi/2)
# print math.cos(math.pi)

print "."*30
print "Question 9"

# Question 9
a = 5
b = 3
c = 9
d = 1
e = 8
print(str(d) + str(c) + 3 * str(e) + str(5))



print "."*30
print "Question 10"

# Question 10
# p is the investment amount
# r is the annual interest rate
# t is the number of years

def simple_interest(p, r, t):
    i = p*r*t
    print(i)

simple_interest(100, 0.4 , 5)


print "."*30
print "Question 11"
# Question 11

def rec_calc(height, width):
    area = height * width
    perimeter = 2 * (height + width)
    print("The rectangle's area is " + str(area))
    print("The rectangle's perimeter is " + str(perimeter))

rec_calc(5, 4)



print "."*30
print "Question 12"

# Question 12
def kmeters_to_miles(n):
    miles = n * .6214
    print(miles)

kmeters_to_miles(50)



print "."*30
print "Question 13"
# Question 13

def twice(a):
    print(a)
    print(a)

twice("20")

# INSTEAD OF REPEATING THE WHAT WE ALREADY WROTE WE CALL twice()
# def twice_two(a, b):
#     print(str(a) + str(b))
#     print(str(a) + str(b))
#
# twice_two("input of twice_two", 3)


def twice_two_inputs(a, b):
    twice(str(a) + str(b))

twice_two_inputs("hello logger ", 442)


print "."*30
print "Question 14"

# Question 14
# result is 8.0

import math
x = math.sqrt(9) + math.sqrt(25)
print(x)



print "."*30
print "Question 15"

# Question 15
# we will get an error because y is defined inside the function

def square(x):
    y = x * x                                  # y is defined only within the function
    print("Value of x squared is " + str(y))

z = square(10)
# print(y)                                     # NameError: name 'y' is not defined


print "."*30
print "Question 16"
# Question 16

def print_n_times(s, n):
    print (s + "\n")*n      # the \n character returns on a new line each time it is usd

print_n_times('Code', 3)



print "."*30
print "Question 17"

# Question 17
x = 'I like'

def fav_fru(a, b, c):
    print(x + ' ' + a)
    print(x + ' ' + b)
    print(x + ' ' + c)

fav_fru('apple', 'orange', 'banana')



print "."*30
print "Question 18"

# Question 18
seconds = 0

def convert_to_sec(h, m, s):
    seconds = (h * 60 * 60) + (m * 60) + s
    print(seconds)

convert_to_sec(3, 1, 1)



print "."*30
print "Question 19"
# Question 19

def calc_hypo(a, b):
    hypo = math.sqrt((a**2) + (b**2))
    print(hypo)

calc_hypo(3, 4)



print "."*30
print "Question 20"
# Question 20

def cal_percentage(a, b, c):
    per1 = b/100.0 * a
    per2 = b/100.0 * c
    print(str(b) + '% of ' + str(a) + ' is ' + str(int(per1)))
    print(str(b) + '% of ' + str(c) + ' is ' + str(int(per2)))


cal_percentage(10, 50, 30)
