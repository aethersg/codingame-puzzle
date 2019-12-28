import sys
import copy
import math
import time

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

no_of_ppl = int(input())
cost_of_gift = int(input())
budget = []
total_budget = 0
split_cost = 0
mini_budget = 1000000000
# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."
# simple check if they have enough money for the cost
t0 = time.time()
for i in range(no_of_ppl):
    b = int(input())
    budget.append(b)
    if b < mini_budget:
        mini_budget = b
    total_budget +=b

budget.sort()

if total_budget < cost_of_gift:
    print("IMPOSSIBLE")
else:

    for current_budget in budget:
        split_cost = int(cost_of_gift/no_of_ppl)
        if current_budget < split_cost:
            print(current_budget)
            cost_of_gift -= current_budget
        else:
            print(split_cost)
            cost_of_gift -=split_cost
        no_of_ppl -= 1
t1 = time.time()
