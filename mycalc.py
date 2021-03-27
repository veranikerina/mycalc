example = input ("Please type command with space: ")
#9 - 2 ^ 3 - 1 + 8 / 4 * 3 ^ 2

import re
splited_line = re.split(' ', example)

def solve_with_one_brackets(splited_line):
    a = splited_line.index('(')
    b = splited_line.index(')')
    part = splited_line[a+1:b]
    value = solve_without_bracets(part)

    for i in range(b, a-1, -1):
        splited_line.pop(i)

    splited_line.insert(a, value)

    return solve_with_one_brackets(splited_line)

def solve_without_bracets(splited_line):
    for i, x in enumerate(splited_line):
        if x == '^':
            a = int(splited_line[i - 1])
            b = int(splited_line[i + 1])
            c = a ** b

            splited_line.pop(i - 1)
            splited_line.pop(i - 1)
            splited_line.pop(i - 1)
            splited_line.insert(i - 1, c)

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
    return c


