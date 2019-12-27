import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
mime_dict = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mime_dict[ext.lower()] = mt
for i in range(q):
    fname = input()  # One file name per line.
    # try to get file name extension
    filename_list = fname.split('.')
    if len(filename_list) != 1:
        # this is to return the last in the list as there might be some where there is a . in the file name
        print(mime_dict.get(filename_list[-1].lower(), 'UNKNOWN'))
    else:
        print('UNKNOWN')
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
