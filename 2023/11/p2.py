import sys
from collections import deque

def empty(mat):
    size = len(mat)
    er = set()
    ec = set()
    
    for i in range(size):
        r = True
        c = True
        for j in range(size):
            r = r and mat[i][j] != '#'
            c = c and mat[j][i] != '#'
        if r:
            er.add(i)
        if c:
            ec.add(i)
    return er,ec

def findPoints(mat):
    p = []
    for i, l in enumerate(mat):
        for j, c in enumerate(l):
            if c == '#':
                p.append((i,j))
    return p


mat = [[*l.strip()] for l in sys.stdin]
el, ec = empty(mat)
points = findPoints(mat)
dists = []
weight = 1000000


for i in range(len(points)):
    p1 = points[i]
    for j in range(i+1, len(points)):
        p2 = points[j]
        x = 0
        for k in range(min(p1[0], p2[0]), max(p1[0], p2[0])):
            x = x + (weight if k in el else 1)

        for k in range(min(p1[1], p2[1]), max(p1[1], p2[1])):
            x = x + (weight if k in ec else 1)

        dists.append(x)
print(sum(dists))
