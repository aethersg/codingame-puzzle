import sys
import math

left = '<'
right = '>'
inc = '+'
dec = '-'
spell = '.'
start = '['
stop = ']'

magicPhrase = raw_input()
unique_letter = set(magicPhrase)
print >> sys.stderr, "unique letter %s" % unique_letter

alp_len = ord('Z') - ord('A') + 1
zone_len = 30

zones = [' ' for x in range(zone_len)]
pos = 0

output = []


def calculate_distance(pos, i):
    return min(abs(pos - i), 30 - abs(pos - i))


def calculate_change(a, b):
    if a == ' ' and b == ' ':
        return 0
    if a == ' ':
        print >> sys.stderr, "value return a %s"  % min(abs(ord(b) - ord('A') - 1), abs(ord('Z') + 1 - ord(b)))
        return min(abs(ord(b) - ord('A') - 1), abs(ord('Z') + 1 - ord(b)))
    if b == ' ':
        print >> sys.stderr, "value return b %s" % min(abs(ord(a) - ord('A') - 1), abs(ord('Z') + 1 - ord(a)))
        return min(abs(ord(a) - ord('A') - 1), abs(ord('Z') + 1 - ord(a)))

    return min(abs(ord(a) - ord(b)), 30 - abs(ord(a) - ord(b)))


def move_to(new_zone):
    global pos, output
    if new_zone > pos:
        if new_zone - pos < pos + zone_len - new_zone:  # go right
            output.extend([right for x in range(new_zone - pos)])
        else:
            output.extend([left for x in range(pos + zone_len - new_zone)])
    elif new_zone < pos:
        if pos - new_zone < new_zone + zone_len - pos:  # go left
            output.extend([left for x in range(pos - new_zone)])
        else:
            output.extend([right for x in range(new_zone + zone_len - pos)])
    pos = new_zone


def change_letter(new_letter):
    current = zones[pos]
    nl, c = ord(new_letter), ord(current)
    if c == nl:
        return
    elif current == ' ':
        if nl - ord('A') + 1 < ord('Z') + 1 - nl:  # better to go up
            output.extend([inc for x in range(nl - ord('A') + 1)])
        else:
            output.extend([dec for x in range(ord('Z') + 1 - nl)])
    elif new_letter == ' ':
        if ord('Z') + 1 - c < c - ord('A') + 1:  # better to go up
            output.extend([inc for x in range(ord('Z') + 1 - c)])
        else:
            output.extend([dec for x in range(c - ord('A') + 1)])
    else:
        if (nl > c and nl - c < c - ord('A') + ord('Z') - nl + 1) or \
                (c - nl > nl - ord('A') + ord('Z') - c + 1):  # better to go up
            output.extend([inc for x in range(min(abs(nl - c), abs(c - ord('A') + ord('Z') - nl + 1)))])
        else:
            output.extend([dec for x in range(min(abs(nl - c), abs(nl - ord('A') + ord('Z') - c + 1)))])

    zones[pos] = new_letter


for letter in magicPhrase:
    best_move_zone = None
    best_result = 1000000
    for i in range(zone_len):
        d = calculate_distance(pos, i)
        change = calculate_change(zones[i], letter)
        if best_result > d + change:
            best_result = d + change
            best_move_zone = i

    move_to(best_move_zone)
    change_letter(letter)
    output.append(spell)

print("".join(output))
