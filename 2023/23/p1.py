import sys
from collections import deque

dir = {
    '#':[],
    '>':[(0,1)],
    '<':[(0,-1)],
    '^':[(-1,0)],
    'v':[(1,0)],
    '.': [(-1,0), (0,-1), (0,1), (1,0)]
}

def neighbors(g,x,y):
    c = g[x][y]
    for i,j in dir[c]:
        a = x+i
        if a<0 or a>=len(g):
            continue
        b = y+j
        if b<0 or b>=len(g[a]):
            continue
        if i == 0 and j == 0:
            continue
        c = g[a][b]
        if c == '#':
            continue
        yield (a,b)

def bfs(g,v,t): #graph, value, targets
    s = {(str(v))} #seen
    q = deque([[v]]) #queue
    d = 0
    mp = []
    while q:
        path = q.popleft()
        p = path[-1]
        if p == t and len(path)>d:
            d = len(path)
            mp = path
            continue
        for u in neighbors(g,*p):
            if len(path)>1 and u == path[-2]:
                continue
            npath = "".join([str(x) for x in path]) + str(u)
            if npath not in s:
                s.add(npath)
                q.append(path+[u])
    return d,mp


mat = [[*l.strip()] for l in sys.stdin]

d, mp= bfs(mat, (0,1), (len(mat)-1, len(mat)-2))

print(d-1)

'''
for i,l in enumerate(mat):
    for j,c in enumerate(l):
        if (i,j) in mp:
            c = 'O'
        print(c, end="")
    print("")

real    0m40,955s
user    0m40,129s
sys     0m0,823s
'''
