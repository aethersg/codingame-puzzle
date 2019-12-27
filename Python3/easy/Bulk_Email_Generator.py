import re

n = int(input())
e = [''] * n
for i in range(n):
    e[i] = input()
a = '\n'.join(e)
c = -1


def choiceReplace(match):
    global c
    c += 1
    choices = match.group()[1:-1].split('|')
    return choices[c % len(choices)]


reply = re.sub('\([^)]*\)', choiceReplace, a)
print(reply)
