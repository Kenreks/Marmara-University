
# ENGR 101 Practice Session Week 12


# Q1
class Vehicle:
    def __init__(self, x = "no color", y = 0, z = "no brand"):
        self.color = x
        self.speed = y
        self.brand = z

c1 =Vehicle()
c2 = Vehicle("blue", 100, "BMW")
# print c1.color
# print c2.brand

# Q2
class Pokemon:
    health = 0
    attack = 0

pikachu = Pokemon()
pikachu.health = 100
pikachu.attack = 15

# print "Pokemons attack is : " + str(pikachu.attack)+ " Pokemons health is : " + str(pikachu.health)

"""
Pokemons attack is: 15 Pokemons health is: 100
"""

# Q3
pokemon1 = Pokemon()
pokemon1.health = 100
pokemon1.attack = 40
pokemon1.name = "poke1"
# print pokemon1.name

pokemon2 = Pokemon()
pokemon2.health = 90
pokemon2.attack = 20
pokemon2.name = "poke2"

pokemon3 = Pokemon()
pokemon3.health = 100
pokemon3.attack = 50
pokemon3.name = "poke3"

pokemon4 = Pokemon()
pokemon4.health = 100
pokemon4.attack = 43
pokemon4.name = "poke4"


# Q4
class Pokemon:
    def __init__(self, name, health, attack):
        self.PokemonsName = name
        self.PokemonsHealth = health
        self.PokemonsAttack = attack


pikachu = Pokemon("Pikachu", 100, 15)
balbasaur = Pokemon("Balbasaur", 115, 10)
charmander = Pokemon("Charmander", 90, 20)
squirtle = Pokemon("Squirtle", 105, 12)

# Q5
pokemon3 = Pokemon("pokemon3", 100, 4)
pokemon3.type = "Electricity"

pokemon4 = Pokemon("pokemon4", 100, 40)
pokemon4.type = "Fire"
# and so on

# Q6
def fight_arena(poke1, poke2):
    round = 1

    while poke1.PokemonsHealth > 0 or poke2.PokemonsHealth>0:

        poke1.PokemonsHealth = poke1.PokemonsHealth-poke2.PokemonsAttack
        poke2.PokemonsHealth = poke2.PokemonsHealth-poke1.PokemonsAttack

        print "Round :"+str(round)+" " +poke1.PokemonsName +" vs " + poke2.PokemonsName

        print poke1.PokemonsName+ " hit "+ str(poke1.PokemonsAttack) + " damage " +\
              poke2.PokemonsName  +"'s " + str(poke2.PokemonsHealth) + " health left"

        print poke2.PokemonsName + " hit " + str(poke2.PokemonsAttack) + " damage " + \
        poke1.PokemonsName + "'s " + str(poke1.PokemonsHealth) + " health left"
        print ""

        round += 1
        if poke1.PokemonsHealth < 0:
            print poke2.PokemonsName + " WINS !!!"
            break
        elif poke2.PokemonsHealth <0:
            print poke1.PokemonsName + " WINS !!!"
            break

# fight_arena(squirtle, balbasaur)

# Q7
import random

def fight_arena(poke1, poke2):
    round = 1
    while poke1.PokemonsHealth > 0 or poke2.PokemonsHealth > 0:
        random_number = random.uniform(0, 1)
        poke1.PokemonsHealth = poke1.PokemonsHealth - poke2.PokemonsAttack * random_number
        poke2.PokemonsHealth = poke2.PokemonsHealth - poke1.PokemonsAttack * random_number
        print "Round :" + str(round) + " " + poke1.PokemonsName + " vs " + poke2.PokemonsName
        print poke1.PokemonsName + " hit " + str(poke1.PokemonsAttack) + " damage" + \
              poke2.PokemonsName + "'s " + str(poke2.PokemonsHealth) + " health left"
        print poke2.PokemonsName + " hit " + str(poke2.PokemonsAttack) + "damage " + \
              poke1.PokemonsName + "'s " + str(poke1.PokemonsHealth) + " health"
        round += 1
        if poke1.PokemonsHealth < 0:
            print poke2.PokemonsName + " WINS !!!"
            break
        elif poke2.PokemonsHealth < 0:
            print poke1.PokemonsName + " WINS !!!"
            break

