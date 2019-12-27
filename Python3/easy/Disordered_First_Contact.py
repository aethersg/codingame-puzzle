import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def step_one(soa, temp):
    step1 = ""
    step1 += soa.pop(0)
    temp += step1
    return temp


def step_two(sta, temp, count):
    step2 = ""
    for i in range(2 + count):
        if len(sta) != 0:
            step2 += sta.pop(0)
        else:
            break
    temp = "".join(step2 + temp)
    return temp


def step_three(sta, temp, count):
    step3 = ""
    for i in range(3 + count):
        if len(sta) != 0:
            step3 += sta.pop(0)
        else:
            break
    temp = temp + step3
    return temp


def encode(string, time):
    temp = ""
    arr = []
    for s in string:
        arr.append(s)
    # step 1
    temp = step_one(arr, temp)
    while time != 0:
        time -= 1
        count = 0
        while (len(arr) != 0):
            # step 2
            temp = step_two(arr, temp, count)

            # step3
            temp = step_three(arr, temp, count)
            # increase count
            count += 2
        if time != 0:
            arr = []
            for t in temp:
                arr.append(t)
            temp = ""
            temp = step_one(arr, temp)

    print(temp)


def dcstep_two(sta, temp, value):
    step2 = ""
    for a in sta[0:value]:
        step2 += a
    del sta[0:value]
    temp = "".join(step2 + temp)
    return temp


def dcstep_three(sta, temp, value):
    step3 = ""
    for a in sta[(len(sta) - value):len(sta)]:
        step3 += a
    del sta[(len(sta) - value):len(sta)]
    temp = "".join(step3 + temp)
    return temp


def decode(string, time):
    arr = []
    temp = ""
    for s in string:
        arr.append(s)
    number_steps = 1
    # check how many steps are there to
    for i in range(len(arr)):
        check = sum(range(1, number_steps, 1))
        if check >= len(arr):
            # break loop as have needed about of steps
            break
        # if steps not enough increase
        number_steps += 1

    # check if perfect fit or not
    check = sum(range(1, number_steps, 1))
    # store the orginal value
    n_s = number_steps
    flag_init = True
    if check >= len(arr):
        while time != 0:
            time -= 1
            # need to find it is more by how much
            # note value of steps is one more for the loop so actually it is using one less.
            # convert to real number of steps
            number_steps = n_s
            number_steps -= 1
            # gotten real number of steps now to check which step is it at.
            # if it is even it is at the 2nd step however since it over the number we will
            # need to substrate the missing value from it. first and only once.
            while number_steps >= 1:
                if (number_steps % 2 == 0) and number_steps != 1:
                    if flag_init:
                        value = number_steps - (check - len(arr))
                        temp = dcstep_two(arr, temp, value)
                        flag_init = False
                    else:
                        temp = dcstep_two(arr, temp, number_steps)
                    number_steps -= 1

                elif (number_steps % 2 == 1) and number_steps != 1:
                    if flag_init:
                        value = number_steps - (check - len(arr))
                        temp = dcstep_three(arr, temp, value)
                        flag_init = False
                    else:
                        temp = dcstep_three(arr, temp, number_steps)
                    number_steps -= 1
                elif number_steps == 1:
                    temp = "".join(arr.pop() + temp)
                    number_steps -= 1

            if time != 0:
                arr = []
                for t in temp:
                    arr.append(t)
                temp = ""
                flag_init = True
    print(temp)


n = int(input())
message = input()

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

if n < 0:
    n = n * -1
    encode(message, n)
else:
    decode(message, n)


