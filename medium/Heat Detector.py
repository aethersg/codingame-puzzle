import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in raw_input().split()]
n = int(raw_input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in raw_input().split()]

xMin,yMin = 0 , 0
xMax,yMax = w-1,h-1

# game loop
while True:
    bomb_dir = raw_input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # the location of the next window Batman should jump to.
    if "U" in bomb_dir:
        yMax = y0 - 1
    elif "D" in bomb_dir:
        yMin = y0 + 1

    if "L" in bomb_dir:
        xMax = x0 - 1
    elif "R" in bomb_dir:
        xMin = x0 + 1
    # set x0 y0 to new value
    x0 = (xMin + xMax)/2
    y0 = (yMin + yMax)/2
    print "%s %s" % (int(round(x0)),int(round(y0)))
    #print '0 0'
