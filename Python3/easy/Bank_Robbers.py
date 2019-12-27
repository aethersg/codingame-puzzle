import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(input())
v = int(input())
arr = []
for i in range(v):
    c, n = [int(j) for j in input().split()]
    arr.append(10 ** n * 5 ** (c - n))

if r >= v:
    print(max(arr))
else:
    # get the smallest from the array list of how many robbers
    count = 0
    while len(arr) != 0:
        m = min(arr[0:r])
        count += m
        for i in range(r):
            if i < len(arr):
                arr[i] = arr[i] - m
        arr.remove(0)
    print(count)

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
