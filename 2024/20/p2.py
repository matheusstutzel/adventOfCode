import sys
import math 
import heapq
from collections import deque
directions = [
    (0,1),(-1,0), (0,-1), (1,0)
]

def valid(x,y,mat):
    return  x>=0 and x<len(mat) and y>=0 and y<len(mat[x]) and mat[x][y]!='#'
def manhattan(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])
    
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
    for k2,v2 in dist.items():
        d =manhattan(k,k2) 
        if d<=20 and v2-v-d>=100:
            #print(k,k2, v,v2, count)
            count+=1
print(count)
    
