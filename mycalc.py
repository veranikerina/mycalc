example = input ("Please type command: ")
#9 - 2 ^ 3 - 1 + 8 / 4 * 3 ^ 2
example
import re
splited_line = re.split(' ', example)
splited_line
for i,x in enumerate(splited_line):
    if x == '^':
        a = int (splited_line[i-1]) 
        b = int (splited_line[i+1])
        c = a ** b
        print(a, b, c)

        splited_line.pop(i-1)
        splited_line.pop(i-1)
        splited_line.pop(i-1)
        splited_line.insert(i-1,c)
        print(splited_line)

for i,x in enumerate(splited_line):
    if x == '/':
        a = int (splited_line[i-1])
        b = int (splited_line[i+1])
        c = a / b
        print(a, b, c)

        splited_line.pop(i-1)
        splited_line.pop(i-1)
        splited_line.pop(i-1)
        splited_line.insert(i-1,c)
        print(splited_line)

for i,x in enumerate(splited_line):
    if x == '*':
        a = int (splited_line[i-1])
        b = int (splited_line[i+1])
        c = a * b
        print(a, b, c)

        splited_line.pop(i-1)
        splited_line.pop(i-1)
        splited_line.pop(i-1)
        splited_line.insert(i-1,c)
        print(splited_line)

for i,x in enumerate(splited_line):
    if x == '+':
        a = int (splited_line[i-1])
        b = int (splited_line[i+1])
        c = a + b
        print(a, b, c)

        splited_line.pop(i-1)
        splited_line.pop(i-1)
        splited_line.pop(i-1)
        splited_line.insert(i-1,c)
        print(splited_line)

for i,x in enumerate(splited_line):
    if x == '-':
        a = int (splited_line[i-1])
        b = int (splited_line[i+1])
        c = a - b
        print(a, b, c)

        splited_line.pop(i-1)
        splited_line.pop(i-1)
        splited_line.pop(i-1)
        splited_line.insert(i-1,c)
        print("Result " + str(c))