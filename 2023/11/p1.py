import sys
from collections import deque

def addLines(mat):    
    size = len(mat)
    nm = []
    for i in range(size):
        r = True
        for j in range(size):
            r = r and mat[i][j] != '#'
        nm.append(mat[i])
        if r:
            nm.append(['.' for _ in range(size)])
    return nm
def addColumn(mat):
    size = len(mat)
    nm=[]
    for i in range(size):
        nm.append([])
    for i in range(len(mat[0])):
        c = True
        for j in range(size):
            c = c and mat[j][i] != '#'
            nm[j].append(mat[j][i])
        if c:
            for j in range(size):
                nm[j].append('.')
    return nm
def findPoints(mat):
    p = []
    for i, l in enumerate(mat):
        for j, c in enumerate(l):
            if c == '#':
                p.append((i,j))
    return p


mat = [[*l.strip()] for l in sys.stdin]
mat = addLines(mat)
mat = addColumn(mat)
points = findPoints(mat)

dists = []


for i in range(len(points)):
    p1 = points[i]
    for j in range(i+1, len(points)):
        p2 = points[j]
        x = abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
        dists.append(x)
print(sum(dists))