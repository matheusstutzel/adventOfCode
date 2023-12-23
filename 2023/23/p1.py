import sys
import heapq as hq

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


def dfs(g,v,t): #graph, value, targets
    dist = {v:0}
    s = {(str(v))} #seen
    q = [] #heap
    hq.heappush(q,(1,[v]))
    mp = []
    while q:
        size,path = hq.heappop(q)
        print(len(q), size, len(s))
        p = path[-1]
        if p in dist and size<dist[p]:
            continue
        dist[p]=size
        if p == t and size>dist[t]:
            mp = path
            continue
        for u in neighbors(g,*p):
            if u in path:
                continue
            npath = "".join([str(x) for x in path]) + str(u)
            if npath not in s:
                s.add(npath)
                hq.heappush(q, (size+1,path+[u]))
    return dist[t],mp


mat = [[*l.strip()] for l in sys.stdin]

d, mp= dfs(mat, (0,1), (len(mat)-1, len(mat)-2))

print(d-1)

'''
for i,l in enumerate(mat):
    for j,c in enumerate(l):
        if (i,j) in mp:
            c = 'O'
        print(c, end="")
    print("")
'''
