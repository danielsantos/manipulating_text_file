file = open('test.txt', 'r')
content = file.readlines()
content.append('New Line')

file = open('test.txt', 'w')
file.writelines(content)

file.close()