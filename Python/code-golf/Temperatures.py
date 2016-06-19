import sys
import math
n = int(raw_input())  # the number of temperatures to analyse
t = raw_input()  # the n temperatures expressed as integers ranging from -273 to 5526
if n == 0:
    r = 0
    print r
else:
    mt = None
    nt = [int(x) for x in t.split()]
    for t in nt:
        if (mt is None) or (abs(t) < abs(mt)) or (t == -mt) and (t > 0):
            mt = t
    print mt
