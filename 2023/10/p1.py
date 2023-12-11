import sys
from math import ceil
from collections import deque

mat = [l.strip() for l in sys.stdin]

dir = {
    '|':[(-1,0), (1,0)],
    '-':[(0,-1), (0,1)],
    'L':[(-1,0), (0,1)],
    'J':[(-1,0), (0,-1)],
    '7':[(1,0), (0,-1)],
    'F':[(1,0), (0,1)],
    'S':[(-1,0),(0,-1),(0,1),(1,0)],
    '.':[],
}

def neighbors(x,y):
    for i,j in dir[mat[x][y]]:
        a = i + x
        b = j + y
        if a<0 or a>=len(mat):
            continue
        if b<0 or b>=len(mat[a]):
            continue
        if mat[a][b] == '.':
            continue
        yield (a,b)
def next (c,p):
    for n in neighbors(*c):
        if n == p:
            continue
        return n

start = (0,0)
for i, l in enumerate(mat):
    for j, c in enumerate(l):
        if c == 'S':
            start = (i,j)

c = start
prev = start
depth = 0
while c == prev or c!=start:
    n = next(c,prev)
    print(c, prev, n)
    prev, c = c, n
    depth = depth + 1

print(*start, depth, depth//2)