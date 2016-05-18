import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
map_of_nodes = {}
n = int(raw_input())  # the number of adjacency relations
for i in xrange(n):
    # xi: the ID of a person which is adjacent to yi
    # yi: the ID of a person which is adjacent to xi
    xi, yi = [int(j) for j in raw_input().split()]
    # map the neighbours to the node
    if xi in map_of_nodes:
        map_of_nodes[xi].append(yi)
    else:
        map_of_nodes[xi] = [yi]
    if yi in map_of_nodes:
        map_of_nodes[yi].append(xi)
    else:
        map_of_nodes[yi] = [xi]
steps = 0
branch = {}
# the number of branches for each node.
for no in map_of_nodes:
    branch[no] = len(map_of_nodes[no])

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
print >> sys.stderr, "no of nodes %s " % n
print >> sys.stderr, "nodes map %s " % map_of_nodes

while len(branch) > 2:
    # get the edge node.
    edge_nodes = [k for k, v in branch.items() if v == 1]
    print >> sys.stderr, "end_nodes %s " % list(edge_nodes)
    print >> sys.stderr, "branch %s " % branch
    # go through all branches
    for value in edge_nodes:
        print >> sys.stderr, "value %s " % value
        node = map_of_nodes[value]
        for x in node:
            if x in branch:
                # reduce the count of branches
                branch[x] -= 1
        # remove branch if it reaches 0
        del branch[value]
    steps += 1

if len(branch) == 2:
    steps += 1

print steps
