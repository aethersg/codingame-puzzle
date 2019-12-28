import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
arr = []
for i in range(n):
    t = input()
    arr.append(t)
ans = sorted(arr)
print(ans[0])
