def d3(x, t):
    if x % 3 != 0:
        return
    print(t + str(int(x / 3)))


def d2(x, t):
    z = int(min(t, x / 2))
    for i in range(0, z + 1):
        d3(x - (i * 2), str(t) + " " + str(i) + " ")


def d5(x):
    for i in range(0, int(x / 5) + 1):
        d2(x - (i * 5), i)


n = int(input())
d5(n)
