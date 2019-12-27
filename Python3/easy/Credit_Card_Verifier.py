n = int(input())
for i in range(n):
    card = list(map(int, input().replace(' ', '')))
    card = card[::-1]
    even = []
    odd = []
    for a in range(len(card)):
        if a % 2:
            if card[a] * 2 >= 10:
                even.append((card[a] * 2) - 9)
            else:
                even.append(card[a] * 2)
        else:
            odd.append(card[a])
    if (sum(even) + sum(odd)) % 10 == 0:
        print('YES')
    else:
        print('NO')
