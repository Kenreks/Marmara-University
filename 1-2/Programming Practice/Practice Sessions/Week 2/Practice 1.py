# Q1

def Q_1(old_file,new_file):
    open_old = open(old_file) # default in r mode
    open_new = open(new_word,'w') # open in write mode
    for line in open_old:
        if line[0] != "#":
            open_new.write(line)
    open_new.close()
    open_old.close()



# Q2

def Q_2(current_img,new_img):

    open_current_img = open(current_img, "rb") # open in read mode
    open_new_img = open(new_img, "wb") # open in write mode

    for line in open_current_img:
        open_new_img.write(line)
    open_new_img.close()
    open_current_img.close()

# Q3
import os
def Directory(path,suf):
    all_files = os.listdir(path)
    names = [] # answer (file names including suf)
    for name in all_files:
        file_path = os.path.join(path,name)
        if os.path.isfile(file_path): # if its a file
            if suf in name:
                names.append(name)
        else: # if its a dirc
            names += Directory(file_path,suf) # run the function again
    return names

# Q4
"""
    The solution only includes the part of arranging the dictionaries, and missing the part of writing to database
"""
words_file = open("a.txt") # open a.txt in read mode
output = {}
lines = words_file.readlines()
for line in lines:
    new_word = line.strip()
    for letter in new_word:
        if letter in output: # if letter exists in output as key
            output[letter] += 1
        else:
            output[letter] = 1
re_output = {}
values = list(set(output.values())) #

for number in values: # 38 2 3 38
    for letter in output: # {'a':38,'b':38}
        if output[letter] == number: # output['a'] = 38, number = 38
            if number not in re_output:
                re_output[number] = [letter]
            else:
                re_output[number].append(letter)

words_file.close()


# Q5

def sumAll(filename):
    sum_value=0
    open_file = open(filename)
    for integer in open_file:
        sum_value += int(integer)
    open_file.close()
    return sum_value

# Q6

def Q_6(filename_1,filename_2):
    open_file_1 = open(filename_1)
    lines = open_file_1.readlines()
    open_file_1.close()

    lines[-1] = lines[-1]+"\n" # adding \n to the last line

    lines = lines[-1::-1] # reverse the elements

    open_file_2 = open(filename_2,'w')
    for item in lines:
        open_file_2.write(item)
    open_file_2.close()
    open_file_1.close()


# Q7
def Q_7(file_1,file_2):
    open_file_1 = open(file_1)
    open_file_2 = open(file_2,'w')
    lines = open_file_1.readlines()
    counter = 1
    for line in lines:
        formatted_int = "%.4d" %counter
        open_file_2.write('{number} {Line}'.format(number=formatted_int,Line = line))
        counter += 1
    open_file_2.close()
    open_file_1.close()

# Q8
def Q_8(file_1,file_2):
    open_file_1 = open(file_1)
    open_file_2 = open(file_2,'w')
    lines = open_file_1.readlines()
    for line in lines:
        words_list = line.split() # By default its ' '
        txt_only = ' '.join(words_list[1:])
        open_file_2.write(txt_only)
    open_file_2.close()
    open_file_1.close()



# Q9

import os
def Q_9(dirc_path):
    files_in_direc = os.listdir(dirc_path)
    files_in_direc.append("file_doesnt_exits.txt")

    only_txt = []
    # appending only the txt files
    for file in files_in_direc:
        if file.endswith('.txt'):
            only_txt.append(file)
    only_txt.append("Faked.txt") # appending the file name
    for txt_file in only_txt:
        try:
            file_path = os.path.join(dirc_path,txt_file)
            open_file = open(file_path)
        except IOError:
            print "No Such file "+ txt_file
            continue
        open_file.close()


# Q10
def readfile(file_name):
    if file_name.endswith('.txt'):
        fileh= open(file_name)
        return fileh.readlines()
    else:
        raise ValueError('File name must end with .txt')

def main():
    try:
        for line in readfile('words.txt'):
            print line.lower()
    except ValueError as E:
        print "Wrong file ",E


# Q 11
def exercise1():
    for i in range(3):
        try:
            x = int(raw_input("Enter a number: "))
            y = int(raw_input("Enter a second number: "))
            print x,'/','y','=', x/y
        except ZeroDivisionError:
            print "Cannot divide by zero!"
        except ValueError:
            print "The input given is not a number."
        except:
            print "An unexpected error happened"

def exercise2(a_list):
    sum_of_pairs=[]
    for i in range(len(a_list)):
        try:
            sum_of_pairs.append(a_list[i]+a_list[i+1])
        except IndexError as e:
            print "IndexError: ",e
        except TypeError:
            print "The type of the list elements is not the same"
    print sum_of_pairs

def exercise3(file_name):
    try:
        fileh = open(file_name,'r')
        for line in fileh:
            print line.lower()
        fileh.close()
    except (NameError,IOError):
        print "The file with the name: ",file_name," was not found"



# Q12

import anydbm
import random
def Q_12(filename):
    db = anydbm.open('new.db','c')
    file_open = open(filename)
    for line in file_open:
        db[str(random.randrange(0,10))] = line
    db.close()





# Q13
import anydbm
import pickle
db = anydbm.open("stdname_score.db","c")
def get_grades():
    grade_name = {}
    data = open("grades.txt","r")
    for line in data:
        separated = line.rstrip("\n").split(" ")
        grade_name[separated[0]]=separated[1]
    return grade_name
def insert_to_db(grade_dicti):
    for student in grade_dicti:
        grade = grade_dicti[student]
        grade = pickle.dumps(grade)
        if grade in db:
            list_of_names = db[grade]
            list_of_names_loaded = pickle.loads(list_of_names)
            list_of_names_loaded.append(student)
            list_of_names = pickle.dumps(list_of_names_loaded)
            db[grade] = list_of_names
        else:
            list_of_names = pickle.dumps([student])
            db[grade] = list_of_names

def Q_13():
    grade_student=get_grades()
    insert_to_db(grade_student)
    for grade_std in db:
        grade = pickle.loads(grade_std)
        students = pickle.loads(db[grade_std])
        print grade, students
    db.close()






