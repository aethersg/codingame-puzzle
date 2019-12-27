import sys
import math

w, h = [int(i) for i in input().split()]
top = []
bottom = []
legs = []
for i in range(h):
    line = input()
    if i == 0:
        top.append(line)
        top = list(top[0].replace(' ', ''))
    elif i == h - 1:
        bottom.append(line)
        bottom = list(bottom[0].replace(' ', ''))
    else:
        line = line.replace('|--|', '|--  |')
        line = line.split('  ')
        legs.append(line)
result = []
for i in range(len(top)):
    pair = ''
    pair += top[i]
    end = i
    for j in range(len(legs)):
        if len(legs[j][end]) == 3:
            end = end + 1
        elif end != 0:
            if len(legs[j][end - 1]) == 3:
                end = end - 1
    pair += bottom[end]
    result.append(pair)
for r in result:
    print(r)
