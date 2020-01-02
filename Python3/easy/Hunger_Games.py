import sys
import math

player_name = []
for i in range(int(input())):
    player_name.append(input())
player_name = sorted(player_name)
m = {}
for i in range(int(input())):
    info = input()
    # print(info,file=sys.stderr)
    # split the first for the name , ignore the killed word and the peoper who was killed
    killed, _, dead = info.split(" ", 2)
    # convert dead to a proper array so we can do checks if we need.
    dead = sorted(dead.split(', '))
    if m.get(killed) is None:
        m[killed] = dead
    else:
        arr = m[killed]
        for x in dead:
            arr.append(x)
        m[killed] = sorted(arr)
# print(player_name, file=sys.stderr)
for i in range(len(player_name)):
    name = player_name[i]
    killed = ["None"]
    killer = 'None'
    if name in m:
        killed = m[name]
    for k, v in m.items():
        if name in [x for x in v]:
            killer = k
    print("Name: %s" % name)
    print("Killed: %s" % ", ".join(killed))
    if killer == 'None' and i + 1 < len(player_name):
        print("Killer: %s" % 'Winner')
        print()
    elif killer != 'None' and i + 1 < len(player_name):
        print("Killer: %s" % killer)
        print()
    elif killer == 'None' and i + 1 == len(player_name):
        print("Killer: %s" % 'Winner')
    else:
        print("Killer: %s" % killer)
