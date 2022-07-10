"""
Week 13 Lecture script: Classes & Methods continued
"""

#Check and set your current directory
import os
cwd=os.getcwd() #This is your current working directory
print cwd

import os
preferred_dir="C:\Users\Mujde\Documents\ISTANBUL_SEHIR_UNI" \
              "\ENGR 101_SPRING 2019_HMA\Week 13" #Please set yours properly
os.chdir(preferred_dir) #Now you have changed your working directory to your preferred directory
#as you defined above. Please set yours properly!
cwd=os.getcwd()
print cwd

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    # # SLIDE 10
    def __str__(self):
        return str(self.hour) + ':' + str(self.minute) + ':' + str(self.second)

    def print_time(self):
        print str(self.hour) + ':' + str(self.minute) + ':'\
          + str(self.second)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def int_to_time(self,seconds):
        hour = (seconds / 3600) % 24
        minute = (seconds /60) % 60
        second = seconds % 60
        return Time(hour, minute, second)

    def increment(self, seconds):
        tot_secs = seconds + self.time_to_int()
        return self.int_to_time(tot_secs)

    def is_after(self, other):
        return self.time_to_int() >other.time_to_int()

    # SLIDE 11: Operator overloading
    # def __add__(self, other):
    #     seconds = self.time_to_int() + other.time_to_int()
    #     return self.int_to_time(seconds)

    # SLIDE 15: Type-based dispatch
    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return self.int_to_time(seconds)

    # SLIDE 15: Type-based dispatch
    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    # SLIDE 18: Right side addition
    def __radd__(self, other):
        return self.__add__(other)


time1 = Time(10, 30)
time1.print_time()
print time1.time_to_int()

time2 = time1.int_to_time(3700)
time1.print_time()
time2.print_time()

time3 = time2.increment(20)
time3.print_time()
time2.print_time()

#SLIDE 10
time = Time(9, 45)
print time

#SLIDE 11&12: Operator overloading
start = Time(9, 45)
duration = Time(1, 15)
print start + duration
# When you apply the + operator to Time objects, Python invokes __add__.
# When you print the result, Python invokes __str__.

#SLIDE 15&16&17: Type-based dispatch
start = Time(9, 45)
duration = Time(1, 35)
print start + duration

print start + 5700

#SLIDE 18
start = Time(9, 45)
print start + 1337
print 1337 + start

#SLIDE 21: Debugging
class Point:
    """represents a point in 2-D space"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
#To create a Point object, you call Point as if it were a function.
blank = Point(0, 0)
print blank


p = Point(0, 0)
print p.z
print getattr(p, 'z')
print type(p)

#SLIDE 23:
p = Point(3, 4)
print p.__dict__

def print_attributes(obj):
    for attr in obj.__dict__:
        print attr, getattr(obj, attr)

print_attributes(p)

# Exercise 1:
"""Create a class which represents rational numbers, with two attributes: numerator and denominator. 
Denominator should not be zero. Override the addition, subtraction, and multiplication operators,
 based on how we do these operations in rational numbers. """
class Rational_num():
    """Create a class which represents rational numbers, with two attributes: numerator and denominator."""
    def __init__(self,numerator,denominator):
        self.numerator=numerator
        if denominator==0:
            print "Denominator cannot be zero"
            return
        else:
            self.denominator=denominator
    def __add__(self, other):
        new_numerator=self.numerator*other.denominator+other.numerator*self.denominator
        new_denominator=self.denominator*other.denominator
        return Rational_num(new_numerator,new_denominator)
    def __sub__(self, other):
        new_numerator=self.numerator*other.denominator-other.numerator*self.denominator
        new_denominator=self.denominator*other.denominator
        return Rational_num(new_numerator,new_denominator)
    def __mul__(self, other):
        new_numerator=self.numerator*other.numerator
        new_denominator=self.denominator*other.denominator
        return Rational_num(new_numerator,new_denominator)
    def __str__(self):
        # return str(self.numerator*1.0/self.denominator)
        return str(self.numerator) + "/" + str(self.denominator)

number1 = Rational_num(4,5)
number2 = Rational_num(2,6)
print number1
print number2
print number1 + number2
print number1 - number2
print number1 * number2


# Exercise 2:
""" Create a class Point_3D that will have 
as attributes an x, y and z coordinates , by default they should be zero. 
Overload the add operator 
to add the coordinates of two points, e.g., (2,4,5) + (1,3,4) = (3,7,9). 
What happens if you create two objects from the Point_2D class and try to add them."""

class Point_3D():
    def __init__(self, x=0, y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        new_self_x=self.x+other.x
        new_self_y = self.y + other.y
        new_self_z = self.z + other.z
        return Point_3D(new_self_x,new_self_y,new_self_z)
    def __str__(self):
        present="( "+str(self.x)+", "+str(self.y)+", "+str(self.z)+")"
        return present

point1=Point_3D(1,2,3)
print point1
point2=Point_3D(5,6,7)
print point2

print point1+point2




