# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
grid = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    grid.append(list(line))

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

# Three coordinates: a node, its right neighbor, its bottom neighbor

for y in range(height):
    for x in range(width):
        if grid[y][x] == '0':
            print('%s %s' % (x, y), end=" ")

            xx = 1
            while ((x + xx) < width) and grid[y][x + xx] == '.':
                xx += 1
            if (x + xx) < width:
                print('%s %s' % ((x + xx), y), end=" ")
            else:
                print('-1 -1', end=" ")
            yy = 1
            while ((y + yy) < height) and grid[y + yy][x] == '.':
                yy += 1
            if (y + yy) < height:
                print('%s %s' % (x, (y + yy)))
            else:
                print('-1 -1')
