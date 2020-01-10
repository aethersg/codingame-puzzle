l = int(input())
n = int(input())


def mergre_overlap(arr):
    sorted_arr = sorted(arr)
    merged = []
    for value_range in sorted_arr:
        if not merged:
            merged.append(value_range)
        else:
            pervious_value_range = merged.pop()
            if pervious_value_range[1] >= value_range[0]:
                new_value_range = (pervious_value_range[0], max(pervious_value_range[1], value_range[1]))
                merged.append(new_value_range)
            else:
                merged.append(pervious_value_range)
                merged.append(value_range)
    return merged


def non_painted(arr, length_fence):
    all_painted = (0, length_fence)
    if len(arr) == 1 and arr[0] == all_painted:
        yield 'All painted'
    if len(arr) == 1 and arr[0][0] != 0:
        yield '0 %s' % arr[0][0]
    if len(arr) == 1 and arr[0][1] != length_fence:
        yield '%s %s' % (arr[0][1], length_fence)
    if len(arr) > 1:
        for i in range(len(arr)):
            if i == len(arr) - 1 and arr[i][1] != length_fence:
                yield '%s %s' % (arr[i][1], length_fence)
            elif arr[i][0] != 0 and i == 0:
                yield '0 %s' % arr[0][0]
                yield '%s %s' % (arr[0][1], arr[1][0])
            elif arr[i][1] != length_fence and i == 0:
                yield '%s %s' % (arr[0][1], arr[1][0])
            elif arr[i][1] != length_fence and i > 0 and i < len(arr) - 1:
                yield '%s %s' % (arr[i][1], arr[i + 1][0])


painted = []
for i in range(n):
    st, ed = [int(j) for j in input().split()]
    painted.append((st, ed))
for v in non_painted(mergre_overlap(painted), l):
    print(v)
