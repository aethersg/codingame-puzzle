import sys
import math


def check_for_bond(row, col, formula):
    if row < 0 or row >= len(formula): return 0
    if col < 0 or col >= len(formula[row]): return 0
    return int(formula[row][col]) if formula[row][col] in '0123' else 0


def verify_bonds(row, col, compound):
    return check_for_bond(row, col - 2, compound) + check_for_bond(row, col + 4, compound) + check_for_bond(row - 1, col + 1, compound) + check_for_bond(row + 1, col + 1, compound)


n = int(input())
compound = []
answer = 'VALID'
for i in range(n):
    compound.append(input())
# print(compound,file=sys.stderr)

for row in range(len(compound)):
    for col in range(len(compound[row])):
        if compound[row][col] == 'C':
            no_carbons = int(compound[row][col + 2])
            bonds = verify_bonds(row, col, compound)
            if no_carbons + bonds != 4:
                answer = 'INVALID'

print(answer)
