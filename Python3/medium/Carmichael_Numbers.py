import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())


# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
def gcd(a, b):
    if a < b:
        return int(gcd(b, a))
    if a % b == 0:
        return b
    return int(gcd(b, a % b))


def checkprime(p):
    flag = True
    for i in range(2, p):
        if int(p % i) == 0:
            flag = False
            break
    return flag


def icm(n):
    if checkprime(n):
        return 0

    b = 2
    while b < n:

        # If "b" is relatively prime to n
        if int(gcd(b, n)) == 1:

            # And pow(b, n-1)% n is not 1,
            # return false.
            if int(pow(b, n - 1, n)) != 1:
                return 0
        b = b + 1
    return 1


# print n
if icm(n):
    print("YES")
else:
    print("NO")
