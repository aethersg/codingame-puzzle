import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
values_for_stock = []
for i in input().split():
    v = int(i)
    values_for_stock.append(v)

max_loss = 0
current_max = 0
current_min = 0
for j in range(n):
    value = int(values_for_stock[j])
    if value > current_max:
        if current_max - current_min > max_loss:
            max_loss = current_max - current_min
        current_max = value
        current_min = value
    elif value < current_min:
        current_min = value

    if current_max - current_min > max_loss:
        max_loss = current_max - current_min

print("%d" % -max_loss)
