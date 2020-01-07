from collections import deque

R = ">"
D = "v"
L = "<"
U = "^"

MR = "R"
ML = "L"


class Cell:
    def __init__(self, h, w, v):
        self.h = h
        self.w = w
        self.value = v
        self.stepped_on_count = 0

    def step_on(self):
        self.stepped_on_count += 1

    def total_steps(self):
        return self.stepped_on_count

    def current_position(self, dh=0, dw=0):
        return "{0} {1}".format(self.h + dh, self.w + dw)


class Pika:
    def __init__(self, start_pos, facing):
        self.current_pos = start_pos
        self.finish_line = start_pos
        self.facing = facing
        self.arrived = False
        self.maze_side = None
        self.first_move = True

    def run_maze(self):
        global maze_map
        while True:
            if self.move_next() == "STUCK":
                return
            if self.arrived:
                return

            maze_map[self.current_pos].step_on()
            self.first_move = False

    def move_next(self):
        if self.current_pos == self.finish_line and not self.first_move:
            self.arrived = True
            return

        if self.facing == R:
            if self.maze_side == MR:
                return self.move_right(0)
            elif self.maze_side == ML:
                return self.move_left(0)
        elif self.facing == D:
            if self.maze_side == MR:
                return self.move_right(1)
            elif self.maze_side == ML:
                return self.move_left(-1)
        elif self.facing == L:
            if self.maze_side == MR:
                return self.move_right(2)
            elif self.maze_side == ML:
                return self.move_left(-2)
        elif self.facing == U:
            if self.maze_side == MR:
                return self.move_right(3)
            elif self.maze_side == ML:
                return self.move_left(-3)

    def move_right(self, index_shift):
        sides = deque([D, R, U, L])
        sides.rotate(index_shift)
        for s in sides:
            c = self.check_for(s)
            if c:
                self.current_pos = c
                return
        return "STUCK"

    def move_left(self, index_shift):
        sides = deque([U, R, D, L])
        sides.rotate(index_shift)
        for s in sides:
            c = self.check_for(s)
            if c:
                self.current_pos = c
                return
        return "STUCK"

    def check_for(self, s):
        global maze_map
        if s == U:
            np = maze_map[self.current_pos].current_position(-1, 0)
            return self.check_value(s, np)
        elif s == D:
            np = maze_map[self.current_pos].current_position(1, 0)
            return self.check_value(s, np)
        elif s == R:
            np = maze_map[self.current_pos].current_position(0, 1)
            return self.check_value(s, np)
        elif s == L:
            np = maze_map[self.current_pos].current_position(0, -1)
            return self.check_value(s, np)

    def check_value(self, side, pos):
        global maze_map
        if pos in maze_map:
            if maze_map[pos].value == '#':
                return False
            else:
                self.facing = side
                return pos

    def set_maze_orientation(self, s):
        self.maze_side = s


maze_map = {}
cursor = None

width, height = [int(i) for i in input().split()]
for i in range(height):
    line = list(input())
    for j, value in enumerate(line):
        cell = Cell(i, j, value)
        if value in [R, D, L, U]:
            cursor = Pika(cell.current_position(0, 0), value)
        maze_map["{0} {1}".format(i, j)] = cell
side = input()
cursor.set_maze_orientation(side)
cursor.run_maze()
for i in range(height):
    for j in range(width):
        pos = "{0} {1}".format(i, j)
        if maze_map[pos].value == '#':
            print(maze_map[pos].value, end='')
        else:
            print(maze_map[pos].total_steps(), end='')
    print('')
