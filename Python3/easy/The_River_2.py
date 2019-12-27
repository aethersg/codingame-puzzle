import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r_1 = int(input())


# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

def checkvalue(value):
    return value + sum(map(int, str(value)))


ans = True
temp = r_1
while ans:
    temp = temp - 1
    if temp == 0:
        ans = False
        print("NO")
    if r_1 == checkvalue(temp):
        ans = False
        print("YES")
