import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in raw_input().split()]
move_x = 0
move_y = 0
# game loop
while True:
    remaining_turns = int(raw_input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."


    # A single line providing the move to be made: N NE E SE S SW W or NW
    # Store Light position
    light_position = {
        'x': light_x,
        'y': light_y
    }
    thor_position = {
        'x': initial_tx + move_x,
        'y': initial_ty + move_y
    }

    distance_to_light = {
        'x': (light_position.get('x') - thor_position.get('x')),
        'y': (light_position.get('y') - thor_position.get('y'))
    }
    if distance_to_light.get('x') == 0 and distance_to_light.get('y') <= 0:
        print 'N'
        move_y -= 1
    if distance_to_light.get('x') == 0 and distance_to_light.get('y') >= 0:
        print 'S'
        move_y += 1
    if (distance_to_light.get('x') >= 0) and distance_to_light.get('y') == 0:
        print 'E'
        move_x += 1
    if distance_to_light.get('x') <= 0 and distance_to_light.get('y') == 0:
        print 'W'
        move_x -= 1
    if distance_to_light.get('x') <= 0 and (distance_to_light.get('y') > 0 and thor_position.get('y') < 17):
        print 'SW'
        move_y += 1
        move_x -= 1
    if distance_to_light.get('x') >= 0 and (distance_to_light.get('y') > 0 and thor_position.get('y') < 17):
        print 'SE'
        move_y += 1
        move_x += 1