# fight_arena(pikachu, charmander)

# Q8
class Animal:
    def __init__(self, x, y, z):
        self.name = x
        self.age = y
        self.color = z


ani1 = Animal("zebra", 23, "black,white")
ani2 = Animal("lion", 12, "golden")
ani3 = Animal("eagle", 4, "black,white")
ani4 = Animal("bird", 3, "yellow")


# Q9
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def move(p, dx, dy):
    p.x += dx
    p.y += dy

p = Point(0,0)
move(p,10,10)

# print p.x, p.y


# Q10
class Student:
    def __init__(self, name, surname, department, semester, gpa):
        self.name = name
        self.surname = surname
        self.department = department
        self.semester = semester
        self.gpa = gpa


johnDoe = Student("john", "doe", "cs", "sophmore", 3.53)
# print johnDoe.name
# print johnDoe.surname
# print johnDoe.gpa


# Q11
class Date:
    def __init__(self, day=1, month=1, year=1):
        self.day = day
        self.month = month
        self.year = year


def print_date(d):
    print str(d.day) + "/" + str(d.month) + "/" + str(d.year)

d = Date(26,4,2019)
# print_date(d)

# Q12
class Triangle:
    def __init__(self, a1, a2, a3):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3

def check_triangle(t):
    if t.a1 + t.a2 + t.a3 == 180:
        return True
    else:
        return False

t = Triangle(30,30,30)
# print check_triangle(t)


# Q13
class Vehicle:
    def __init__(self, type_of_vehicle, n_of_wheels, engine_size, color="red"):
        self.type = type_of_vehicle
        self.n_of_wheels = n_of_wheels
        self.engine_size = engine_size
        self.color = color


def changeColor(v, color):
    v.color = color


v1 = Vehicle("car", 4, 1600)
changeColor(v1, "blue")
# print v1.color


# Q14
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print "You added a new employee, their name is: " + self.name


# e1 = Employee("hakki", 5300)


#Q15
class Car:
    def __init__(self, speed, max_speed):
        self.speed = speed
        self.max_speed = max_speed


def increaseSpeed(car, speed):
    if car.speed + speed > car.max_speed:
        car.speed = car.max_speed
    else:
        car.speed += speed

c = Car(20,100)
# increaseSpeed(c, 50)
# print c.speed
# increaseSpeed(c, 40)
# print c.speed


# Q16
def decreaseSpeed(car, speed):
    if car.speed - speed < 0:
        car.speed = 0
    else:
        car.speed -= speed

# decreaseSpeed(c, 10)
# print c.speed
# decreaseSpeed(c, 20)
# print c.speed


# Q17
class Hotel:
    def __init__(self, roomsOccupied, totalRooms):
        self.roomsOccupied = roomsOccupied
        self.totalRooms = totalRooms

def occuper(hotel):
    return (float(hotel.roomsOccupied) / hotel.totalRooms) * 100



h = Hotel(25,100)
# print occuper(h)


# Q18
class RationalNumber:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        if self.den == 0:
            print "this is not valid"



def printRNum(rational_number):
    print str(rational_number.num) + "/" + str(rational_number.den)



r1 = RationalNumber(20, 10)

# printRNum(r1)


# Q19
def reduceR(rational_number):
    x = rational_number.num
    y = rational_number.den
    while y != 0:
        (x, y) = (y, x % y)

    remainder = rational_number.den % rational_number.num
    new_num = rational_number.num / x
    new_den = rational_number.den / x
    print str(new_num) + "/" + str(new_den)


# reduceR(r1)



# Multiple Objects Cretion with a Loop

# dict_obj = {}
# for i in range(10):
#     dict_obj[i] = Vehicle(0,0,0)
#
# for i in range(10):
#     print dict_obj[i]
# d ={"a":1000}
# print d.values()