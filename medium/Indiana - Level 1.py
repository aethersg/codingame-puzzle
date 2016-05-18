import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: number of columns.
# h: number of rows.

w, h = [int(i) for i in raw_input().split()]
rooms = []
for i in xrange(h):
    line = raw_input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    rooms.append([int(i) for i in line.split()])
ex = int(raw_input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

# game loop
while True:
    xi, yi, pos = raw_input().split()
    xi = int(xi)
    yi = int(yi)
    print >> sys.stderr, "h: %s" % h
    print >> sys.stderr, "w : %s" % w
    print >> sys.stderr, "pos: %s" % pos
    print >> sys.stderr, "xi : %s" % xi
    print >> sys.stderr, "yi : %s" % yi
    print >> sys.stderr, "line : %s" % line
    print >> sys.stderr, "rooms %s" % rooms[yi][xi]
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # One line containing the X Y coordinates of the room in which you believe Indy will be on the next turn.
    if rooms[yi][xi] in (1, 3, 7, 8, 9, 12, 13):
        yi += 1
    elif rooms[yi][xi] in (2, 6):
        if pos == "LEFT":
            xi += 1
        else:
            xi -= 1
    elif rooms[yi][xi] == 4:
        if pos == "TOP":
            xi -= 1
        else:
            yi += 1
    elif rooms[yi][xi] == 5:
        if pos == "TOP":
            xi += 1
        else:
            yi += 1
    elif rooms[yi][xi] == 10:
        xi -= 1
    elif rooms[yi][xi] == 11:
        xi += 1

    print "%s %s" % (xi, yi)
