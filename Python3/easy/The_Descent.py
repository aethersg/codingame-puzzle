import sys
import math

# The while loop represents the game.
# Each iteration represents a turn of the game
# where you are given inputs (the heights of the mountains)
# and where you have to print an output (the index of the mountain to fire on)
# The inputs you are given are automatically updated according to your last actions.


# game loop
while True:
    height_of_mountain = {}
    for i in range(8):
        mountain_h = int(input())  # represents the height of one mountain, from 9 to 0.
        mountain_name = i
        height_of_mountain[i] = mountain_h
    sorted_height = sorted(height_of_mountain, key=height_of_mountain.get, reverse=True)
    object_to_shoot = sorted_height[0]
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # The number of the mountain to fire on.
    print(object_to_shoot)
