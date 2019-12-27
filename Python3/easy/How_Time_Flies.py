import sys
import math
from datetime import date

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

begin = input()
end = input()
# create array day.month.year
begin_arr = list(map(int, begin.split(".")))
end_arr = list(map(int, end.split(".")))

ds = date(begin_arr[2], begin_arr[1], begin_arr[0])
de = date(end_arr[2], end_arr[1], end_arr[0])

change = de - ds
days = change.days

# given each year 365.25 calculating including leap years
years = int(days / 365.25)

# get number of months left
leftDays = (days - int(365.25 * (years)))
if leftDays >= 31:
    months = int(leftDays / 30)
else:
    months = 0

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

response = ""
if years != 0:
    if years == 1:
        response += str(years) + " year, "
    else:
        response += str(years) + " years, "
if months != 0:
    if months == 1:
        response += str(months) + " month, "
    elif months ==12 and years ==0:
        years +=1
        months=0
        response += str(years) + " year, "
    else:
        response += str(months) + " months, "
response += "total " + str(change.days) + " days"

print(response)
