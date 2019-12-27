import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

pw = 1+2*(n-1)
tw = 2*pw+1

print('.' + ' '*(2*(n-1)) + '*')
for i in range(1, n):
    sir = 1 + 2*i
    sbfp = (tw - sir) // 2
    print(' '*sbfp + '*'*sir)

for i in range(n):
    sir = 1 + 2*i
    sbfp = (pw - sir) // 2
    sbp = 2*sbfp + 1
    print(' '*sbfp + '*'*sir + ' '*sbp + '*'*sir)