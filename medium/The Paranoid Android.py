import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in raw_input().split()]

elevator_mapping = {exit_floor: exit_pos}
for i in xrange(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in raw_input().split()]
    # creating a map of the elevator this assumes that there is only one per floor
    elevator_mapping[elevator_floor] = elevator_pos


# this is to check which direction the clone should be moving to the elevator
def find_direction_to_lift(clone_position, elevator_position, clone_current_floor):
    if int(clone_position) - int(elevator_position.get(clone_current_floor)) > 0:
        return "LEFT"
    elif clone_position - int(elevator_position.get(clone_current_floor)) < 0:
        return "RIGHT"
    else:
        return "NONE"


# this is to check if it is the leading clone which can be a few however when they block their direction will change to NONE.
def leading_clone(clone_current_floor, clone_position, clone_direction):
    return clone_current_floor != -1 and clone_position != -1 and clone_direction != "NONE"


# game loop
while True:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = raw_input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)
    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."
    # action: WAIT or BLOCK
    if leading_clone(clone_floor, clone_pos, direction):
        if direction == find_direction_to_lift(clone_pos, elevator_mapping, clone_floor) or find_direction_to_lift(clone_pos, elevator_mapping, clone_floor) == "NONE":
            print "%s" % "WAIT"
        else:
            print "%s" % "BLOCK"
    else:
        print "%s" % "WAIT"
