#q1

def square(x):
    result = x * x
    return result
# print square(5) * square(5)


#q2

def isdivisible(n):
    str_n = str(n)
    biggest_num = max(str_n)
    return int(biggest_num) % 3 == 0
# print(isdivisible(945))

#q3

def quotient(x,y):
    return x/y

def remainder(x,y):
    return x % y

# print quotient(11,3)
# print remainder(11,3)

# in the following function, the two possible outputs should be both returned or printed.
def remainder_0(x,y):
    if remainder(x,y) == 0:
        return quotient(x,y)
    else:
         return "The number can not be divided without remainder"

# print(remainder_0(9, 4))

#q4

def fahrenheit(T_in_celsius):
    return  (T_in_celsius * 9.0 / 5) + 32


def fahrenheit_range(x, y):
    for t in range(x, y+1):
        print(str(float(t))+": "+str(fahrenheit(t)))

# fahrenheit_range(22, 27)

#q5

def factorial(n):
    fact = 1
    while n > 1:
        fact *= n
        n -=1
    return fact

# print(factorial(5))


#q6

import math
def area(radius):
    area = math.pi * radius ** 2
    return area

def distance_and_area(x1,y1,x2,y2):
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
    return round(area(distance),5)

# print distance_and_area(8,7,4,4)


#q7

def add_even_numbers(s,e):
    sum = 0
    for i in range(s+1, e):
        if i % 2 == 0:
            sum+=i
    print sum
# add_even_numbers(4,9)


#q8
# brute force gready_prime function
def greedy_prime(n):
    j=2
    for i in range(2, n):
        # print i
        if n % i != 0:
            j+=1
            if j == n:
                print str(n) + " is a prime number"
                break
        else:
            print str(n) + " is not a prime number"
            break
# greedy_prime(11)


#q9

def divisble_by_2_3(number1, number2, number3):
    for i in range(1, number1):
        if i % number2 == 0  and i % number3 == 0:
            continue
        else:
            return False
    return True
# print(divisble_by_2_3(6, 1,1 ))


#q10
def vote_class():
    age = raw_input("Please enter your age:")
    if int(age) >= 18:
        print "you are able to vote in the United States!"
    else:
        print "you are not able to vote in the United States!"

# vote_class()


#q11

# def ask_hadi():
#     whom_do_you_love = raw_input("Whom do you love?:")
#     return whom_do_you_love
# while ask_hadi() != "myself":
#     print "Wrong answer!"
# print "I love myself"

def ask_beloved():
    while True:
        whom_do_you_love = raw_input("Who do you love?:")
        if whom_do_you_love != "myself":
            print "Wrong answer!"
        else:
            print "I love myself"
            break

# ask_beloved()

#q12
def height_even():
    height = raw_input("what is your height?:")
    if int(height) % 2 == 0:
        return True
    else:
        return False
# print(height_even())

#q13
#1
# while True:
#     print(4)
#     break
#2 (create a variable)
# a = 0
# while a <= 0:
#     a +=1
#     print(4)


#q14

import random
def guess():
    rand_num = random.randint(0, 100)
    # print(rand_num)
    input = int(raw_input("Enter a number:"))
    while input != rand_num:
        if input > rand_num:
            print "Your input is larger than the random number"
            input = int(raw_input("Enter a number:"))
        elif input < rand_num:
            print "Your input is smaller than the random number"
            input = int(raw_input("Enter a number:"))
    print "Number Found"
# guess()

#q15

import random
def input_num():
    input = int(raw_input("Enter a number:"))
    return input
def guess2():
    rand_num = random.randint(0, 100)
    user_input = -1
    while user_input != rand_num:
        user_input = input_num()
        if user_input > rand_num:
            print "Your input is larger than the random number"
        elif user_input < rand_num:
            print "Your input is smaller than the random number"
    print "Number Found"
# guess2()


#Q16
# in this implementation if the input is incorrect the program terminates and does not
# prompt the user to enter his parameters again, we solve this below by adding a while loop
def change_username():
    password=1234
    currentusername="KRAL"
    inputname = raw_input("Enter your current username: ")
    if inputname==currentusername:
       inputpassword = int(raw_input("Enter your password for " + currentusername+": "))
       if inputpassword==password:
           newname = raw_input("Enter your new username: ")
           if newname !=None:
               print "your user name changed succesfully"
# change_username()


def change_username2():
    password=1234
    currentusername="KRAL"

    while True:
        inputname = raw_input("Enter your current username: ")
        if inputname==currentusername:
           inputpassword = int(raw_input("Enter your password for " + currentusername+": "))
           if inputpassword==password:
               newname = raw_input("Enter your new username: ")
               if newname !=None:
                   print "your user name changed succesfully"
# change_username2()


#q17

def func(a, b, c):
    if a == b:
        return a
    elif b == c:
        return b
    elif a == c:
        return c
# print(func(3, 5, 5))

#q18

def egypt(n):
    str_add = ""
    for i in range(n):
        str_add += str(i)
        print(str_add)
# egypt(5)


#q19

# num = raw_input("Enter a number:")
# if num == 3:
#     print True
# elif num != 3:
#     print False

# # we need to convert the str type to int
#
# num = int(raw_input("Enter a number:"))
# if num == 3:
#     print True
# elif num != 3:
#     print False

#20

# a = 10
# b = 5
#
# if a > b:
#     c = 3
# while a < b:
#     c +=1
#     if a > b:
#         a = 7
#         b = 6
#         break
# while a > 2:
#     c += 2
#     a -=5
#     while c > 1:
#         c -=2
#         a +=1
#         b -=1
#         break
# print a
# print b
# print c



