import sys
from collections import deque
import math

mat = [l.strip() for l in sys.stdin]
options = {
    "^":([">", "<"], (-1,0)), 
    ">":(["v", "^"], (0,1)), 
    "v":(["<", ">"], (1,0)), 
    "<":(["^", "v"], (0,-1))
}

def dfs(mat, start, end):
    values = []
    for i in range(len(mat)):
        values.append([])
        for j in range(len(mat[i])):
            values[i].append(
                {
                    ">":math.inf,
                    "v":math.inf,
                    "<":math.inf,
                    "^":math.inf
                }
            )
    q = deque([(*start, ">", 0)])
    while q:
        i,j,d,p = q.popleft()
        if len(q)%100==0:
            print(len(q))
        if i<0 or i>=len(mat) or j<0 or j>=len(mat[i]):
            continue
        if mat[i][j]=='#':
            continue
        if values[i][j][d]<p:
            continue
        values[i][j][d]=p
        if (i,j) == end:
            continue
        opt, delta = options[d]
        q.append([i+delta[0], j+delta[1], d, p+1])
        for x in opt:
            q.append([i,j,x,p+1000])
    return values[end[0]][end[1]]
start  = (0,0)
end = (0,0)
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j]=='S':
            start = (i,j)
        if mat[i][j]=='E':
            end = (i,j)
score = dfs(mat, start, end)
resp = math.inf
for _,v in score.items():
    resp=min(resp,v)
print(v)
