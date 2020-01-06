import sys

w, h, count_x, count_y = [int(i) for i in input().split()]
all_x, all_y = [], []
all_x.append(w)
all_y.append(h)
for i in input().split():
    all_x.append(int(i))
for i in input().split():
    all_y.append(int(i))
all_x = sorted(all_x)
all_y = sorted(all_y)
print(w, h, file=sys.stderr)
print(all_x, file=sys.stderr)
print(all_y, file=sys.stderr)
all_subwidths, all_subheights = [], []


# this is to return all sub values from array
def return_combinations(subarray, arr):
    while len(arr) != 0:
        t = arr[-1]
        subarray.append(arr.pop(-1))
        for v in arr:
            subarray.append(t - v)
    return subarray


all_subwidths = return_combinations(all_subwidths, all_x)
all_subheights = return_combinations(all_subheights, all_y)
results = 0
print(all_subwidths, file=sys.stderr)
print(all_subheights, file=sys.stderr)
# check which array is longer or has more subvalues
if len(all_subheights) >= len(all_subwidths):
    x, y = all_subheights, all_subwidths
else:
    y, x = all_subheights, all_subwidths
for w in x:
    results += y.count(w)
print(results)
