import os
print(os.getcwd())


myfile = open('python.txt', 'w')

myfile.write('hello world!\n')
myfile.write('I like Python!\n')

myfile.close()

myfile2 = open('python.txt', 'a')
myfile2.write('Today is Monday!')

myfile2.close()

myfile2 = open('Python.txt', 'r')

for line in myfile2:
    print(line)

for line in open('python.txt', 'r'):
    print(line,)

with open('python.txt', 'r') as myfile:
    for line in myfile:
        print(line)

def walk(dir):
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            print(path)
        else:
            walk(path)
			
walk('C:\ENGR102')


def main():
    f= open("test.txt","w+")
    #f=open("test.txt","a+")
    for i in range(10):
         f.write("This is line " + str(i) + "\n")
    f.close()
    #Open the file back and read the contents
    #f=open("test.txt", "r")
    #if f.mode == 'r':
    #   contents =f.read()
    #   print (contents)
    #or, readlines reads the individual line into a list
    #fl =f.readlines()
    #for x in fl:
    #print(x)

