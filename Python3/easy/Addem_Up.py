import sys
import math

n = int(input())
x=sorted(map(int, input().split()))
ans=0
while len(x)>1:
    temp=0
    for i in range(2):
        temp += x.pop(0)
    ans += temp
    x.append(temp)
    x=sorted(x)
print(ans)