import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(raw_input())  # the number of cells on the X axis
height = int(raw_input())  # the number of cells on the Y axis
grid = []
for i in xrange(height):
    line = raw_input()  # width characters, each either 0 or .
    grid.append(list(line))

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

# Three coordinates: a node, its right neighbor, its bottom neighbor

for y in xrange(height):
    for x in xrange(width):
        if grid[y][x] == '0':
            print '%s %s' % (x, y),

            xx = 1
            while ((x + xx) < width) and grid[y][x + xx] == '.':
                xx += 1
            if (x + xx) < width:
                print '%s %s' % ((x + xx), y),
            else:
                print '-1 -1',
            yy = 1
            while ((y + yy) < height) and grid[y + yy][x] == '.':
                yy += 1
            if (y + yy) < height:
                print '%s %s' % (x, (y + yy))
            else:
                print '-1 -1'
