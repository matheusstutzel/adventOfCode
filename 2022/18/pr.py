import sys
from collections import deque

def sides(x, y, z):
    yield (x + 1, y, z)
    yield (x - 1, y, z)
    yield (x, y + 1, z)
    yield (x, y - 1, z)
    yield (x, y, z + 1)
    yield (x, y, z - 1)

def outside(x,y,z):
    return x<-1 or y<-1 or z<-1 or x>size+1 or y>size+1 or z>size+1

def bfs(v):
    seen = {v}
    q = deque([v]) #queue
    while q:
        for side in sides(*q.popleft()):            
            if(side in points or side in seen or outside(*side)):
                continue
            seen.add(side)
            q.append(side)
    return seen

points = [tuple([int(k) for k in l.strip().split(",")]) for l in sys.stdin]
size = max( [max(l) for l in points])
outised = bfs((size-1,size-1,size-1)) #only for part2

p1 = p2 = 0 
for pt in points:
    for side in sides(*pt):
        if(side not in points):
            p1 = p1 +1
        if(side in outised):
            p2 = p2+1
print(p1,p2)