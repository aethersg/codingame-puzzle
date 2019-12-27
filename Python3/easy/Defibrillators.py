import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

lon = input()
lat = input()
n = int(input())
defib_list = []


def convert_to_float(value):
    return float(value.replace(',', '.'))


def return_distance(dlon, dlat, lon, lat):
    dlon = convert_to_float(dlon)
    dlat = convert_to_float(dlat)
    lon = convert_to_float(lon)
    lat = convert_to_float(lat)
    x = (dlon - lon) * math.cos((lat + dlat) / 2)
    y = (dlat - lat)
    d = math.sqrt(x * x + y * y) * 6371
    return d


for i in range(n):
    defib = input()
    split_defid = defib.split(';')
    defib_data = {
        'id': int(split_defid[0]),
        'name': split_defid[1],
        'add': split_defid[2],
        'no': split_defid[3],
        'lon': split_defid[4],
        'lat': split_defid[5]
    }
    defib_list.append(defib_data)
min_distance = None
nearest_defib = {}

if len(defib_list) > 1:
    for df in defib_list:
        d = return_distance(df['lon'], df['lat'], lon, lat)
        if min_distance is None:
            min_distance = d
            nearest_defib = df
        elif d < min_distance:
            min_distance = d
            nearest_defib = df
else:
    nearest_defib = defib_list[0]

print(nearest_defib['name'])
