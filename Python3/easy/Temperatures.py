import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input()
if n == 0:
    result = 0
    print(result)
else:
    min_temp = None
    new_temps = [int(x) for x in temps.split()]
    for temp in new_temps:
        if (min_temp is None) or (abs(temp) < abs(min_temp)) or (temp == -min_temp) and (temp > 0):
            min_temp = temp
    print(min_temp)
