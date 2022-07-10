# ENGR 101 INTRODUCTION TO PROGRAMMING
# PRACTICE SESSION WEEK 8

# REVISION
# this will print like rows and column number pairs 10 row and 10 columns
# for i in range(1,11):
#     for j in range(1,11):
#         print i,j," ",
#     print ''

#Q1
def word_hist(fn_input):
    if type(fn_input) == type(3) or type(fn_input) == type(1.0):
        fn_input = str(fn_input)
    print fn_input + ": " + "*" * len(fn_input)

# word_hist("the")
# word_hist("ENGR211")
# word_hist(213090080)
# word_hist(9.12613)

#Q2
def unique_elem(str_1, str_2):
    for i in range(len(str_1)):
        unique_to_str_1 = True
        for j in range(len(str_2)):
            if str_2[j] == str_1[i]:
                unique_to_str_1 = False

        if unique_to_str_1 == True:
            print str_1[i]

# unique_elem("hello", "hola")
# unique_elem('alyo', 'efendim')


def unique_(str1, str2):

    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i]==str2[j]:
                break
            if j+1 == len(str2):
                print str1[i]

# unique_("hello", "hola")
# unique_('alyo', 'efendim')

# Additional
# This program creates a mirror image of the letters on the left to the right
# and the letters from right to the left around the center of the string
def mirror(str1):
    x = len(str1)/2
    s = ''
    for i in range(len(str1)-1, x-1,-1):
        s += str1[i]

    for j in range(x-1, -1,-1):
        s += str1[j]
    print s

# mirror("nes_ev_neb")  # the output is: ben_ve_sen

#Q3
def string_reverse(input_string):
    output_string = ""
    for i in range(len(input_string) - 1, -1, -1):
        output_string += input_string[i]
    return output_string
# print string_reverse("sehir")

#Q4
def repeat_letters_v1(input_string, n):
    output_string = ""
    for i in range(len(input_string)):
        output_string += input_string[i]*n
    return output_string
# print repeat_letters_v1('bla',2)


def letters(input_string, n):
    output_string = ""
    for i in range(len(input_string)):
        for j in range(n):
            output_string += input_string[i]
    return output_string

# print letters('bla',2)

#Q5
def check_pass():
    password = raw_input("Please enter a password:\t")
    unique_elements = ""
    for i in range(len(password)):
        if len(unique_elements) == 0:
            unique_elements += password[i]
        else:
            not_found = True
            for j in range(len(unique_elements)):
                if unique_elements[j] == password[i]:
                    not_found = False
            if not_found:
                unique_elements += password[i]
    return unique_elements == password

# print check_pass()

# Second simplified version
def check_pass2():
    password = raw_input("Please enter a password 2: ")
    for i in range(len(password)):
        counter = 0

        for j in range(len(password)):
            if password[i] == password[j]:
                counter += 1
            if counter == 2:
                return False
    return True

# print check_pass2()



#Q6

from random import randint
def random_pass_gen(n):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    password = alphabets[randint(0, 25)]
    print password
    while len(password) <= n - 1:
        random_alphabet = alphabets[randint(0, 25)]
        not_in_password = True
        for i in range(len(password)):
            if password[i] == random_alphabet:
                not_in_password = False
            if not_in_password:
                password += random_alphabet
    return password

# print random_pass_gen(5)

def random_pass_gen2(n):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    password = ""
    for i in range(n):
        random_alphabet = alphabets[randint(0, 25)]
        password += random_alphabet
    return password

# print random_pass_gen2(6)



#Q7
def return_longer(str1, str2):
    if len(str1) > len(str2):
        return str1
    else:
        return str2

#print return_longer("abcdef", "abcde")


#Q8
def check_same(str1, str2):
    if len(str1) != len(str2):
        return False
    count = 0

    for i in range(len(str1)):
        if str1[i] == str2[i]:
            count += 1
    if count == len(str1):
        return True
    else:
        return False
# print check_same("abc", "abcd")


#Q9
def check_length(n):
    a=0
    for i in n:
        a+=1
    return a

# if check_length("awer") < 5:
#     print "The string's length is smaller than 5"
# else:
#     print "The string's length is bigger than 5"

#Q10
def is_length(strin, number1):
    if len(strin) == number1:
        return True
    else:
        return False

# print is_length("asc", 2)

#Q11
def change_letter(strn,char1,char2):
    temp=""
    for i in strn:
        if char1==i:
            temp+=char2
        else:
            temp+=i
    print temp

#change_letter("also","w","a")


#Q12
def word(word1):
    a=0
    while True:
        if len(word1)< a:
            return a
        a+=1

# print word("welcome")


#Q13
def cut_string(string1,letter1):
    temp=""
    for i in string1:
        if letter1==i:
            temp = i
        else:
            temp+=i
    return temp

#cut_string("words","d")


#Q14
def count_letter(sentence,letter):
    letter_count = 0
    for i in sentence:
        if letter==i:
            letter_count+=1
    return letter_count

# count_letter("You shall not pass","s")


#Q15
def repeat(n):
    a=0
    for i in n:
        a+=1
        print i * a

#repeat("hello")


#Q16
def getMax(a, b, c):
    if len(a) > len(b) and len(a) >len(c):
        return a
    elif len(b) > len(a) and len(b) > len(c):
        return b
    else:
        return c

#getMax("aa","word","welcome")


#Q17
def insert_letter(word,letter1):
    count=0
    for i in range(len(word)):
        if letter1==word[i]:
            count+=1
            if count == 2:
                return i

#print insert_letter("welcomehome","e")



#Q18
def remove_ind(word,ind):
    output_word = ""
    for i in range(len(word)):
        if i!=ind:
            output_word+=word[i]
    return output_word
#print remove_ind("asdf",2)

#Q19
def remove_odds(word):
    output_word = ""
    for i in range(len(word)):
        if i%2==0:
            output_word+=word[i]
    return output_word

#print remove_odds("flower")



#Q20
def change_first_last(word):
    output_word=word[-1]+word[1:-1]+word[0]
    return output_word

#print change_first_last("hello")




