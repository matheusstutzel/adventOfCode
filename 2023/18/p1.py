import sys
from collections import deque

def neighbors(mat, x,y, minx, maxx, miny, maxy):
    opt = [(-1,0),(0,-1),(0,1),(1,0)]
    for i,j in opt:
        a = i + x
        b = j + y
        if a<0 or a>=len(mat) or a<minx or a>=maxx:
            continue
        if b<0 or b>=len(mat[a])or b<miny or b>=maxy:
            continue
        yield (a,b)


def flood(mat, start, minx, maxx, miny, maxy):
    q = deque([start]) #queue
    round = 0
    s = set() #seen
    while q:    
        for _ in range(len(q)): #all in this depth
            
            p = q.popleft()
            if mat[p[0]][p[1]] != 0:
                continue
            mat[p[0]][p[1]] = 1

            for u in neighbors(mat, *p, minx, maxx, miny, maxy):
                if u not in s:
                    s.add(u)
                    q.append(u)

lines = [[x for x in l.strip().split()] for l in sys.stdin]

size = 1000
start = 500

mat = [[0 for col in range(size)] for row in range(size)]

x = start
y = start

minx =x
miny = y
maxx=x
maxy=y
for d,s,c in lines:
    #print(d, int(s), c)
    for i in range(int(s)):
        if d == 'R':
            y = y+1
        if d == 'L':
            y = y-1
        if d == 'U':
            x = x-1
        if d == 'D':
            x = x+1
        mat[x][y]=mat[x][y]-1
        minx = min(x, minx)
        miny = min(y, miny)
        maxx = max(x, maxx)
        maxy = max(y, maxy)
'''
print(minx, maxx, miny, maxy)
for i in range(minx-1, maxx+2):
    for j in range(miny-1, maxy+2):
        print( "." if mat[i][j] == 0 else "#", end=" ")
    print("")
'''
flood(mat, (minx-1,miny-1), minx-2, maxx+2, miny-2, maxy+2)

'''
for i in range(minx-1, maxx+2):
    for j in range(miny-1, maxy+2):
        print( "." if mat[i][j] <= 0 else "#", end=" ")
    print("")
'''
count = 0
for i in range(minx-1, maxx+2):
    for j in range(miny-1, maxy+2):
        if mat[i][j]<=0:
            count = count +1
print(count)