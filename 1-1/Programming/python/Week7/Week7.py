"""
Week 7 Lecture script
"""

#Check and set your current directory
import os
cwd=os.getcwd() #This is your current working directory
print cwd

import os
preferred_dir="C:\Users\Mujde\Documents\ISTANBUL_SEHIR_UNI" \
              "\ENGR 101_SPRING 2019_HMA\Week 7" #Please set yours properly
os.chdir(preferred_dir) #Now you have changed your working directory to your preferred directory
#as you defined above. Please set yours properly!
cwd=os.getcwd()
print cwd

#SLIDE 13: Strings
fruit = 'banana'
letter = fruit[1]
print letter

print fruit[0]
print type(fruit[0])

#SLIDE 14: len function of strings (gives the length of the string)
print len(fruit)

length=len(fruit)
last_char = fruit[length]
print last_char
last_char2 = fruit[length-1]
print last_char2

#SLIDE 16: Traversal with a for loop
for char in fruit: #traverses each char in fruit
    print char#remember , suppresses new line

for i in range(len(fruit)): #traverses each char in fruit
    print fruit[i]#remember , suppresses new line

#SLIDE 17: Traversal with a while loop
index = 0
while index < len(fruit):
    letter = fruit[index]
    print letter
    index = index + 1

#SLIDE 18: String slices
#start_index included, but end_index is not!
s = "Istanbul"
print s[0:3]  # prints Ist
print s[2:8]  # prints tanbul

#SLIDE 19
#Remember end_index is not included!
fruit = 'banana'
print fruit[:3]#start index=0 end index=3: ban
print fruit[3:]#start index=3 end index=6: ana

#negative indices:-1 is the last char
print fruit[-4:-1] # prints nan
print fruit[:-1]   # all until last char, prints banan

#SLIDE 20: String are immutable
greeting = 'Hello, world!'
greeting[0] = 'J'

new_greeting = "J" + greeting[1:]
print new_greeting

#SLIDE 21: Searching
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1
word="Search example"
letter=" " #Note that the above function will only return
#the first index if the letter appears more than once
print find(word, letter)

#SLIDE 22: Looping and counting
def count(word, my_letter):
    count = 0
    for letter in word:
        if letter == my_letter:
            count = count + 1
    return count
word="Search example"
my_letter="e"
print count(word, my_letter)

#SLIDE 23: String methods
word = 'banana'
print word.upper()
#method find returns index if found and -1 otherwise.
print word.find('a') #finds the first index where specified letter appears
print word.find('e') #-1 means no such a letter found
print word.find('na') #finds the first index where specified slice starts
print word.find('na', 3) #start index=3, end_index=length by default
print word.find('n', 1, 3) #starting index(0 by default) and ending index(length by default)

#SLIDE 24: in operator
val = "a" in "banana"
print val  # prints True

print "seed" in "banana" # prints False
print "ana" in "banana" # prints True

#SLIDE 25: Relational operators in strings
#checks alphapetical order and length
#alphabetical order you would use with a dictionary,
#except that all the uppercase letters come before all the lowercase letters
word="banana"
word="ayse"
word="zebra"
word="BANANA"
if word < "banana":
    print "Your word," + word + ", comes before banana."
elif word > "banana":
    print "Your word," + word + ", comes after banana."
else: # then the string is a ‘banana’
    print "All right, bananas."

#SLIDE 28: Exercises
def has_no_e(word):
    for letter in word:
        if letter == 'e':
            return False
    return True
print has_no_e("banana")
print has_no_e("hello")

#prints TRUE only if each letter of word is available in the next string "available"
def uses_only(word, available):
    for letter in word:
        if letter not in available:
            return False
    return True
print uses_only("hello","banana")
print uses_only("hello","zebra")
print uses_only("hel","hello")

#SLIDE 30: Palindrome
def is_palindrome(word):
    i = 0
    j = len(word)-1
    while i<j:
        if word[i] != word[j]:
            return False
        i = i+1
        j = j-1
    return True

print is_palindrome("hello")
print is_palindrome("madam")

#SLIDE 33: Repeat letters
def repeat_letters(stri,n):
    new_str=''
    for letter in stri:
        new_str=new_str+letter*n
    return new_str

print repeat_letters("bla", 2)
print repeat_letters("sehir", 3)

#SLIDE 34: Second occurence of a letter
def find_letter(word,letter1):
    count=0
    for i in range(len(word)):
        if letter1==word[i]:
            count=count+1
            if count == 2:
                return i
print find_letter("welcomehome","e")
print find_letter("banana","a")

#SLIDE 35: Second occurence of a letter
def cut_string(str1,letter1):
    ind=0
    new_str=''
    for letter in str1:
        if letter==letter1:
            exists=True
            break
        ind = ind + 1  # finds the index if letter exists
        exists = False
    if exists:
        for j in range(ind,len(str1)):
            new_str=new_str+str1[j]
        return new_str
    else:
        return "nothing to cut"

print cut_string("words","r")
print cut_string("words","z")
print cut_string("banana","a")

