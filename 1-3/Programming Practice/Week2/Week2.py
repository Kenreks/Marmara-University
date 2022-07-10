
import dbm

list_db = dbm.open('list.db', 'c')

t1 = [1, 2, 3, 'istanbul']
print(t1)
import pickle

str_t1 = pickle.dumps(t1)

list_db['t1'] = str_t1

t2 = pickle.loads(list_db['t1'])
print(t2)

print(t1 == t2)
print(t1 is t2)

for elem in list_db:
    print(elem)



list_db.close()

def divider(num1, num2):
    try:
        result = num1/num2
    except ZeroDivisionError:
        print('I do not know how to divide by zero.')
    except ValueError:
        print('I cannot process values that are not numbers')
    except TypeError:
        print('I cannot process this input. Sorry!')
    except:
        print('I really did not expect this error')
        raise
    else:
        print('The result of division is', result)
    finally:
        print('I am done. This is executed always!')

divider(4, 'a')


while False:
    menu_number = input('Please select an option from the game menu: ')

    try:
        menu_number = int(menu_number)
    except:
        print('Sorry! This is an invalid option.')
        continue

    if int(menu_number) == 1:
        print('insert a new item')
    elif int(menu_number) == 0:
        print('Exiting! Bye!')
        break



try:
    f = open('engr102.practice')
except:
    print('I could not read the file! Therefore, I am terminating!')
    #exit()
else:
    for line in f:
        print(line)


import dbm
import os
import pickle

print(os.getcwd())

db = dbm.open('phonebook.db', 'c')

db['Ahmet'] = pickle.dumps(['123', '456'])

print(pickle.loads(db['Ahmet']))


for key in db.values():
    print(key)


db.close()
