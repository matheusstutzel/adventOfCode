import sys
import math 
import heapq
from collections import deque
size = 71
limit = 1024
directions = [
    (0,1),(-1,0), (0,-1), (1,0)
]

def valid(c):
    return  c[0]>=0 and c[0]<size and c[1]>=0 and c[1]<size
def printa(p):
    for i in range(size):
        for j in range(size):
            if (i,j) in p:
                c = '#'
            else:
                c = '.'
            print(c, end='')
        print()

def bfs(current, target, points):
    q = deque([(current, 0, [])])
    values = []
    for i in range(size):
        values.append([])
        for j in range(size):
            values[i].append(math.inf)
    
    result = math.inf
    while q:
        if len(q)%1000==0:
            print(len(q))
        n,v,path = q.popleft()
        if n==target:
            result = min(result, v)
            continue
        if values[n[0]][n[1]]<v:
            continue
        values[n[0]][n[1]] = v
        visited = path + [n]
        for d in directions:
            u = (n[0]+d[0], n[1]+d[1])
            if u in visited:
                continue
            if not valid(u) or u in points:
                continue
            q.append((u, v+1, visited))
    return result

def calc(i,j,ti,tj):
    return abs(i-ti)+abs(j-tj)

def path(details, dst):
    p = []
    i = dst[0]
    j = dst[1]
    while not (details[i][j][0]==i and details[i][j][1]==j):
        p.append((i,j))
        i,j = details[i][j][0] , details[i][j][1]
    p.append((i,j))
    p.reverse()
    return p

def astar(src, dst, points):
    closed = [[False for _ in range(size)] for _ in range(size)]
    # parent i, parent j, (g+h), g (dist src to this), h (dist to dst using heuristic)
    details =[[(0,0,math.inf,math.inf, 0) for _ in range(size)] for _ in range(size)]

    i,j=src
    details[i][j]=(i,j,0,0,0)
    olist = []
    heapq.heappush(olist, (0.0, i,j))

    found = False

    while len(olist)>0:
        _,i,j = heapq.heappop(olist)
        closed[i][j]=True
        for d in directions:
            ni = i+d[0]
            nj = j+d[1]

            if not valid((ni,nj)) or (ni,nj) in points or closed[ni][nj]:
                continue
            g = details[i][j][3] +1
            if (ni,nj)==dst:
                details[ni][nj]=(i,j,g,g,0)
                return True,g, path(details, dst)
            else:
                h = calc(i,j,*dst)
                f = g+h
                cf=details[ni][nj][2]
                if cf==math.inf or cf>f:
                    heapq.heappush(olist, (f, ni,nj))
                    details[ni][nj]=(i,j,f,g,h) 
    return False,0,[]    


points = []
for l in sys.stdin:
    x,y = l.strip().split(",")
    points.append((int(y), int(x)))

#print(points)
#printa(points)
#print(bfs((0,0), (size-1,size-1), points))
p = []
f = False
g = 0
for i in range(limit, len(points)):
    c = points[:i+1]
    if points[i] in p or len(p)==0:
        f,g,p=astar((0,0), (size-1, size-1), c)
    if not f:
        print(points[i][1],",",points[i][0])
        break
    #print(i,"/",len(points)," ",g)

