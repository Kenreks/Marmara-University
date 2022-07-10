file = open("data.txt", "w+")
file.write("00,01,02\n")
file.write("10,11,12\n")

# set the file iterator back to the beginning of the file:
file.seek(0)

for line in file:
	print line,

file.close()
