

import random

#Q1
def sum_from_n_to_0(n):
    if n == 1:
        return 1
    return n + sum_from_n_to_0(n-1)

# print(sum_from_n_to_0(5))

#Q2
def sum_all_even_to_0(even):
    if even == 2:
        return 2
    return even + sum_all_even_to_0(even-2)

# print(sum_all_even_to_0(6))



#Q3

def sum_all_even_to_0_v2(even):
    if even % 2 == 1:
        even -=1
    if even == 2:
        return 2
    return even + sum_all_even_to_0(even-2)

# print(sum_all_even_to_0_v2(7))

#Q4

def add_negatives(n):       # or
    if n == -1:             # if n == 0:
        return n           #     return 0
    return n + add_negatives(n+1)

# print(add_negatives(-3))

# Q5
k = 0
def num_of_digits(n):
    global k
    if n == 0:
        return k
    k+=1
    return num_of_digits(n/10)

# print(num_of_digits(221))


k2 = 0
def num_of_digits_v2(n,p):
    if n == 0:
        return p
    p+=1
    return num_of_digits_v2(n/10,p)

# print(num_of_digits_v2(21,k2))
# # demonstration of how to change a value of a variable outside a function using return
# k2 = num_of_digits_v2(21,k2)
# print "k2 is " + str(k2)

# Q6

def num_of_dig_for(n):
    count = 0
    for i in range(len(str(n))):
        count+=1
    return count

# print(num_of_dig_for(1233))

def num_of_dig_while(n):
    count = 0
    i = 0
    while i < len(str(n)):
        count+=1
        i+=1
    return count

# print(num_of_dig_while(1234))



#Q7

def multiple_3(n):
    if n == 1:
        return 3
    else:
        return multiple_3(n - 1) + 3

# print multiple_3(10)


# Non-recursive
def multiple_3_loop(n):
    for i in range(1,n+1):
        print i * 3

# multiple_3_loop(10)


#Q8

def power(x, y):
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)
# print power(2,4)

# Non-recursive Question 2
def power1(x, y):
    start = 1
    for i in range(y):
        start = start * x
    return start
# print power1(2, 4)


#Q9

def sum_digits(number):
    if number == 0:
        return 0
    else:
        # (227 % 10 == 7) gives the rightmost digit,
        # integer division by 10 removes the rightmost digit (227 / 10 is 22)
        return (number % 10) + sum_digits(number / 10)
# print sum_digits(3642)


# Non-Recursive
def digits_sum(number):
    sum = 0
    for i in str(number):
        sum += int(i)
    return sum
# print digits_sum(2362)


#Q10

def check(i, t):
    while i <= 100:
        if i % 2 == 0:
            t += i
        i += 1
    return t


# Recursion
def rec_check(i, t):
    if i > 100:
        return t
    elif i % 2 == 0:
        t += i
    return rec_check(i + 1, t)
# print check(98, 2)
# print rec_check(98,2)

#Q11

def recur_sum_(start, max):
   if start>max:
       return max    #mistake 1: 0 instead of max becuase we stop here
   else:
       return 1 + recur_sum_(start+1, max) #mistake 2: start instead of 1

# print recur_sum_(1, 100)

def recur_sum(start, max):
   if start>max:
       return 0    #mistake 1: 0 instead of max becuase we stop here
   else:
       return start + recur_sum(start+1, max) #mistake 2: start instead of 1

# print recur_sum(1, 100)

def recur_sum_loop(start, max): #takes same arguments! For consistency.
   sum = 0
   for i in range(start, max+1):
       sum += i
   return sum

# print recur_sum_loop(1, 100)

#Q12

def useless(x):
    a = x
    while a>0:
        a-=1
        if a==20:
            a=100
        print a
# useless(100)


#Q13

def fibonacci(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


def fibonacci_with_while(n):
    a, b = 1, 1
    k = 0
    while k < n - 1:
        a, b = b, a + b
        k += 1
    return a

# print fibonacci_with_while(4)

def F_with_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return F_with_recursive(n-1)+F_with_recursive(n-2)

# print F_with_recursive(4)

#Q14

def multiply_from_n_to_zero(n):
    if n == 0:
        return 1
    return n * multiply_from_n_to_zero(n-1)
# print(multiply_from_n_to_zero(4))

#Q15
def print_until_true(n):
    while True:
        rand_num = random.randint(0,n**2)
        print(rand_num, n)
        if rand_num == n:
            print(True)
            break
# print_until_true(4)

#Q16

def countdown(n1, n2):
    for k in range(n1, n2, -1):
        if k != n2:
            print k
        else:
            break
# countdown(15,8)

#Q17

def countdown_with():
    number1 = int(raw_input("Enter your first number: "))
    number2 = int(raw_input("Enter your second number: "))
    while number2 >= number1:
        number1 = int(raw_input("Enter your first number: "))
        number2 = int(raw_input("Enter your second number: "))
    countdown(number1, number2)
# countdown_with()

#Q18
# while True:
#     enter_number = int(raw_input("Enter a number:"))
#     if enter_number == random.randint(1,3):
#         print('Right Guess!')
#         break

#Q19
#it will print true infinitly.
#the rand_num will always be an even number so it will never get to the else statement.
# while True:
#     rand_num = random.randrange(0, 10, 2)
#     print rand_num
#     if rand_num%2==0:
#         print(True)
#     else:
#         print(False)
#         break

#Q20
# rand_letter = random.choice('abc')
# if rand_letter == 'a':
#     print('The letter is ' + rand_letter)
# elif rand_letter == 'b':
#     print('The letter is ' + rand_letter)
# elif rand_letter == 'c':
#     print('The letter is ' + rand_letter)


# print "Welcome Ahmet!\nPlease enter the number of the service:\n1.	Withdraw Money\n2.	Deposit Money\n3.	Transfer Mone\n4.	My Account Information\n5.	Logout"
