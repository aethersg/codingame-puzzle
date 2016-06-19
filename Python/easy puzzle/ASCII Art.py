import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(raw_input())
h = int(raw_input())
t = raw_input()

printoutput = []
for i in xrange(h):
    printoutput.append(raw_input())

output = []
text = t.lower()

for c in text:
    if c < 'a' or c > 'z':
        c = chr(ord('z') + 1)

    for i in xrange(h):
        if len(output) <= i:
            output.append('')
        ls = (ord(c) - ord('a')) * l
        output[i] += printoutput[i][ls:ls + l]
for output_string in output:
    print output_string

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
