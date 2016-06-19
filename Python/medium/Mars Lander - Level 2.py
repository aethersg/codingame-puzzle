import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(raw_input())  # the number of points used to draw the surface of Mars.
surface_x, surface_y = [], []
mars_gravity = 3.711
vertical_max_speed = 40
horizontal_max_speed = 20
margin_for_error_y = 20
margin_for_speed = 5
map_thrust = {
    0: 0,
    1: 1,
    2: 2,
    3: 3,
    4: 4
}


# to get the location to land.
# it will check where the land is flat
def move_to_location(pos_x, pos_y):
    perv_x = -1
    prev_y = -1
    for i in range(0, surface_n):
        if pos_y[i] == prev_y:
            # checking if the landing space is at least 1000
            if abs(prev_x - pos_x[i]) >= 1000:
                return [prev_x, prev_y, pos_x[i], pos_y[i]]
            else:
                prev_y = pos_y[i]
                prev_x = pos_x[i]
        else:
            prev_y = pos_y[i]
            prev_x = pos_x[i]


# this checks if the mars lander is in the landing site.
def ship_over_location(current_x, landing_site):
    return landing_site[0] < current_x < landing_site[2]


# this is to check if the mars lander is nearing the end.
def check_nearing_landing(current_y, landing_site):
    return current_y < landing_site[1] + margin_for_error_y


# check if speed is safe
def check_if_speed_safe(current_speed_x, current_speed_y):
    return abs(current_speed_x) <= horizontal_max_speed - margin_for_speed and abs(current_speed_y) <= vertical_max_speed - margin_for_speed


# check if mars lander is moving in wrong direction
def check_direction(current_x, current_hor_speed, landing_site):
    return (current_x < landing_site[0] and current_hor_speed < 0) or (landing_site[2] < current_x and current_hor_speed > 0)


# check if going horizontal too fast
def check_horizontal_speed(current_hor_speed, type):
    if type == "FAST":
        return abs(current_hor_speed) > 4 * horizontal_max_speed
    elif type == "SLOW":
        return abs(current_hor_speed) < 2 * horizontal_max_speed


# return angle to move to target
def angle_to_target(current_x, landing_site):
    angle = int(math.degrees(math.acos(mars_gravity / 4.0)))
    if current_x < landing_site[0]:
        return -angle
    elif landing_site[2] < current_x:
        return angle
    else:
        return 0


# returns power to hover
def hover(current_speed_y):
    if current_speed_y >= 0:
        return 3
    else:
        return 4


# return best angle to slow down
def angle_to_slow_down(current_speed_x, current_speed_y):
    speed = math.sqrt((current_speed_x * current_speed_x) + (current_speed_y * current_speed_y))
    return int(math.degrees(math.asin(current_speed_x / speed)))


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
    print >> sys.stderr, "surface_n : %s" % surface_n
    print >> sys.stderr, "x : %s" % x
    print >> sys.stderr, "y : %s" % y
    print >> sys.stderr, "h_speed : %s" % h_speed
    print >> sys.stderr, "v_speed : %s" % v_speed
    print >> sys.stderr, "fuel : %s" % fuel
    print >> sys.stderr, "rotate : %s" % rotate
    print >> sys.stderr, "power : %s" % power
    print >> sys.stderr, "surface_x : %s" % surface_x
    print >> sys.stderr, "surface_y : %s" % surface_y
    print >> sys.stderr, move_to_location(surface_x, surface_y)
    print >> sys.stderr, ship_over_location(x, move_to_location(surface_x, surface_y))
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    # rotate power. rotate is the desired rotation angle. power is the desired thrust power.

    # if ship not over location
    correct_site = move_to_location(surface_x, surface_y)
    if not ship_over_location(x, correct_site):
        if (check_direction(x, h_speed, correct_site)) or (check_horizontal_speed(h_speed, "FAST")):
            print "%s %s" % (angle_to_slow_down(h_speed, v_speed), map_thrust.get(4))
        elif check_horizontal_speed(h_speed, "SLOW"):
            print "%s %s" % (angle_to_target(x, correct_site), map_thrust.get(4))
        else:
            print "%s %s" % (map_thrust.get(0), hover(v_speed))
    else:
        if check_nearing_landing(y, correct_site):
            print "0 3"
        elif check_if_speed_safe(h_speed, v_speed):
            print "0 2"
        else:
            print "%s 4" % angle_to_slow_down(h_speed, v_speed)
