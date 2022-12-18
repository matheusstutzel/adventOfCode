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
    return x<0 or y<0 or z<0 or x>=size or y>=size or z>=size

def bfs(v):
    seen = {v}
    q = deque([v]) #queue
    while q:
        p = q.popleft()
        if(p == (0,0,0)):
            return True
        for side in sides(*p):            
            if(side in seen):
                continue
            if(outside(*side)):
                return True
            if(side not in points):
                seen.add(side)
                q.append(side)
    return False

points = [tuple([int(k) for k in l.strip().split(",")]) for l in sys.stdin]

size = 30
total = 0 
for pt in points:
    for side in sides(*pt):
        if(side not in points and bfs(side)):
            total = total+1
print(total)