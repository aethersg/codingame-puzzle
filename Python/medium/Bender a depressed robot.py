import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

normal_order = ["SOUTH", "EAST", "NORTH", "WEST"]
reverse_order = ["WEST", "NORTH", "EAST", "SOUTH"]


class Bender(object):
    def __init__(self):
        self.current_x, self.current_y, self.current_direction, self.breaker, self.order, self.teleport = 0, 0, "SOUTH", False, normal_order, []

    def update_current(self, x, y):
        self.current_x = x
        self.current_y = y

    def return_current(self):
        return self.current_x, self.current_y

    def return_current_x(self):
        return self.current_x

    def return_current_y(self):
        return self.current_y

    def update_direction(self, direction):
        self.current_direction = direction

    def return_current_direction(self):
        return self.return_current_direction

    def update_breaker(self):
        self.breaker = not self.breaker

    def return_breaker(self):
        return self.breaker

    def update_order(self):
        if self.order == normal_order:
            self.order = reverse_order
        else:
            self.order = normal_order

    def update_teleport(self, teleport):
        self.teleport.append(teleport)


def next_move(bender_object):
    next_move_current_x = bender_object.current_x
    next_move_current_y = bender_object.current_y
    next_move_direction = bender_object.current_direction
    if next_move_direction == "SOUTH":
        next_move_current_y += 1
    elif next_move_direction == "NORTH":
        next_move_current_y -= 1
    elif next_move_direction == "EAST":
        next_move_current_x += 1
    elif next_move_direction == "WEST":
        next_move_current_x -= 1

    return next_move_current_x, next_move_current_y


def change_direction(area, bender_object):
    change_current_direction = 0
    if not bender_object.breaker:
        bender_object.update_direction(bender_object.order[change_current_direction])
    change_x, change_y = next_move(bender_object)
    while area[change_y][change_x] == "#" or ((bender_object.breaker == False) and area[change_y][change_x] == "X"):
        bender_object.update_direction(bender_object.order[change_current_direction])
        change_x, change_y = next_move(bender_object)
        change_current_direction += 1


def teleport(bender_object):
    if bender_object.current_x == bender_object.teleport[0][0] and bender_object.current_y == bender_object.teleport[0][1]:
        bender_object.update_current(bender_object.teleport[1][0], bender_object.teleport[1][1])
    else:
        bender_object.update_current(bender_object.teleport[0][0], bender_object.teleport[0][1])


def move(area, bender_object, move_array):
    move_current_direction = bender_object.current_direction
    move_array.append(move_current_direction)
    if move_current_direction == "SOUTH":
        bender_object.current_y += 1
    elif move_current_direction == "NORTH":
        bender_object.current_y -= 1
    elif move_current_direction == "EAST":
        bender_object.current_x += 1
    elif move_current_direction == "WEST":
        bender_object.current_x -= 1
    symbol = area[bender_object.current_y][bender_object.current_x]
    if symbol in ["X"]:
        if bender_object.breaker:
            area[bender_object.current_y][bender_object.current_x] = " "
    elif symbol in ["B"]:
        bender_object.update_breaker()
    elif symbol in ["I"]:
        bender_object.update_order()
    elif symbol in ["S"]:
        bender_object.update_direction("SOUTH")
    elif symbol in ["N"]:
        bender_object.update_direction("NORTH")
    elif symbol in ["W"]:
        bender_object.update_direction("WEST")
    elif symbol in ["E"]:
        bender_object.update_direction("EAST")
    elif symbol in ["T"]:
        teleport(bender_object)


l, c = [int(i) for i in raw_input().split()]
bender = Bender()
moves = []
map_route = []
for y in range(l):
    row = raw_input()
    second_layer = []
    for x, r in enumerate(row):
        second_layer.append(r)
        if r == "@":
            bender.update_current(x, y)
        if r == "T":
            bender.update_teleport([x, y])
    map_route.append(second_layer)

while (map_route[bender.return_current_y()][bender.return_current_x()] != "$") and (len(moves) < 200):
    current_x, current_y = next_move(bender)
    symbol = map_route[current_y][current_x]
    if symbol in [" ", "$", "E", "W", "S", "N", "B", "I", "T"]:
        move(map_route, bender, moves)
    elif symbol in ["#", "X"]:
        change_direction(map_route, bender)
        move(map_route, bender, moves)
if len(moves) == 200:
    print "LOOP"
else:
    for m in moves:
        print m
