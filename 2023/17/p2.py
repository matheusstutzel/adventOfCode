import sys
from heapq import heappush, heappop

lines = [[*l.strip()] for l in sys.stdin]

RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
UP = (-1, 0)

movement = [RIGHT, DOWN, LEFT, UP]
def valid(x,y):
    return not(x<0 or y<0 or x>=(len(lines)) or y>=(len(lines[x])))
def neig(x,y,d):
    if d == RIGHT or d==LEFT:
            yield DOWN
            yield UP
    elif d == DOWN or d==UP:
        yield RIGHT
        yield LEFT
    else: #start
        yield RIGHT
        yield DOWN

def dfs(g, mmin, mmax):
    p = (0,0)
    t = (len(g)-1, len(g[0])-1)
    heap = [(0, (0,0), (0,0))]
    hmap = {(0,0):0}
    s = set() #seen
    while heap:
        cost, p, d = heappop(heap)
        
        if p==t:
            return cost
        if (p, d) in s:
            continue
        s.add((p,d))
        
        x,y = p
        for nd in neig(x,y,d):
            nc = cost
            dx,dy = nd
            for i in range(1, mmax+1):
                np = (x+i*dx, y+i*dy)
                if not valid(*np):
                    continue
                nc = nc + int(g[np[0]][np[1]])
                if i>=mmin:
                    u = (np, (dx,dy))
                    if hmap.get(u, 999999999999999)<=nc:
                        continue
                    hmap[u]=nc
                    heappush(heap, (nc, np, nd))
    return cost


print(lines)
print(dfs(lines, 4,10))