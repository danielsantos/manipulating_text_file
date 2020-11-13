file = open("test.txt", "a")

lines = list()
lines.append("One \n")
lines.append("Two \n")
lines.append("Three \n")
lines.append("Four \n")

file.writelines(lines)