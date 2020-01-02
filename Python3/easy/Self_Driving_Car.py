import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

no_of_road = int(input())
command = input()
command = command.split(';')
# get the starting point convert to integer and to also make it to an index.
starting_point = int(command.pop(0)) - 1
expanded_command = []
for c in command:
    for i in range(int(c[0:-1])):
        expanded_command.append(c[-1])
road = []
for i in range(no_of_road):
    no, road_pattern = input().split(';')
    for j in range(int(no)):
        road.append(road_pattern)
for i in range(len(road)):
    if expanded_command[i] == 'S':
        road[i] = road[i][:starting_point] + '#' + road[i][starting_point + 1:]
    elif expanded_command[i] == 'R':
        starting_point += 1
        road[i] = road[i][:starting_point] + '#' + road[i][starting_point + 1:]
    elif expanded_command[i] == 'L':
        starting_point -= 1
        road[i] = road[i][:starting_point] + '#' + road[i][starting_point + 1:]

for r in road:
    print(r)
