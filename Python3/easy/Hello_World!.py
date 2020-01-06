import sys
import math

n = int(input())  # number of capitals
m = int(input())  # number of geolocations for which to find the closest capital


class Captial:
    def __init__(self, name, lat, lon, message):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.message = message
        self.distance = -1

    def return_lat(self):
        lat = self.lat
        facing = lat[0]
        degree = lat[1:3]
        mins = lat[3:5]
        sec = lat[5:7]
        return convert_std(facing, degree, mins, sec)

    def return_lon(self):
        lon = self.lon
        facing = lon[0]
        degree = lon[1:4]
        mins = lon[4:6]
        sec = lon[6:8]
        return convert_std(facing, degree, mins, sec)


def convert_std(facing, hh, mm, ss):
    if facing in ['N', 'E']:
        return float(hh) + float(mm) / 60.0 + float(ss) / 3600.0
    else:
        return -1 * (float(hh) + float(mm) / 60.0 + float(ss) / 3600.0)


captial_object = {}
for i in range(n):
    name, lat, lon = input().split()
    cap = Captial(name, lat, lon, '')
    captial_object[i] = cap
for i in range(n):
    captial_object.get(i).message = input()

for i in range(m):
    lat, lon = input().split()
    ncap = Captial('', lat, lon, '')
    # print(lat,lon,file=sys.stderr)
    for i in range(n):
        x1 = math.radians(captial_object.get(i).return_lat())
        y1 = math.radians(captial_object.get(i).return_lon())
        x2 = math.radians(ncap.return_lat())
        y2 = math.radians(ncap.return_lon())
        distance = int(round(6371 * math.acos(math.sin(x1) * math.sin(x2) + (math.cos(x1) * math.cos(x2) * math.cos(abs(y1 - y2))))))
        # print(distance,x1,y1,ncap.lat,ncap.lon,captial_object.get(i).name,file=sys.stderr)
        if ncap.distance == -1:
            # set the first one
            ncap.distance = distance
            ncap.message = captial_object.get(i).message
        elif ncap.distance == distance:
            ncap.message = ncap.message + ' ' + captial_object.get(i).message
        elif ncap.distance > distance:
            ncap.distance = distance
            ncap.message = captial_object.get(i).message
    print(ncap.message)
