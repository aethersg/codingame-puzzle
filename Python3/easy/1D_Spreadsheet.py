import sys

n = int(input())
# list of instruction
sp = [input().split() for i in range(n)]
# list of answers
ans = ['_'] * n
print(sp, file=sys.stderr)


def ev(val):
    if val[0] == '$':
        return ei(int(val[1:]))
    else:
        return int(val)


def ei(index):
    # if the answer exist return it
    if ans[index] != '_':
        return ans[index]

    operation, arg_1, arg_2 = sp[index]
    if operation == 'VALUE':
        r = ev(arg_1)
    elif operation == 'ADD':
        r = ev(arg_1) + ev(arg_2)
    elif operation == 'SUB':
        r = ev(arg_1) - ev(arg_2)
    elif operation == 'MULT':
        r = ev(arg_1) * ev(arg_2)
    else:
        return False

    ans[index] = r
    return r


for i in range(n):
    print(ei(i))
