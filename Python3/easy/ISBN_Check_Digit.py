import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def isbn13(value):
    arr = list(map(int, str(value)))
    check = arr[-1]
    count = 0
    weight = [1, 3]
    checkvalue = 0
    for b in arr[0:-1]:
        if count % 2:
            checkvalue += (b * weight[1])
        else:
            checkvalue += (b * weight[0])
        count += 1
    if (check == (10 - (checkvalue % 10))) or (checkvalue % 10 == 0):
        return True
    else:
        return False


def isbn10(value):
    arr = list(map(str, str(value)))
    check = arr[-1]
    weight = 10
    checkvalue = 0
    for i in range(0, 9):
        checkvalue += (int(arr[i]) * weight)
        weight -= 1
    if check.isdigit():
        if (int(check) == (11 - (checkvalue % 11))) or (checkvalue % 11 == 0):
            return True
        else:
            return False
    else:
        if 11 - checkvalue % 11 == 10 and check == "X":
            return True
        else:
            return False


n = int(input())
invalid = []
for i in range(n):
    isbn = input()
    lg = len(isbn)
    if lg == 10:
        if not isbn[0:-1].isdigit():
            invalid.append(isbn)
        elif not isbn10(isbn):
            invalid.append(isbn)
    elif lg == 13:
        if not isbn.isdigit():
            invalid.append(isbn)
        elif not isbn13(isbn):
            invalid.append(isbn)
    else:
        invalid.append(isbn)

print(str(len(invalid)) + " invalid:")
for inv in invalid:
    print(inv)

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
