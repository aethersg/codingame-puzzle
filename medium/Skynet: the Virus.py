import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in raw_input().split()]
links = {}
exit = []
for i in xrange(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in raw_input().split()]
    if n1 not in links:
        links[n1] = []
    links[n1].append(n2)
    if n2 not in links:
        links[n2] = []
    links[n2].append(n1)
for i in xrange(e):
    ei = int(raw_input())  # the index of a gateway node
    exit.append(ei)

# game loop
while True:
    si = int(raw_input())  # The index of the node on which the Skynet agent is positioned this turn
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    serve_connection = ''
    for e in exit:
        if e in links[si]:
            serve_connection = '%s %s' % (si, e)
    if len(serve_connection) == 0:
        for e in exit:
            if len(links[e]):
                serve_connection = '%s %s' % (e, links[e].pop())
                break
            elif len(links[si]):
                serve_connection = '%s %s' % (si, links[si].pop())
                break
    print serve_connection
