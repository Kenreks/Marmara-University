
# ENGR 101 Introduction to Programming
# Practice Session Week 14

# Question 1

class Car:
    a = "coper"
    def __init__(self, a):
        self.a = a


c = Car("sahin")
# print c.a

#in the first question sahin will be printed not "coper" becasue we have write
#(self.a) to indicate which (a) we want to use.

# Question 2
class Car:
    a = "coper"
    def __init__(self, a):
        self.a = self.a

c = Car("sahin")
# print c.a
# print Car.a

# Question 3
class Person:
    def __init__(self,first,last):
        self.name = first
        self.lastname = last

    def get_name(self):
        return str(self.name) + " " + str(self.lastname)

class Employee(Person):
    def __init__(self, first, last, id):
        Person.__init__(self, first, last)
        self.id_number = id
#
# emp1 = Employee('Ayse','Eren',1234)
# print emp1.get_name()


# Additional demonstration that inheritance can span within multiple classes
class SalesPersonel(Employee):
    def __init__(self,n,l,id,type):
        Employee.__init__(self, n, l, id)
        self.type = type

    def desplay(self):
        print "Name&Surname: " + self.get_name()
        print "ID: " + str(self.id_number)
        print "Type: " + self.type

# manager = SalesPersonel("Ahmed", "Groshar", 21538, "Sales Manager")
# manager.desplay()



# Question 4
class Car:
    def __init__(self,max_speed):
        self.max_speed = max_speed
    def price(self):
        return "Price?"
class Bmw(Car):
    def price(self):
        return "Price of BMW is: 200000"
class Audi(Car):
    def price(self):
        return "Price of the Audi is 30000"


car1 = Bmw(210)
car2 = Audi(210)
# print car1.price()
# print car1.max_speed
# print car2.price()
# print car2.max_speed

# Question 4 and 5
class Point_2D:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

class Point_3D(Point_2D):
    def __init__(self,x,y,z):
        Point_2D.__init__(self,x,y)
        self.z = z
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point_3D(x,y,z)

    # if this method does not exist we have the memory locations printed instead
    # def __str__(self):
    #     return "x :" + str(self.x) + " y :"+str(self.y)+  " z :"+str(self.z)+"\n"

point1 = Point_3D(2,4,5)
point2 = Point_3D(1,3,4)

# print point1
# print point2
# point3 = point1 + point2
# print point3
# print point1 + point2

# Question 6
class FirstName():
    def first_name(self):
        return ("Mohamed")

class SecondName():
    def second_name(self):
        return "Ali"

class FullName(FirstName, SecondName):
    def full_name(self):
        name = FullName()
        print name.first_name() + " " + name.second_name()

# name = FullName()
# name.full_name()

# Question 7
class Student:
    def __init__(self,name,id):
        self.name = name
        self.id = id
class CurrentStudent(Student):
    def __init__(self,name, id, semester):
        Student.__init__(self, name, id)
        self.semester = semester


std1 = CurrentStudent('Ahmet','213456',4)
std2 = Student('Ayse','136242')

# print isinstance(std1,Student)
# print isinstance(std1,CurrentStudent)
# print isinstance(std2,Student)
# print isinstance(std2,CurrentStudent)


# Question 8 and 10
class Game:
    def __init__(self,energy,money,no_of_castle):
        self.energy = energy
        self.money = money
        self.no_of_castle = no_of_castle
    def show_info(self):
        print "Energy:" , self.energy,'\n',"Money:",self.money,'\n','No. of buildings:',self.no_of_castle


class Player(Game):
    def __init__(self,energy,money,no_of_castle):
        Game.__init__(self,energy,money,no_of_castle)
    def create_new_castle(self):
        if self.energy > 5 and self.money > 10:
            self.no_of_castle +=1
            self.energy -=5
            self.money -=10
        else:
            print "You do not have enough money or energy to create a new building"


class OpponentPlayer(Game):
    def __init__(self,energy,money,no_of_castle, no_of_destructions):
        Game.__init__(self,energy,money,no_of_castle)
        self.no_of_destructions = no_of_destructions
    def destroyCastle(self):
        if self.energy > 10:
            self.no_of_destructions +=1
            self.energy -=10


# player1 = Player(30,60,10)
# player1.create_new_castle()
# player1.show_info()
# player2 = OpponentPlayer(40,30,20,30)
# player2.destroyCastle()
# player2.show_info()

# Question 9
class Document:
    def __init__(self, name,n):
        self.name = name
        self.number_of_pages = n
    def show(self):
        pass
    def get_no_pages(self):
        pass

class Excel(Document):
    def show(self):
        return 'Show excel contents!'
    def get_no_pages(self):
        return self.number_of_pages

