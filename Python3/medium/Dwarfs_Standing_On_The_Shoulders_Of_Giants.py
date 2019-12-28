# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Node(object):
    def __init__(self, id):
        self.id, self.depth, self.affected_ppl = id, 1, []

    def affected(self, n):
        self.affected_ppl.append(n)

    def update(self):
        for n in self.affected_ppl:
            if (n.depth < self.depth + 1):
                n.depth = self.depth + 1
                n.update()


nodes = {}
n = int(input())  # the number of relationships of influence
for i in range(n):
    # x: a relationship of influence between two people (x influences y)
    x, y = [int(j) for j in input().split()]
    if x not in nodes:
        nodes[x] = Node(x)
    if y not in nodes:
        nodes[y] = Node(y)
    nx, ny = nodes[x], nodes[y]
    nx.affected(ny)
    nx.update()

max_depth = 0
for j in nodes.values():
    max_depth = max(j.depth, max_depth)
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."


# The number of people involved in the longest succession of influences
print(max_depth)
