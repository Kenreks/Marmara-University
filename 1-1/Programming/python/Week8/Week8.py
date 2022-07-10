"""
Week 8 Lecture script
"""

#Check and set your current directory
import os
cwd=os.getcwd() #This is your current working directory
print cwd

import os
preferred_dir="C:\Users\Mujde\Documents\ISTANBUL_SEHIR_UNI" \
              "\ENGR 101_SPRING 2019_HMA\Week 8" #Please set yours properly
os.chdir(preferred_dir) #Now you have changed your working directory to your preferred directory
#as you defined above. Please set yours properly!
cwd=os.getcwd()
print cwd

#SLIDE 17
a=['spam', 2.0, 5, [10, 20]]
print a[0]
print len(a)
print a[len(a)-1]

#SLIDE 19: indexing a list
cheeses = ['Cheddar', 'Edam', 'Gouda']
print cheeses[0]

#SLIDE 20: Lists are mutable
numbers = [17, 123]
numbers[1] = 5
print numbers

#SLIDE 22: in operator in lists
cheeses = ['Cheddar', 'Edam', 'Gouda']
print 'Edam' in cheeses #True
print 'Brie' in cheeses #False

#SLIDE 23: Traversing a list with a for loop
for cheese in cheeses:
    print cheese

#SLIDE 24: Traversing a List
numbers = [2, 3,5]
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print numbers

for x in []:
    print 'This never happens.'

for x in [""]:
    print 'This happens once.'

#Although a list can contain another list, the nested list still
# counts as a single element.
mylist=['spam', 1, ['Brie', 'Roquefort', 'Pol le Veq'], [1, 2, 3]]
print mylist[2]

#SLIDE 25: List operations
a = [1, 2, 3]
b = [4, 5]
c = a + b
print c

print [0] * 4
print [1,2] * 4

#SLIDE 26: List slices
t = ['a', 'b', 'c', 'd', 'e', 'f']
print t[1:3]
print t[:4]
print t[3:]

#SLIDE 27: List slices
t = ['a', 'b', 'c', 'd', 'e', 'f']
print t[:]#default start_index=0, default_end_index=end

t[1:3] = ['x', 'y'] #lists are mutable
t[1:4] = ['x', 'y']
print t

#SLIDE 28: List slices
x = [1, 2, 3, 4, 5, 6]
x[1:3] = [11,12]
print x #[1, 11,12, 4, 5, 6]

x = [1, 2, 3, 4, 5, 6]
x[1:3] = [11]
print x #[1, 11, 4, 5, 6]-shortening length


x = [1, 2, 3, 4, 5, 6]
x[1:3] = [10, 12, 13]
print x #[1, 10, 12, 13,4, 5, 6]-extending length

#SLIDE 29: LIST Methods-append
#Adding a new ELEMENT to the end of a list
t = ['a', 'b', 'c']
t.append('d')
print t

t = ['a', 'b', 'c']
r=['z','m']
t.append(r) #appends the list as one ELEMENT, to append all the elements we wil use EXTEND method later
print t
print(t+r)

#SLIDE 30: List methods-insert
t = ['a', 'b', 'c']
t.insert(1, 'd') # 1: index for insertion, ‘d’: item to be inserted
print t #['a', ‘d’, 'b', 'c']

#SLIDE 31: List methods-extend
t = ['a', 'b', 'c']
r=['z','m']
t.extend(r) #appends the list as one ELEMENT, to append all the elements we wil use EXTEND method later
print t

#SLIDE 32: List methods-sort
t = ['d', 'c', 'e', 'b', 'a']
t.sort()
print t

t=[2, 4, 1]
t.sort()
print t

t=["a",3, 1,"z"]
t.sort()
print t

sorted_t = t.sort()
print sorted_t #List methods being void, they will return None

#SLIDE 33: Deleting elements with pop, knowing the index
t = ['a', 'b', 'c']
x = t.pop(1) #delete the element with index 1 and return the element, which is b
print t #['a', 'c']
print x # b

