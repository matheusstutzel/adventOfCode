import sys
import math 
import heapq
from collections import deque
directions = [
    (0,1),(-1,0), (0,-1), (1,0)
]

def valid(x,y,mat):
    return  x>=0 and x<len(mat) and y>=0 and y<len(mat[x]) and mat[x][y]!='#'

def walk(start, end, mat, dist):
    p=end
    x=end
    c=0
    while start!=x:
        dist[x]=c
        c+=1
        for d in directions:
            u = (x[0]+d[0], x[1]+d[1])
            if u!=p and valid(*u, mat):
                p=x
                x=u
                break
    dist[start]=c
    return dist[start]
            

mat = [l.strip() for l in sys.stdin]


start  = (0,0)
end = (0,0)
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j]=='S':
            start = (i,j)
        if mat[i][j]=='E':
            end = (i,j)

dist = {}

walk(start, end, mat, dist)

count = 0 
for k,v in reversed(dist.items()):
    for d in directions:
        p = (k[0]+2*d[0], k[1]+2*d[1])
        if p in dist:
            nv = dist[p]
            if v-nv-2>=100:
                #print(k,p, nv, v)
                #print(v-nv-2)
                count+=1
print(count)
    
