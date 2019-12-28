import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
telephone_list = []


def make_tree(tl):
    root = dict()
    for t in tl:
        current_dict = root
        for no in t:
            current_dict = current_dict.setdefault(no, {})
    return root


def count_child(d):
    yield len(d)

    for v in d.values():
        if isinstance(v, dict):
            for x in count_child(v):
                yield x


def return_sum(d):
    return sum(count_child(d))


for i in range(n):
    telephone = input()
    telephone_list.append(telephone)
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

# The number of elements (referencing a number) stored in the structure.

tree = make_tree(telephone_list)
count = return_sum(tree)
print(count)
