import sys
import math

l = int(input())
h = int(input())
t = input()

output = []

for i in range(h):
    output.append(input())

ans = []
text = t.lower()

for c in text:
    if c < 'a' or c > 'z':
        c = chr(ord('z') + 1)

    for i in range(h):
        if len(ans) <= i:
            ans.append('')
        ls = (ord(c) - ord('a')) * l
        ans[i] += output[i][ls:ls + l]

for output_string in ans:
    print(output_string)
