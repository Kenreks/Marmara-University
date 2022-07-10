import math


#Q1
class Circle():
    def __init__(self, radius = 0):
        self.radius = radius

    def area_c(self):
        a = math.pi * math.pow(self.radius, 2)
        return a
    def perimeter_c(self):
        p = self.radius * math.pi * 2
        return p

c_ob = Circle()
c_ob.radius = 4
# print c_ob.radius
# print "Area: " + str(c_ob.area_c())
# print "Perimeter: " + str(c_ob.perimeter_c())

#Q2
class Student():
    def __init__(self, id = 0, name = "", dict_c = {}):
        self.id = id
        self.name = name
        self.dict_c = dict_c

    def semester_history(self, s):
        total_credits = 0
        if s in self.dict_c:
            for j in range(len(self.dict_c[s])):
                print self.dict_c[s].keys()[j]
                total_credits += self.dict_c[s].values()[j]
            print "Total credits in Semester1: " + str(total_credits)

        else:
            print "ERROR, SEMESTER NOT FOUND !!!"

student1 = Student(21899129, "ASEM", {"Semester1":{"PHYS 101": 3, "MATH 101":4},"Semester2":{"ENGR 101": 1, "UNI 101":2}})
# student1.semester_history("Semester1")

#Q3
student_ob = {}
student2= Student(21899122, "Ahmed", {"Semester1":{"PHYS 101": 3, "MATH 901":4},"Semester2":{"ENGR 101": 1, "UNI 101":2}})
student_ob[student1.id] = student1

student_ob[student2.id] = student2

class Course():
    def __init__(self, code, name, room, instructor, students):
        self.code = code
        self.name = name
        self.room = room
        self.instructor = instructor
        self.students = students

    def get_attendance_list(self):
        for i in self.students:
            print self.students[i].name, i

    def students_sharing_course(self, course_name):
        for i in self.students:
            for j in self.students[i].dict_c.values():
                # print j
                if course_name in j:
                    print self.students[i].name, i


course_ob = Course(12, 'math', '5104', 'ali',student_ob)
# print student_ob
# course_ob.get_attendance_list()
# course_ob.students_sharing_course('MATH 101')


#Q4
class Inventory():
    def __init__(self, product_name, current_count):
        self.count = current_count
        self.product_name = product_name

    def full_fill_customer_order(self, x):
        self.count -= x
        return self.count

    def add_product_to_inventory(self):
        return self.count

    def __str__(self):
        return "current count: " + str(self.count)

inv = Inventory("lah", 5)
# print inv
# print inv.full_fill_customer_order(3)
# print inv.add_product_to_inventory()
# print inv

#Q5

class Club():
    def __init__(self, list_members, club_name, club_web):
        self.list_m = list_members
        self.club_name = club_name
        self.club_web = club_web

    def make_full_name(self, f_name, l_name):
        full_name = f_name + " " +  l_name
        return full_name

    def add_memeber(self, f_name, l_name):
        self.list_m.append(f_name +" " +  l_name)

# c = Club([], "bests", "www.bests.com")
# c.add_memeber("ahmed", "groshar")
# print c.list_m

#Q6
class StudentGPAList():
    def __init__(self, gpas_dict, dpt_name, let_gd_dictionary):
        self.gpas_dict = gpas_dict
        self.dpt_name = dpt_name
        self.letter_dict = let_gd_dictionary

    def sum(self):
        s = 0
        for i in self.gpas_dict.values():
            s+=i
        return s

    def avg(self):
        s = self.sum()
        return s/(len(self.gpas_dict))

    def convert_to_letter(self, gd):
        for i in self.letter_dict:
            if gd <= self.letter_dict[i][0] and gd >= self.letter_dict[i][1]:
                return i

gpa = StudentGPAList({"ahmet": 3.5, "omer": 3.6}, "CS", {"A": (4.0,3.5), "B": (3.5,3.0)})
# print gpa.convert_to_letter(3.6)
# print gpa.sum()
# print gpa.avg()

#Q7

class StudentGPAList():
    def __init__(self, gpas_dict, dpt_name, let_gd_dictionary):
        self.gpas_dict = gpas_dict
        self.dpt_name = dpt_name
        self.letter_dict = let_gd_dictionary

    def max(self):
        list_max = []
        max_gpa = max(self.gpas_dict.values())
        for key, val in self.gpas_dict.items():
            if val == max_gpa:
                list_max.append(key)
        return list_max
    def min(self):
        list_min = []
        min_gpa = min(self.gpas_dict.values())
        for key, val in self.gpas_dict.items():
            if val == min_gpa:
                list_min.append(key)
        return list_min
    def sum(self):
        s = 0
        for i in self.gpas_dict.values():
            s+=i
        return s
    def avg(self):
        s = self.sum()
        return s/(len(self.gpas_dict))

    def convert_to_letter(self, gd):
        for i in self.letter_dict:
            if gd <= self.letter_dict[i][0] and gd >= self.letter_dict[i][1]:
                return i

gpa7 = StudentGPAList({"ahmet": 3.5, "omer": 3.6}, "CS", {"A": (4.0,3.5), "B": (3.5,3.0)})
# print gpa7.max()
# print gpa7.min()

#Q8
class VendingMachine():
    def __init__(self, dict_of_items, number_of_sales= 0, total_sales_revenue=0):
        self.number_of_sales = number_of_sales
        self.total_sales_revenue = total_sales_revenue
        self.dict_of_items = dict_of_items

    def fetchItem(self, item,p):
        if p >= self.dict_of_items[item][0] and self.dict_of_items[item][1] >0:
            print "please take your item!"
            self.total_sales_revenue+=p
            self.number_of_sales +=1
        else:
            print "The amount of money entered is not enough"

