n = int(input())
l = int(input())
room = [input().split() for _ in range(n)]
candle = []


def get_neighbors(c, r, rs):
    if rs == 1:
        return

    if r > 0:
        yield c, r - 1
        if c > 0:
            yield c - 1, r - 1
        if c < rs - 1:
            yield c + 1, r - 1

    if r < rs - 1:
        yield c, r + 1
        if c > 0:
            yield c - 1, r + 1
        if c < rs - 1:
            yield c + 1, r + 1

    if c > 0:
        yield c - 1, r
    if c < rs - 1:
        yield c + 1, r


def fill_light(c, r, l, rm, rs):
    if l == 0: return
    if rm[c][r] in ('X', 'C'):
        rm[c][r] = l
    elif rm[c][r] >= l:
        return

    rm[c][r] = l

    for nc, nr in get_neighbors(c, r, rs):
        fill_light(nc, nr, l - 1, rm, rs)


for i in range(len(room)):
    for j in range(len(room[i])):
        if room[i][j] == 'C':
            candle.append((i, j))

for c, r in candle:
    fill_light(c, r, l, room, n)
ans = 0
for r in room:
    for v in r:
        if v == 'X':
            ans += 1
print(ans)