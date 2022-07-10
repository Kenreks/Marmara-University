fin = open("data.txt", "w+")
fin.write("af,af\n")
fin.write("selam\n")

fin.seek(0)

for line in fin:
    for token in line.split(","):
        if token[-1] == "\n":
            token = token[:-1]
        print token,
fin.close()
