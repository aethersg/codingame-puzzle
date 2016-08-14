import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def nested(strings):
    res = strings.pop()
    while len(strings) > 0:
        new = strings.pop()
        for i in range(len(new) + 1):
            subLast = min(i + len(res), len(new))
            if new[i:subLast] == res[:subLast - i]:
                res = new[:subLast] + res[subLast - i:] + new[i + len(res):]
                break
    return res


def permutations(l):
    if len(l) == 0:
        return [[]]
    else:
        res = []
        for head in l:
            l2 = l[:]
            l2.remove(head)
            for tail in permutations(l2):
                res.append([head] + tail)
        return res


n = int(raw_input())
strings = []
for i in xrange(n):
    subseq = raw_input()
    strings.append(subseq)
    print >> sys.stderr, "seq : %s" % subseq
print >> sys.stderr, "the strings: %s" % strings
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

print(min(len(nested(p)) for p in permutations(strings)))