t = ['a', 'b', 'c']
x = t.pop() #If you do not provide an index, pop removes the last element
print t #['a', 'b']

#SLIDE 34: Deleting elements with del
#If you don’t need the removed value, you can use the del operator:
t = ['a', 'b', 'c']
del t[1]
print t

#SLIDE 35: Deleting elements with remove
#no indexing needed, return value is None
t = ['a', 'b', 'c']
t.remove('b')
print t

#SLIDE 36: Deleting a set of elements
t = ['a', 'b', 'c', 'd', 'e', 'f']
del t[1:5]
print t

#SLIDE 37: Lists and strings
s = 'spam'
t = list(s) #to convert a string into a list of characters
print t

#SLIDE 38: Lists and strings-split
#Splits the string into list of words. Result is a list
s = "Istanbul Sehir University"
t = s.split()
print t

#SLIDE 39: Lists and strings-split
s = 'spam-spam-spam'
delimiter = '-'
print s.split(delimiter) #split is a string method

#SLIDE 40: Lists and strings-join
t = ['Istanbul', 'Sehir', 'University']
my_string = ' ' # contains a space
print my_string.join(t) #Join is a string method
print type(my_string.join(t)) #result is a string

my_string = '-' # contains a space
print my_string.join(t)

#SLIDE 41: Objects and values
a = [1, 2, 3]
b = [1, 2, 3]
print a is b #FALSE: same values but different objects

#SLIDE 42: Object and Aliasing
a = [1, 2, 3]
b = a
print a is b #TRUE

#SLIDE 43: List arguments
def delete_head(t):
    del t[0]
letters = ['a', 'b', 'c']
delete_head(letters)
print letters

#SLIDE 44: Calling methods on lists
t1 = [1, 2]
t2 = t1.append(3)#append is MODIFYING list t1 , not creating a new list
print t1
t1.append(4)
print t1

print t2#append being a void function, return is none

#SLIDE 45: List arguments
t1 = [1, 2]
t3 = t1 + [3] #creating a new list, rather than modifying
print t3

print t1 is t3 #False as created a new list

#SLIDE 46: List arguments
#original list is unmodified
def tail(t):
    return t[1:]
letters = ['a', 'b', 'c']
rest = tail(letters)
print rest

#SLIDE 49: MAP
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res
letters = ['a', 'b', 'c']
print capitalize_all(letters)

#SLIDE 50: FILTER
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res
letters = ['a', 'B', 'c']
print only_upper(letters)

#SLIDE 51: REDUCE
def add_all(t):
    total = 0
    for x in t:
        total += x #total=total+x
    return total
nums = [1, 2, 3]
print add_all(nums)

def add_all(t):
    total = ""
    for x in t:
        total += x #total=total+x
    return total
letters = ['a', 'b', 'c']
print add_all(letters )

#SLIDE 54: Exercise 1
def change_item(t):
    for i in range(len(t)):
        if type(t[i])==int:
            t[i]=str(t[i])
    return t
t=[1,2,'sr',4,'m']
print change_item(t)

#SLIDE 55: Exercise 2
def reverse(t1):
    t2=[]
    for i in range(len(t1)):
        t2.append(t1[len(t1)-1-i])
    return t2
my_list=['2','m','33']
print reverse(my_list)

#SLIDE 56: Exercise 3
def remove_squares(mylist):
    del_elements=[]
    for i in range(len(mylist)):
        item=mylist[i]
        if item*item in mylist[i+1:]: #check if squared value exists in the remaining part of the list
            del1=item
            del2=item*item
            if del1 not in del_elements:
                del_elements.append(del1)
            if del2 not in del_elements:
                del_elements.append(del2)
    print del_elements #debugging
    for j in del_elements:
        mylist.remove(j) #delete the element not using index
    return mylist
print remove_squares([1,2,6,4,13,36,18])