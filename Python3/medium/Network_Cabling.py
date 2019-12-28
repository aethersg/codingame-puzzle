# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
map_of_houses = []
for i in range(n):
    x, y = [int(j) for j in input().split()]
    map_of_houses.append([x, y])
# get the distance x needed for the main cable
# sort the map
map_of_houses.sort()
# get the first value
temp_value = map_of_houses[0]
min_x = temp_value[0]
temp_value = map_of_houses[-1]
max_x = temp_value[0]
distance_of_main_cable = int(abs(max_x - min_x))

# collect all the y values from sorted list
y_values = []
for value in map_of_houses:
    y_values.append(value[1])
# need to sort y_values again incase
y_values.sort()
# y value of where main cable should be
main_y = y_values[int(len(y_values) / 2)]

# add the value of cable from main cable to houses
for j in range(len(y_values)):
    if main_y <= y_values[j]:
        distance_of_main_cable += int(abs((y_values[j] - main_y)))
    else:
        distance_of_main_cable += int(abs((main_y - y_values[j])))

print("%d" % distance_of_main_cable)
