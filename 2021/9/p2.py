import sys
from math import prod

def edges(i,j):
    e = []
    #top
    if(i>0):
        e.append((i-1,j))
    #left
    if(j>0):
        e.append((i,j-1))
    #down
    if(i+1<rows):
        e.append((i+1, j))
    #right
    if(j+1<cols):
        e.append((i, j+1))
    return e

def dfs(l, p):
    if(l[p[0]][p[1]]==9):
        return 0
    l[p[0]][p[1]] = 9
    size = 1
    for t in edges(p[0],p[1]):
        size = size + dfs(l, t)
    return size 

l = [[int(t) for t in l.strip()] for l in sys.stdin]

rows = len(l)
cols = len(l[0])

low = []

for i in range(rows):
    for j in range(cols):
        v = l[i][j]
        if all([v < l[p[0]][p[1]] for p in edges(i,j)]):
            low.append((i,j))

basin = prod(sorted([dfs(l,p) for p in low])[-3:])

print(basin)

