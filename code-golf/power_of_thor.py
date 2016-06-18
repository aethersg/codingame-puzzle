import sys
import math

lx, ly, tx, ty = [int(i) for i in raw_input().split()]
m_x = 0
m_y = 0
while True:
    rt = int(raw_input())
    lp = {'x': lx,'y': ly}
    tp = {'x': tx + m_x,'y': ty + m_y}
    dl = {'x': (lp.get('x') - tp.get('x')),'y': (lp.get('y') - tp.get('y'))}
    if dl.get('x') == 0 and dl.get('y') <= 0:
        print 'N'
        m_y -= 1
    if dl.get('x') == 0 and dl.get('y') >= 0:
        print 'S'
        m_y += 1
    if (dl.get('x') >= 0) and dl.get('y') == 0:
        print 'E'
        m_x += 1
    if dl.get('x') <= 0 and dl.get('y') == 0:
        print 'W'
        m_x -= 1
    if dl.get('x') <= 0 and (dl.get('y') > 0 and tp.get('y') < 17):
        print 'SW'
        m_y += 1
        m_x -= 1
    if dl.get('x') >= 0 and (dl.get('y') > 0 and tp.get('y') < 17):
        print 'SE'
        m_y += 1
        m_x += 1
