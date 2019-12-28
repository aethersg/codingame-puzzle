import random

nodes, links, exits = map(int, input().split())
ADJ = [[0] * nodes for _ in range(nodes)]  # adjacence-matrix of graph
for _ in range(links):  # read links of graph
    N1, N2 = map(int, input().split())
    ADJ[N1][N2] = ADJ[N2][N1] = 1
exit_nodes = [int(input()) for _ in range(exits)]


def ngh(u):  # returns neighbors
    return [ix for ix in range(nodes) if ADJ[u][ix] and ix != u]


def cut(u, v):  # remove a link and print
    ADJ[u][v] = ADJ[v][u] = 0
    print(u, v)


while 1:
    SI = int(input())  # position of agent (node-id)
    forced_cuts = filter(lambda e: SI in ngh(e), exit_nodes)
    if forced_cuts:
        cut(forced_cuts[0], SI)
        continue
    # check if we can trap the AI!
    if len(ngh(SI)) <= 2:  # only two neighbors?
        c = min(ngh(SI), key=lambda x: -len(ngh(x)))
        cut(SI, c)
        continue
    # random cut at a gateway:
    xe, xn = random.choice([(ei, ei_n) for ei in exit_nodes for ei_n in ngh(ei)])
    cut(xe, xn)
