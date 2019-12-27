import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r_1 = int(input())
r_2 = int(input())


# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
def checkvalue(value):
    temp = map(int, str(value))
    return value + sum(temp)


while (r_1 != r_2):
    if r_1 > r_2:
        r_2 = checkvalue(r_2)
    else:
        r_1 = checkvalue(r_1)
print(r_1)