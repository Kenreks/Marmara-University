"""
Week 12 Lecture script: Dictionaries
"""

#Check and set your current directory
import os
cwd=os.getcwd() #This is your current working directory
print cwd

import os
preferred_dir="C:\Users\Mujde\Documents\ISTANBUL_SEHIR_UNI" \
              "\ENGR 101_SPRING 2019_HMA\Week 12" #Please set yours properly
os.chdir(preferred_dir) #Now you have changed your working directory to your preferred directory
#as you defined above. Please set yours properly!
cwd=os.getcwd()
print cwd

#SLIDE 18&19
class Point:
    """represents a point in 2-D space"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
#To create a Point object, you call Point as if it were a function.
blank = Point(0, 0)
print blank

#SLIDE 20&21: Attributes
#Access attributes of an instance using dot notation
print blank.x
print blank.y

blank.x = 3.0
blank.y = 4.0
print blank.x, blank.y

import math
distance = math.sqrt(blank.x**2 + blank.y**2)
print distance

#print point function taking an instance as an argument
def print_point(p):
    print '(' + str(p.x)  + ',' + str(p.y) + ')'

print_point(blank)

#SLIDE 22&23
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

def print_time(t):
    print str(t.hour) + ':' + str(t.minute) + ':'\
          + str(t.second)

#SLIDE 24&25:
time = Time() #no arguments, default values for the hour, minute and second
print_time(time)

time = Time(9) #overrides hour
print_time(time)

time = Time(9,45) #overrides hour and minute
print_time(time)

time = Time(9,45,20) #overrides hour, minute and second
print_time(time)

#SLIDE 28&29
#METHODS are functions within the classes
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print str(self.hour) + ':' + str(self.minute) + ':'\
          + str(self.second)

start = Time(9, 45)
Time.print_time(start) # method call via class name

start.print_time() # method call via a class instance 09:45:0

#SLIDE 30&31&32:
class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def print_time(self):
        print str(self.hour) + ':' + str(self.minute) + ':'\
          + str(self.second)

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def int_to_time(self, seconds):
        hour = (seconds / 3600) % 24
        minute = (seconds /60) % 60
        second = seconds % 60
        return Time(hour, minute, second)

    def increment(self, seconds):
        tot_secs = seconds + self.time_to_int()
        return self.int_to_time(tot_secs)

    #SLIDE 34
    def is_after(self, other):
        return self.time_to_int() >other.time_to_int()


start = Time(9, 45)
print start.time_to_int()
print start.int_to_time(35100) #creating a new time object
start.int_to_time(35100).print_time()

start.increment(60*60).print_time()

#SLIDE 33
start = Time(9, 45)
start.print_time()
end = start.increment(1337)
end.print_time()

end = start.increment(1337)

#SLIDE 34
print start.is_after(end) #False
print end.is_after(start) #True

#SLIDE 36
time1 = Time(10, 30)
time1.print_time()
print time1.time_to_int()

time2 = time1.int_to_time(3700)
time1.print_time()
time2.print_time()

time3 = time2.increment(20)
time3.print_time()
time2.print_time()

#SLIDE 37
import math
class Point:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def get_dist_from_origin(self):
        return math.sqrt(self.x**2 + self.y**2)

    def get_dist_from_another_point(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)

point1 = Point(3, 5)
point2 = Point(1, 0)

print point1.get_dist_from_origin()
print point1.get_dist_from_another_point(point2)

#SLIDE 40&41
"""I am repeating the code just for illustrative purposes. Not necessary and efficient
to repeat the code normally"""
class Point:
    """represents a point in 2-D space"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    """represent a rectangle.
    attributes: width, height, corner."""
    def __init__(self, width, height, x, y):
            self.width = width
            self.height = height
            self.corner = Point(x, y)

box = Rectangle(100, 200, 0, 0)
print box

box.width = box.width + 50
box.height = box.height + 100
print box.width,box.height

#SLIDE 44: Instances as return values
def find_center(box):
    p = Point(0,0)
    p.x = box.corner.x + box.width/2.0
    p.y = box.corner.y + box.height/2.0
    return p
center_point=find_center(box)
print center_point.x,center_point.y

#SLIDE 46: Copying
class Point:
    """represents a point in 2-D space"""
    def __init__(self):
        self.x = 0
        self.y = 0
p1 = Point()
p1.x = 3.0
p1.y = 4.0
import copy
p2 = copy.copy(p1)

print p1 is p2 #p1 and p2 contain the same data, but they are not the same Point.

#SLIDE 47:
class Point:
    """represents a point in 2-D space"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    """represent a rectangle.
    attributes: width, height, corner."""
    def __init__(self, width, height, x, y):
            self.width = width
            self.height = height
            self.corner = Point(x, y)


box = Rectangle(100, 200, 0, 0)
box2 = copy.copy(box)
print box2 is box #False:copied
print box2.corner is box.corner #True: not copied

#SLIDE 48: Deep copy
box3 = copy.deepcopy(box)
print box3 is box #False
print box3.corner is box.corner #False

#SLIDE 49:
p = Point(0, 0)
print p.z

#To check whether an object has a particular attribute:
print hasattr(p, "z")#False
print hasattr(p, "y")#True

#If you are not sure what type an object is, you can ask:
print p
print type(p)

#EXERCISE 1:
""" Define a class Employee that will have as attributes name and salary. Whenever you create 
a new employee instance it should print out “You added a new employee, their name is: <given name>”. 
Add a method to change to be able to update the salary."""

class Employee:
    """ Defines a class Employee that will have as attributes name and salary"""
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print "You added a new employee, name is: ", self.name

    def update_salary(self,new_Salary):
        print "The salary of the employee ", self.name, " is updated " \
        "from ",str(self.salary)," to ", str(new_Salary)
        self.salary=new_Salary
        return self.salary

employe1 = Employee('Ayse', 1200)
print employe1.salary

employe1.update_salary(2000)
print employe1.salary


#EXERCISE 2:
""" Define a class Student that has two attributes: name and a dictionary of courses by semester 
(e.g. {‘Semester4’:{‘PHYS101’:3, ‘CS 100’:1}} 
Note: the values for course codes are credits.). 
Add a method that takes an argument like ‘SemesterX’ as input (X can be 1-8) and 
prints all the courses student took in that semester along with total number of credits that semester.

>> student1 = Student("Alper", {"Semester1":{"PHYS 101":3, "MATH 101":3}})
>> student1.semester_history("Semester1")
   PHYS 101
   MATH101
   Total credits in Semester1: 6

"""

class Student(object):
    def __init__(self, name = "", course_hist = {}):
        self.name = name
        self.course_hist = course_hist

    def semester_history(self, semester):
        total_credits= 0
        for course in self.course_hist[semester]:
            print course
            total_credits +=  self.course_hist[semester][course]
        print "Total credits in", semester, ":", total_credits
student1 = Student("Alper", {"Semester1":{"PHYS 101":3, "MATH 101":3},
                             "Semester2":{"ENGR 102":3, "MATH 102":4}})

student1.semester_history("Semester1")
student1.semester_history("Semester2")
