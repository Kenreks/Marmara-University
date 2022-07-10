"""
Week 11 Lecture script: Dictionaries
"""

#Check and set your current directory
import os
cwd=os.getcwd() #This is your current working directory
print cwd

import os
preferred_dir="C:\Users\Mujde\Documents\ISTANBUL_SEHIR_UNI" \
              "\ENGR 101_SPRING 2019_HMA\Week 11" #Please set yours properly
os.chdir(preferred_dir) #Now you have changed your working directory to your preferred directory
#as you defined above. Please set yours properly!
cwd=os.getcwd()
print cwd

#SLIDE 15
eng2sp = dict()
print eng2sp

#SLIDE 16
eng2sp['one'] = 'uno'
print eng2sp

eng2sp['two'] = 'dos'
print eng2sp

eng2sp['two']='iki'
print eng2sp

#or
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print eng2sp

#SLIDE 17: Access
print eng2sp['two']
print eng2sp['four']

print len(eng2sp)

#SLIDE 18: in operator in dictionaries checks existence in key
print 'one' in eng2sp
print 'uno' in eng2sp  #checks existence only in keys

#if you want to check existence in values rather then keys
vals = eng2sp.values()
print vals
print 'uno' in vals #if you want to check existence in values rather then keys

##SLIDE 21: counters implementation
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
print histogram("ankara")

def print_hist(h):
    for c in h: #traversing the keys
        print c, h[c] #printing the key and corresponding value

h = histogram('ankara')
print_hist(h)

print_hist(histogram("ankara"))

##SLIDE 23: Reverse Lookup: Find a value
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    return -1
eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print reverse_lookup(eng2sp, "uno")
print reverse_lookup(eng2sp, "forto")

##SLIDE 25: Getting all keys and values as a list
hist = {'a': 1, 'p': 1, 'r': 2, 't': 1}
print hist.keys()
print hist.values()

##SLIDE 26: Deleting from a dictionary
hist = {'a':1,'p':1,'r':2,'t':1,'o':1}
a = hist.pop('a') #providing key and so deleting the corresponding key&value pair
print a
print hist

del hist['r'] #delete the item
print hist

##SLIDE 28-29: Dictionaries and lists
#Create a dictionary that maps from frequencies to    letters
def invert_dict(d):
    inv = dict()
    for key in d:
        val = d[key]
        if val not in inv:
            inv[val] = [key]
        else:
            inv[val].append(key)
    return inv
hist={'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}
print invert_dict(hist)

#SLIDE 33: Memos
def fibonacci(n):
    if n == 0:
        res=0
    elif n == 1:
        res=1
    else:
        res = fibonacci(n-1) + fibonacci(n-2)
    return res
print fibonacci(4)

import timeit
start = timeit.default_timer()
print fibonacci2(30)
stop = timeit.default_timer()
print('Time: ', stop - start)


known = {0:0, 1:1}
def fibonacci2(n):
    if n in known:
        return known[n]
    res = fibonacci2(n-1) + fibonacci2(n-2)
    known[n] = res
    return res

print fibonacci(1)
print known

#SLIDE 34: EXERCISE 1
""" Write a function that takes a list and a dictionary as input.
 It should check if the elements of the list exist as values in the dictionary. 
 If so, then return those values as a list."""
def check_list(mylist,mydictionary):
    existing=[]
    for i in mylist:
        if i in mydictionary.values():
            existing.append(i)
    return existing

print check_list([1,2,3,4],{'one':1,'five':5,'four':4})

#SLIDE 35: EXERCISE 2
"""Imagine a dictionary with the structure {name:height}. 
Define a function height_filter that takes such
 a dictionary and a number h as inputs and returns a list 
 containing names of people with height greater than h."""
def height_filter(mydict,h):
    new_dict={}
    for key in mydict:
        if mydict[key]>h:
            new_dict[key]=mydict[key]
    return new_dict

print height_filter({"Gul":168, "Nazli":155, "Merve":170, "Omer":180, "Cetin":180}, 165)


#SLIDE 36: EXERCISE 3
""" Define a function height_reverse_lookup that takes the dictionary from question 7 as input
 and returns its reverse dictionary i.e. the keys will be heights and values will be names 
 (or list of names in case multiple people have the same height)."""
def height_reverse_lookup(mydict):
    new_dict={}
    old_key=mydict.keys()
    old_vals=mydict.values()
    for i in range(len(mydict)):
        if old_vals[i] not in new_dict:
            new_dict[old_vals[i]]=old_key[i]
        else:
            new_dict[old_vals[i]] = [new_dict[old_vals[i]]] #turn the string into list
            new_dict[old_vals[i]].append(old_key[i])
    return new_dict
print height_reverse_lookup({"Gul":168, "Nazli":155, "Merve":170, "Omer":180, "Cetin":180})