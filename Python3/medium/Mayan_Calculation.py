import sys
import copy

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

no_of_digits = 20  # this is given from the question.
l, h = [int(i) for i in input().split()]
numeral_array = []
s1_array = []
s2_array = []
for i in range(h):
    numeral = input()
    numeral_array.append(numeral)

s1 = int(input())
for i in range(s1):
    num_1line = input()
    s1_array.append(num_1line)

s2 = int(input())
for i in range(s2):
    num_2line = input()
    s2_array.append(num_2line)

operation = input()


# return the power with 20
def power(x):
    return pow(20, x)


def get_power(x):
    current_value = copy.copy(x)
    power_level = 0
    while current_value > 20:
        current_value /= 20
        power_level += 1
    return power_level


# sort out the mayan digits into a map
def convert_numeral_array_to_map(array, l, h, no_of_digits):
    n = 0
    map = {}

    while n < (no_of_digits * l):
        starting = 0 + n
        ending = l + n
        temp = []
        for i in range(h):
            line = ""
            for j in range(starting, ending):
                line += array[i][j]
            temp.append(line)
        if n == 0:
            number = n
        else:
            number = n / l
        map[number] = temp
        n += l

    return map


def convert_number_to_map(array, length, no_digits, height):
    array_digit = (no_digits / height)
    key_number = copy.copy(array_digit - 1)
    temp_no = 0
    temp_map = {}
    while temp_no < array_digit:
        temp_map[key_number] = array[temp_no * length:(temp_no * length) + (length)]
        temp_no += 1
        key_number -= 1
    return temp_map


def return_value(map1, map2):
    temp_value = []
    return_value = 0
    for key, value in map1.items():
        for key1, value1 in map2.items():
            if value == value1:
                temp_value.append(key1)
    for i in range(len(temp_value)):
        return_value += (temp_value[i] * power(len(temp_value)-i-1))
    return return_value


def return_answer(op, v1, v2):
    if op == "-":
        return v1 - v2
    elif op == "+":
        return v1 + v2
    elif op == "/":
        return v1 / v2
    elif op == "*":
        return v1 * v2


def mayan_form(value, map_of_mayan):
    temp_array = []
    no_power = get_power(value)
    temp_original = copy.copy(value)
    while no_power > 0:
        left_value = int(temp_original / power(no_power))
        temp_array += map_of_mayan.get(left_value)
        temp_original -= (left_value * power(no_power))
        no_power -= 1
    if temp_original < 20:
        temp_array += map_of_mayan.get(temp_original)
    return temp_array


mayan_digits = convert_numeral_array_to_map(numeral_array, l, h, no_of_digits)
s1_map = convert_number_to_map(s1_array, l, s1, h)
s2_map = convert_number_to_map(s2_array, l, s2, h)
s1_value = int(return_value(s1_map, mayan_digits))
s2_value = int(return_value(s2_map, mayan_digits))

# print("------ s1 value %s ------" % s1_value , file=sys.stderr)
# print("------ s2 value %s ------" % s2_value , file=sys.stderr)

answer = int(return_answer(operation, s1_value, s2_value))

# print("------ answer : %s ------" % answer, file=sys.stderr)

mayan_answer = mayan_form(answer, mayan_digits)
for m in mayan_answer:
    print(m)
