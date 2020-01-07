import sys

width, height = [int(i) for i in input().split()]
print(width, height, file=sys.stderr)
game_maze = []
for i in range(height):
    game_maze.append(list(input()))
print(game_maze, file=sys.stderr)


def get_adjancent_count(h, w):
    count = 0
    if w != width - 1 and game_maze[h][w + 1] != '#':
        count += 1
    if w != 0 and game_maze[h][w - 1] != '#':
        count += 1
    if h != height - 1 and game_maze[h + 1][w] != '#':
        count += 1
    if h != 0 and game_maze[h - 1][w] != '#':
        count += 1
    return count


for i in range(height):
    for j in range(width):
        if game_maze[i][j] == '#':
            print(game_maze[i][j], end='')
        else:
            print(get_adjancent_count(i, j), end='')
    print()