class Word(Document):
    def show(self):
        return 'Show word contents!'
    def get_no_pages(self):
        return self.number_of_pages

documents = [Excel('Document1',45),
             Excel('Document2',38),
             Word('Document3',23)]


# for document in documents:
#     print document.name + ': ' + document.show()
#     print document.name + ': ' + str(document.get_no_pages())

#Q-11/12

class Polygon:
    def __init__(self, n):
        self.number_sides = n
        self.sides = []

    def enterSides(self):
        for i in range(self.number_sides):
            length = input("Please enter length for Side %s:\t"%(i+1))
            self.sides.append(length)
        self.sides.reverse()

    def showSides(self):
        for i in range(len(self.sides)):
            print "Length of Side %s: "%(i+1), self.sides[i]


import math
class Triangle(Polygon):
    def area(self):
        s = sum(self.sides)/2.0
        A = math.sqrt(s*(s-self.sides[0])*(s-self.sides[1])*(s-self.sides[2]))
        return round(A,3)

# mytriangle = Triangle(3)
# mytriangle.enterSides()
# mytriangle.showSides()
# print mytriangle.area()

#Q-13
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

class Date(Time):
    def __init__(self, year, month, day, hours, minutes, seconds):
        Time.__init__(self, hours, minutes, seconds)
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "%d%d%d %d : %d : %d"%(self.year, self.month, self.day, self.hours, self.minutes, self.seconds)

# test = Date(2016, 12, 28, 23, 04, 00)
# print test

#Q-14
class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

class Date(Time):
    def __init__(self, year, month, day, hours, minutes, seconds):
        Time.__init__(self, hours, minutes, seconds)
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "%d%d%d %d : %d : %d"%(self.year, self.month, self.day, self.hours, self.minutes, self.seconds)

# test = Date(2016, 12, 28, 23, 04, 00)
# print test

#Q-14
class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return str(self.name)+" " +str(self.surname)

class CollegeStudent(Student):

    def __init__(self, name, surname, dept,  ID, year):
        Student.__init__(self, name, surname)
        self.dept = dept
        self.ID = ID
        self.year = year

    def __str__(self):
        return Student.__str__(self) + " " +self.dept + " " + str(self.ID) + " " + str(self.year)

# test = CollegeStudent("Mehmet", "Kadir", "IE", 213322, 2015)
# print test

#Q-15
class Rational:
    def __init__(self, numerator, denominator):
        self.num = numerator
        self.denom = denominator

    def __lt__(self, other):
        return self.num*other.denom < self.denom*other.num

    def __le__(self, other):
        return self.num * other.denom <= self.denom * other.num

    def __eq__(self, other):
        return self.num*other.denom == self.denom*other.num

    def __ne__(self, other):
        return self.num*other.denom != self.denom*other.num

    def __gt__(self, other):
        return self.num*other.denom > self.denom*other.num

    def __ge__(self, other):
        return self.num * other.denom >= self.denom * other.num

# test1 = Rational(2,5)
# test2 = Rational(2,5)
# print test1 == test2


#Q-16 and Q-17 and Q-18
class PowerList:
    def __init__(self, data):
        self.data = data

    def __mul__(self, other):
        temp = self.data[:]
        if isinstance(other, int):
            for i in range(len(temp)):
                temp[i] *= other
            return temp

    def __pow__(self, power, modulo=None):
        temp = self.data[:]
        if isinstance(power, int):
            for i in range(len(temp)):
                temp[i] **= power
            return temp

    def __abs__(self):
        temp = self.data[:]
        for i in range(len(temp)):
            if isinstance(temp[i], int):
                if temp[i] <0:
                    temp[i] *= -1

        return temp
#test = PowerList([-1, -2, -3])
#print test*3
#print test**3
#print abs(test)

#Q-19
class PowerDict:
    def __init__(self, data_dict):
        self.data_dict = data_dict

    def __add__(self, other):
        temp = self.data_dict
        for i in other:
            if i not in temp:
                temp[i] = other[i]
        return temp

    def __sub__(self, other):
        temp = self.data_dict
        to_return = {}
        for i in temp:
            if i not in other:
                to_return[i] = temp[i]
        return to_return

# test = PowerDict({"a":1, "b":2, "c":3})
# print test.data_dict
# print test + {"a":1, "b":2, "c":3, "d":4, "e":5}
#
# test2 = PowerDict({"a":1, "b":2, "c":3, "d":4, "e":5})
# print test2 - {"a":1, "b":2, "c":3}


# Q-20
class MyClass:
    def __init__(self, inp):
        self.xyz = inp
    def __str__(self):
        return str(self.xyz*2)

class MyClass2(MyClass):
    def __str__(self):
        return str(self.xyz*3)

# test = MyClass2(range(1,3))
# print test
