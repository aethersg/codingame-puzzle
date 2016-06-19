import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(raw_input())  # the number of points used to draw the surface of Mars.
surface_x, surface_y = [], []
for i in xrange(surface_n):
    # land_x: X coordinate of a surface point. (0 to 6999)
    # land_y: Y coordinate of a surface point. By linking all the points together in a sequential fashion, you form the surface of Mars.
    land_x, land_y = [int(j) for j in raw_input().split()]
    surface_x.append(land_x)
    surface_y.append(land_y)
# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in raw_input().split()]

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # 2 integers: rotate power. rotate is the desired rotation angle (should be 0 for level 1), power is the desired thrust power (0 to 4).
    to_ground = -1
    initial_to_ground = 0
    while (initial_to_ground < surface_n) and (to_ground == -1):
        if (surface_x[initial_to_ground] <= x) and (surface_x[initial_to_ground + 1] >= x):
            to_ground = surface_y[initial_to_ground]
        initial_to_ground += 1

    vdY = v_speed - 8.555
    vY = y - 36.665 + 5 * v_speed
    t = math.ceil((-40 - vdY) / 0.289)
    if vY + t * (vdY + 0.289 * (1 + t) / 2) > to_ground:
        print('0 0')
    else:
        print('0 4')
