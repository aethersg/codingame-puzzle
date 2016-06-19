import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(raw_input())
values_for_stock = []
for i in raw_input().split():
    v = int(i)
    values_for_stock.append(v)

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
print >> sys.stderr, "values : %s " % list(values_for_stock)

max_loss = 0
current_max = 0
current_min = 0
for j in xrange(n):
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

print "%d" % -max_loss
