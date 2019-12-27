import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

temp_binary = ''
value_for_0 = '00 '
value_for_1 = '0 '
value_for_1_more = '0'

# if there is more then one letter in the input add binary values together
for c in message:
    # converting the value to binary
    binary = bin(ord(c))[2:]
    # if the binary is less the 8 add 0 in the front
    while len(binary) < 7:
        binary = '0' + binary
    temp_binary += binary

# placeholder to hold the last value
temp_value = ''
# placeholder to hold the count of same values
count = 0
final_value = ''
for value in temp_binary:

    # if the value is equal to the temp value increase count
    if value is temp_value:
        count += 1
    else:
        if temp_value is '0':
            final_value += value_for_0
        elif temp_value is '1':
            final_value += value_for_1
        for i in range(count):
            final_value += value_for_1_more
        if count > 0:
            final_value += ' '

        temp_value = value
        count = 1

if temp_value is '0':
    final_value += value_for_0
elif temp_value is '1':
    final_value += value_for_1
for j in range(count):
    final_value += value_for_1_more

print(final_value)
s