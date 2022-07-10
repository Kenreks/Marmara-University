file = open("data.txt", "w")
file.write("00,01,02\n")
file.write("10,11,12\n")

file = open("data.txt", "r")
for line in file:
	print line

file.close()
