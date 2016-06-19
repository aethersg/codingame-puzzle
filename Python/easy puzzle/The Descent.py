import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# game loop

while True:
    height_of_mountain = {}
    for i in xrange(8):
        mountain_h = int(raw_input())  # represents the height of one mountain, from 9 to 0.
        mountain_name = i
        height_of_mountain[i] = mountain_h
    sorted_height= sorted(height_of_mountain, key=height_of_mountain.get, reverse=True)
    object_to_shoot = sorted_height[0]
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # The number of the mountain to fire on.
    print object_to_shoot