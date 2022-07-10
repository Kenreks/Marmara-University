"""
Week 10 Lecture script
"""

#Check and set your current directory
import os
cwd=os.getcwd() #This is your current working directory
print cwd

import os
preferred_dir="C:\Users\Mujde\Documents\ISTANBUL_SEHIR_UNI" \
              "\ENGR 101_SPRING 2019_HMA\Week 10" #Please set yours properly
os.chdir(preferred_dir) #Now you have changed your working directory to your preferred directory
#as you defined above. Please set yours properly!
cwd=os.getcwd()
print cwd

#SLIDE 8: Tuples are immutable so can be used as keys in dictionaries
a= (1,2)
b= [1,2]

c = {a: 1}     # OK
print c
print c[a]
print c[(1,2)]
c = {b: 1} #mutable keys are not allowed in dictionaries

#SLIDE 10
t1 = 'a',
print type(t1) #tuple

#SLIDE 11
t2 = ('a')
print type(t2) #string

t3 = ('a',)
print type(t3) #tuple

t4 = ('a','b')
print type(t4) #tuple

t = tuple()
print t
print type(t)

#SLIDE 12
#argument as a string
t = tuple('lupins')
print t

#argument as a list
seq=['m','u']
t = tuple(seq)
print t

#argument as a tuple
seq=('m','u')
t = tuple(seq)
print t

#SLIDE 13: Tuples – Accessing Items
t = ('a', 'b', 'c', 'd', 'e')
print t[0]
print type(t[0])#string

print t[1:3]
print type(t[1:3]) #tuple

#SLIDE 14: Tuples are immutable
t[0] = 'A'

t = ('A',) + t[1:]
print t

#SLIDE 15: Tuple Assignment
#swapping the values of two variables
a=1
b=2
a, b = b, a
print a,b

a=3
b=4
c=b,a
print c

a=1
b=2
a, b = b+a, a
print a,b

a, b = 1, 2,3 #error

(a,b,c)=(1,2,3)
print (a,b,c)


#SLIDE 16: Tuple Assignment
addr = 'monty@python.org'
print addr.split('@')

#a list on the right hand side of the tuple assignment
(uname, domain) = addr.split('@')
print uname
print domain
print (uname, domain)

#SLIDE 17: Tuple as a Return value
def min_max(t):
    return min(t), max(t)
a, b = min_max([1,2,3,4])
print a,b


#SLIDE 18: Variable length argument tuples
#gather multiple arguments into a tuple
def printall(*args):
    print args
printall('a', 1, 2)
printall(1, 2)

#SLIDE 19: Pass the sequence to a function as multiple arguments
#scatter a sequence into multiple arguments
def test(a,b):
    return a+b
t = (2, 3)
print test(*t)

t2=("a","b")
t3=["c","d"]
print test(*t2)
print test(*t3)

#SLIDE 20: Lists and Tuples
#a list of tuples
t = [('a', 0), ('b', 1), ('c', 2)]
for letter, number in t:
    print number, letter

# SLIDE 21: Dictionaries and Tuples
#Dictionaries have a method called items that returns
#  a list of tuples, where each tuple is a key-value
d = {'a':0, 'b':1, 'c':2}
t = d.items()
print t

# SLIDE 22: Dictionaries and Tuples
#Conversely, you can use a list of tuples to initialize a new dictionary
t = [('a', 0), ('c', 2), ('b', 1)]
d = dict(t)
print d

# SLIDE 23: Dictionaries and Tuples
#Traversing the keys and values of a dictionary
for key, val in d.items():
    print val, key

# SLIDE 25: Dictionaries and Tuples
directory={}
directory[("Ozaltin", "Meryem")] = "5449999999"
directory[("Kaplan", "Nihal")] = "5339999999"
print directory
# traverse this dictionary
for last, first in directory:
    print first, last, directory[last,first]

# SLIDE 26: Comparing Tuples
print (0, 1, 2) < (0, 3, 4)#True
print (0, 1, 2000000) < (0, 3, 4)#True
print (0, 5, 2000000) < (0, 3, 4)#False

# SLIDE 29: Exercise 1
def count_frequency(str):
    freq = {} #letters as keys and frequencies as counts
    for letter in str:
        if letter not in freq: # I have not seen this letter before
            freq[letter] = 1 # since it is the first time I have seen this letter
        else: # I must have seen this letter before
            freq[letter] += 1
    return freq

print count_frequency("ankara")

def print_letters_ordered_by_freq(str):
    freq_count = count_frequency(str)
    freq_lst = []
    for letter, freq in freq_count.items():#freq_count.items is a list of tuples
        freq_lst.append((freq, letter)) # a list of tuples with values swapped
    freq_lst.sort(reverse = True)
    for freq, letter in freq_lst:
        print letter, freq

print_letters_ordered_by_freq("ankara")

liste=[1,5,3]
liste=[(3,"m"),(1,"a"),(5,"b")]
liste.sort(reverse = True)
print (liste)

# SLIDE 31: Exercise 2
def ave_first_exam(mylist):
    sum=0
    count=0
    for i in range(len(mylist)):
        if type(mylist[i])==tuple:
            t=mylist[i]
            sum=sum+t[0]
            count=count+1
    return sum*1.0/count

exam_list = ["john", (40, 70), "murat", (20, 30), "faruk", (35, 55), "ahmet", (80, 90)]
print ave_first_exam(exam_list)

# SLIDE 33: Exercise 3
def charmap(string):
    new_dict={}
    for i in range(len(string)):
        if string[i] not in new_dict:
            new_dict[string[i]]=string.index(string[i]),
            indi = string.index(string[i]) #find the index of the letter in the string
        else:
            new_string=string[indi+1:]
            print new_string
            new_dict[string[i]] = new_dict[string[i]]+(indi+1+new_string.index(string[i]),)
            indi=new_string.index(string[i]) #find the index of the letter in the NEW string
    return new_dict

print charmap("ankara")
print charmap("mujde")
print charmap("Hello World")


di={"a":1,"b":2}
print di
di["a"]=111
print di