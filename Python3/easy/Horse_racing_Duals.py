import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
horses = []
for i in range(n):
    pi = int(input())
    horses.append(pi)
horses.sort()
min_diff = None
for i in range(0, n - 1):
    diff = int(abs(horses[i] - horses[i + 1]))
    if min_diff is None:
        min_diff = diff

    if diff < min_diff:
        min_diff = diff

print(min_diff)