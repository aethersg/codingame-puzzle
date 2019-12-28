# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: number of columns.
# h: number of rows.

w, h = [int(i) for i in input().split()]
rooms = []
for i in range(h):
    line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    rooms.append([int(i) for i in line.split()])
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

# game loop
while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)
    # Write an action using print

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

    print("%s %s" % (xi, yi))
