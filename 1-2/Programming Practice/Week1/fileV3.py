file = open("data.txt", "w+")
file.write("00,01,02\n")
file.write("10,11,12\n")

# set the file iterator back to the beginning of the file:
file.seek(0)

for line in file:
	for token in line.split(",") :
		# get rid of the possible newlines in the token:
		if token[-1] == "\n":
			token = token[:-1]
		print "%s" % token,

file.close()
