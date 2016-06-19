import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# r: number of rows.
# c: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
r, c, a = [int(i) for i in raw_input().split()]

print >> sys.stderr, "r : %s" % r
print >> sys.stderr, "c : %s" % c
print >> sys.stderr, "a : %s" % a
d = {
    "R": "RIGHT",
    "L": "LEFT",
    "U": "UP",
    "D": "DOWN"
}
# game loop
while True:
    # kr: row where Kirk is located.
    # kc: column where Kirk is located.
    kr, kc = [int(i) for i in raw_input().split()]
    print >> sys.stderr, "kr :%s Kc : %s " % (kr, kc)
    for i in xrange(r):
        row = raw_input()  # C of the characters in '#.TC?' (i.e. one line of the ASCII maze).
        print >> sys.stderr,"%s" % row
    print d.get("R")
