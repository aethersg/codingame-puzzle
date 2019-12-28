import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

r = int(input())
l = int(input())


def lookandsay(number):
    num = consume_delimited_string(number)
    result = ""
    repeat = num[0]
    num = num[1:]
    times = 1
    for actual in num:
        if actual != repeat:
            result = check_result(result, times, repeat)
            times = 1
            repeat = actual
        else:
            times += 1
    result = check_result(result, times, repeat)

    return result


def consume_delimited_string(number):
    delimited_array = number.split(",")
    return delimited_array


def check_result(value, t, r):
    if value != "":
        value = value + "," + str(t) + "," + str(r)
    else:
        value = str(t) + "," + str(r)
    return value


num = str(r)

for i in range(l - 1):
    num = lookandsay(num)

print(num.replace(",", " "))
