import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())


# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
def gcd(a, b):
    if (a < b):
        return int(gcd(b, a))
    if (a % b == 0):
        return b
    return int(gcd(b, a % b))


def power(x, y, mod):
    if (y == 0):
        return 1
    temp = power(x, int(y/2), mod) % mod
    temp = (temp * temp) % mod
    if (y % 2 == 1):
        temp = (temp * x) % mod
    return temp


def checkprime(p):
    flag = True
    for i in range(2, p):
        if (p % i) == 0:
            flag = False
            break
    return flag


def icm(n):
    if checkprime(n):
        return 0

    b = 2
    while b < n:

        # If "b" is relatively prime to n
        if (int(gcd(b, n)) == 1):

            # And pow(b, n-1)% n is not 1,
            # return false.
            if (int(power(b, n - 1, n)) != 1):
                return 0
        b = b + 1
    return 1


# print n
if icm(n):
    print("YES")
else:
    print("NO")