vm = VendingMachine({"Item1":[1.50, 10], "Item2":[2.50, 5], "Item3":[3.50,4]})
# vm.fetchItem("Item1",2)
# print vm.number_of_sales
# print vm.total_sales_revenue
# vm.fetchItem("Item1",2)
# print vm.number_of_sales
# print vm.total_sales_revenue


#Q9
class VendingMachine():
    def __init__(self, dict_of_items, number_of_sales= 0, total_sales_revenue=0):
        self.number_of_sales = number_of_sales
        self.total_sales_revenue = total_sales_revenue
        self.dict_of_items = dict_of_items
        #new attrs
        self.dict_analytics = {}
        self.quant = 0

    def fetchItem(self, item,p):
        if p >= self.dict_of_items[item][0] and self.dict_of_items[item][1] >0:
            print "please take your item!"
            self.total_sales_revenue+=p
            self.number_of_sales +=1
            self.quant +=1
            self.dict_analytics[item] = self.quant
            self.quant-=1
        else:
            print "The amount of money entered is not enough"

    def analytics(self):
        for item in self.dict_analytics:
            print "Item: " + item + " Quantity Sold: " +  str(self.dict_analytics[item]) + "  Sales Volume: " + \
                  str(self.dict_of_items[item][0])


vm = VendingMachine({"Item1":[1.50, 10], "Item2":[2.50, 5], "Item3":[3.50,4]})
# vm.fetchItem("Item1", 1.50)
# vm.fetchItem("Item2", 2.50)
# vm.fetchItem("Item3", 3.50)
# vm.analytics()

#Q10

class Critic():
    def __init__(self, name, movies_dict):
        self.name = name
        self.movies_dict = movies_dict

    def filter(self, n):
        li = []
        for i in self.movies_dict:
            if n >= self.movies_dict[i]:
                li.append(i)
        return li
test = Critic('Melih', {'Hababam Sinifi':10, 'Hababam Sinifi Tatilde':8.5, 'Hababam Sinifi Askerde':5})
# print test.filter(8.5)


#Q11

class InstantExtreme():
    def __init__(self, li_int = []):
        self.li_int = li_int

    def instant_add(self,n):
        self.li_int.append(n)

    def instant_max(self):
        return max(self.li_int)

    def instant_min(self):
        return min(self.li_int)

# myds = InstantExtreme()
# myds.instant_add(9)
# myds.instant_add(2)
# myds.instant_add(1)
# print myds.instant_max()

#Q12
class ExtendedList():
    def __init__(self, li_int):
        self.li_int = li_int

    def mean(self):
        return  sum(self.li_int)/float(len(self.li_int))

    def mode(self):
        dict = {}
        for i in range(len(self.li_int)):
            if self.li_int[i] in dict:
                dict[self.li_int[i]] +=1
            else: dict[self.li_int[i]] = 1

        for i in range(len(dict.values())-1):
            # print dict.values()
            if dict.values()[i] != dict.values()[i+1]:
                return self.li_int[max(dict.values())]
        return "no mode"

    def median(self):
        if len(self.li_int) % 2 == 0:
            self.li_int.sort()
            return (self.li_int[len(self.li_int)/2] + self.li_int[(len(self.li_int)/2)-1])/2.0
        elif len(self.li_int) %2 == 1:
            self.li_int.sort()
            return (self.li_int[len(self.li_int)/2])

mylist = ExtendedList([1,3,4, 2,2,2])
# print mylist.mean()
# print mylist.median()
# print mylist.mode()

#Q13

class Shoe():
    def __init__(self, size, color, price):
        self.size = size
        self.color = color
        self.price = price
    def getSize(self):
        return self.size
    def getColor(self):
        return self.color
    def getPrice(self):
        return self.price


# c = Shoe(29,"green", 39)
# print c.getColor()


#Q14
class Shoe():
    def __init__(self, size, color, price):
        self.size = size
        self.color = color
        self.price = price
    def getSize(self):
        return self.size
    def getColor(self):
        return self.color
    def getPrice(self):
        return self.price
    def adjust_price(self, percentage):
        inc = percentage * self.price
        self.price +=inc

# c = Shoe(29,"green", 40)
# c.adjust_price(.5)
# print c.getPrice()


#Q15, 16, 17
class Pokemon:
    def __init__(self, name, health, attack):
        self.PokemonsName = name
        self.PokemonsHealth = health
        self.PokemonsAttack = attack
    def __str__(self):
        s =self.PokemonsName + " " +  str(self.PokemonsHealth) + " " +  str(self.PokemonsAttack)
        return s

    def hpboost(self, n):
        self.PokemonsHealth +=n
    def apboost(self, n):
        self.PokemonsAttack+=n

# p = Pokemon("pokemonX", "20","30")
# print p


#Q18

class Pet():
    def __init__(self, name = None):
        self.name = name

    def intro(self):
        if self.name == None:
            print("Hi, I am a pet without a name")
        else:
            print("Hi, I am %s")%self.name
# pet = Pet("bok")
pet = Pet()
# pet.intro()


#Q19

class StrCircus:
    def __init__(self, word = 'co-operative', flag = False):
        if not flag:
            self.word = word*3
            # print self.word
        self.word = word
    def pretty_print(self, flag = True):
        if flag:
            print '-'.join(self.word.split("-"))
        else:
            print '\n'.join(self.word.split("-"))

# test = StrCircus('bi-directional')
# test.pretty_print(False)

