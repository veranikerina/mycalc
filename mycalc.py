example = input ("Please type command with space: ")
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

        splited_line.pop(i-1)
        splited_line.pop(i-1)
        splited_line.pop(i-1)
        splited_line.insert(i-1,c)

for i, x in enumerate(splited_line):
    if x == '*' or x == '/':
        a = int(splited_line[i - 1])
        b = int(splited_line[i + 1])
        if (splited_line[i]) == '*':
            c = a * b
        else:
            c = a / b

        splited_line.pop(i - 1)
        splited_line.pop(i - 1)
        splited_line.pop(i - 1)
        splited_line.insert(i - 1, c)

c = int(splited_line[0])
for i, x in enumerate(splited_line):
    if x == '+' or x == '-':
        # a = int (splited_line[i-1])
        b = int(splited_line[i + 1])
        if (splited_line[i]) == '+':
            c = c + b
        else:
            c = c - b

print(str(c))
