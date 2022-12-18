import sys
from collections import deque

def bfs(x,y,z):
    v = (x,y,z)
    s = {(x,y,z)} #seen
    q = deque([v]) #queue
    while q:
        p = q.popleft()
        x,y,z = p
        if((x==0 and y==0 and z==0)
        or x == size-1
        or y == size-1
        or z == size-1
        ):
            return True
        for side in sides:
            mx,my,mz = side
            mx=x+mx
            my=y+my
            mz=z+mz
            
            v = (mx,my,mz)
            
            if((mx,my,mz) in s):
                continue
            if(mx<0 or my<0 or mz<0 or mx>=size or my>=size or mz>=size):
                return True
            if(not m[mx][my][mz]):
                s.add(v)
                q.append(v)
    return False


p = [[int(k) for k in l.strip().split(",")] for l in sys.stdin]

m=[]
size = 30
for i in range(size):
    m.append([])
    for j in range(size):
        m[i].append([False]*size)
        

q=w=e=0
for pt in p:
    x,y,z = pt
    q = max(q,x)
    w = max(w,y)
    e = max(e,z)
    m[x][y][z]=True
print(q,w,e)
sides = [
    [0,0,-1], #up
    [0,0,1], #down
    [-1,0,0], #left
    [1,0,0],
    [0,1,0],
    [0,-1,0]
]
total = 0 
for pt in p:
    x,y,z = pt
    for side in sides:
        mx,my,mz = side
        mx=x+mx
        my=y+my
        mz=z+mz
        if(not m[mx][my][mz] and bfs(mx,my,mz)):
            total = total+1
print(total)