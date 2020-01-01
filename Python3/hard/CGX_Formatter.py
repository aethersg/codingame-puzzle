import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

cgxline = ''
n = int(input())
for i in range(n):
    cgxline += input()

quotes = 0
index = 0
newline = 0
current = 0
trimed = ''

for c in cgxline:
    if c == '\'':
        quotes = quotes ^ 1
    if quotes == 1 or (c != ' ' and c != '\t' and c != '\n'):
        trimed += c
cgxline = trimed

for i in range(len(cgxline)):
    c = cgxline[i]

    if newline == 1:
        print('\n', end="")
        print(' ' * index, end="")
        current = index
        newline = 0

    if c != '\'' and quotes == 1:
        print(c, end="")
        current += 1

    elif c == '(':
        if current != index:
            print('\n', end="")
            print(' ' * index, end="")
            current = index
        print("(", end="")
        current += 1
        index += 4
        if i != len(cgxline) - 1 and cgxline[i + 1] != ')':
            newline = 1

    elif c == ';':
        print(c, end="")
        current += 1
        newline = 1

    elif c == ')':
        print('\n', end="")
        index -= 4
        print(' ' * index, end="")
        current = index
        print(c, end="")
        current += 1
        if i != len(cgxline) - 1 and (cgxline[i + 1] != ';' and cgxline[i + 1] != ')'):
            nl = 1

    elif c == '\'':
        quotes ^= 1
        print(c, end="")
        current += 1

    else:
        print(c, end="")
        current += 1