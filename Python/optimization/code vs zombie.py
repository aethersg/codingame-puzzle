import sys
import math


# Save humans, destroy zombies!

class Human(object):
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y


class Zombie(object):
    def __init__(self, id, x, y, nx, ny):
        self.id = id
        self.x = x
        self.y = y
        self.nx = nx
        self.ny = ny


def get_distance(x1, y1, x2, y2):
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


# game loop
while True:
    human_array = []
    zombie_array = []
    x, y = [int(i) for i in raw_input().split()]
    human_count = int(raw_input())
    for i in xrange(human_count):
        human_id, human_x, human_y = [int(j) for j in raw_input().split()]
        human_array.append(Human(human_id, human_x, human_y))

    zombie_count = int(raw_input())
    for i in xrange(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in raw_input().split()]
        zombie_array.append(Zombie(zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext))

    min_dist = sys.maxint
    for human in human_array:
        closing_zombie = None
        closest_zombie_dist = sys.maxint
        for zombie in zombie_array:
            zdist = get_distance(human.x, human.y, zombie.x, zombie.y)
            if closest_zombie_dist > zdist:
                closest_zombie_dist = zdist
                closing_zombie = zombie

        if closest_zombie_dist < min_dist:
            dist = get_distance(x, y, human.x, human.y)
            if closest_zombie_dist / 400.0 >= (max(dist - 2000, 0)) / 1000.0:
                location = (closing_zombie.x, closing_zombie.y)
                min_dist = closest_zombie_dist
    pzombie = True

    for z in zombie_array:
        for h in human_array:
            if get_distance(h.x, h.y, z.x, z.y) < get_distance(x, y, z.x, z.y):
                pzombie = False
                break
        if not pzombie:
            break

    print >> sys.stderr, "p %s" % pzombie
    if pzombie:
        center_x = 0
        center_y = 0
        for z in zombie_array:
            center_x += z.x
            center_y += z.y
        center_x /= len(zombie_array)
        center_y /= len(zombie_array)

        location = (center_x, center_y)
    print "%s %s" % location
