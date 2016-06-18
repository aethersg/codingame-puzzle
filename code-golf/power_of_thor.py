lx, ly, tx, ty = [int(i) for i in raw_input().split()]
d = {(-1, 1): 'SW',(0, 1): 'S',(1, 1): 'SE',(-1, 0): 'W',(0, 0): None,(1, 0): 'E',(-1, -1): 'NW',(0, -1): 'N',(1, -1): 'NE'}
while tx != lx or ty != ly:
    rt = int(raw_input())
    dx, dy = map(lambda x: (x[0] > x[1]) - (x[0] < x[1]), ((lx, tx), (ly, ty)))
    tx += dx
    ty += dy
    print(d.get((dx, dy)))