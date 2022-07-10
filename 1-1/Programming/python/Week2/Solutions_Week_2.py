
# ENGR 101 Introduction to Programming
# Practice Session Week 2

# Question 1
print "Question 1"

total_money = 10

# prices
notebook_price = 1.25
pen_price = .25
simit_price = .75

# amount bought
notebooks = 2
pens = 5

money_sub_pens_and_notebooks = total_money - (pens * pen_price + notebooks * notebook_price)
print "Money left after buying notebooks and pens: ", money_sub_pens_and_notebooks

# we use round becouse we want to buy only a whole simit, not a 1/3 of one simit!
print "Simits bought before being rounded: ",money_sub_pens_and_notebooks/simit_price
# We round 8.33333333333 which is assigned to the simits that can be bought
# becouse we can buy only a whole simit, not a fraction"

simits_bought = round(money_sub_pens_and_notebooks/simit_price)
print "Simits that can be bought: ", simits_bought

money_for_simits = simits_bought * simit_price
money_left = money_sub_pens_and_notebooks - money_for_simits

print "Money Left: ", money_left


print '.'*30
# Question 2
print "Question 2"

x = 5
y = 6.0
z = "."

"""
   x*5
   x/2
   x/2.0
   z*4
   z+y
   x*y
   x+y 
   z*y
   y*z
"""
print("1- " + str(x*5))
print("2- " + str(x/2))
print("3- " + str(x/2.0))
print("4- " + str(z*4))
# print("5- " + str(z+y))
print("5- " + " Error, Cannot concatenate str and float  ")
print("6- " + str(x*y))
print("7- " + str(x+y))
# print("8- " + str(z*y))
print("8- " + "Cannot multiply a sequence(string) by a float")
# print("9- " + str(y*z))
print("9- " + "Cannot multiply a sequence(string) by a float")




print('.'*30)
# Question 3
print("Question 3")

print("1- " + "We need quotation marks for the string")
print(type('Hello word'))
print("2- " + "variable 'a' is not defined")
a = 1
print(a+5)
print("3- " + "We need quotation marks around 5 to make it a string")
print("Hello" + '5')
print("4- " + "We need quotation marks around the word Hi to make it a string,"
              " because we can't add str type with int type. Or you make a variable called Hi")
print("+-----+" + 'Hi')

print("5- " + "Sehir(S being turkish she) University contains a Non-ASCII character")

print("6- " + "the uneven number of single quotes gives an error but when an escape sign is added the  is avoided")
print('Turkiye\'de') # renders correct 1 option, \ is used above as an escape character
print("Turkiye'de") # renders correct 2 option



print('.'*30)
# Question 4
print("Question 4")

print("1- " + str(10+20*30/10))
print("2- " + str((10+20)*30/10))
print("3- " + str(10+(20*30)/10))
print("4- " + str((10+20*30)/10))
print("5- " + str(10+20*(30/10)))


print('.'*30)
# Question 5
print("Question 5")
"""
  given numbers: 5,6,2,7,4    -> b =33
  given numbers: 3,4,5,9      -> b =170
  given numbers: 9,8,7,6,5,2  -> b = 81
"""

print("1- " + "(5 * 6 + (7-4)) = %d" %(5 * 6 + (7-4)))
print("2- " + "(9 * 3 * 5 + 3 * 9 + 5 + 3), (4*5*9 - (9/4)*5) = %d" %(4*5*9 - (9/4)*5))
print("3- " + "(8 * 9) + (7 + 2) = %d" %((8 * 9) + (7 + 2)))


print('.'*30)
# Question 6
print("Question 6")

print("1- " + str(5 + 7))
print("2- " + "Error!")
print("3- " + str(5 + 7.0))
print("4- " + ("5" + "7"))


print('.'*30)
# Question 7
print("Question 7")

print("1- " + str(5**2))
print("2- " + str(5*2))
print("3- " + str(5*2.0))
print("4- " + ("5" * 2))
# Additional Example
print("Moreover ->" + str(5**2.0))


print('.'*30)
# Question 8
print("Question 8")

# a)
#syntax error
# print 5:

# b)
#run time error
#dividing by zero
#print(5/0)

# c)

# Forgetting to divide by 100 when printing a percentage amount, so you do not get the answer you want.
# example
print(23.0/103)
# or for example doing floor division but expecting a float division like 5/2 but expecting 2.5

print('.'*30)
# Question 9
print("Question 9")

"""
a = 12
a = "15"
"a"=8
12 = "a"
a = b
a = "b"
"""
print "1- No Error"
print "2- No Error"
print "3- Error(a string can not be used for a variable name)"
print "4- Error(variable names must not begin with number)"
print "5- No Error (would give an error if a and b are not defined)"
print "6- No Error"
