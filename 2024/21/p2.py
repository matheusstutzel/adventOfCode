import sys
from collections import deque
from functools import cache
import math

direction = {
(0,1):'>',
(-1,0):'^',
(0,-1):'<',
(1,0):"v"
}


def valid(mat, x,y):
    return x>=0 and x<len(mat) and y>=0 and y<len(mat[x]) and mat[x][y]!='#'

def precalc(mat):
    resp = {}
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j]=='#':
                continue
            for k in range(len(mat)):
                for l in range(len(mat[k])):
                    if k == i and l==j:
                        continue
                    resp[(i,j,k,l)] = paths(mat,(i,j),(k,l))
    return resp    
    
def paths(mat, start, end):
    q = deque([(*start, [start])])
    result = []
    m = math.inf
    while q:
        x,y,path = q.popleft()
        if (x,y) == end and len(path)<=m:
            if len(path) < m:
                result.clear()
            m = len(path)
            result.append(path)
            continue
        for d in direction:
            u = (x+d[0], y+d[1])
            if valid(mat, *u) and u not in path:
                q.append((*u, path+[u]))  
    final=[]
    for r in result:
        f =[]
        for i in range(1,len(r)):
            mov = (r[i][0]-r[i-1][0], r[i][1]-r[i-1][1])   
            #print(r, r[i-1], r[i]) 
            f.append(direction[mov])
        f.append('A')
        final.append(f)
    return final

def toCord(mat):
    result = {}
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            result[mat[i][j]]=(i,j)
    return result


pad = [
    "789",
    "456",
    "123",
    "#0A"
]
pad2cord = toCord(pad)

padpaths = precalc(pad) #precalc

dpad = [
    "#^A",
    "<v>"
]
dpad2cord = toCord(dpad)
dpadpaths = precalc(dpad) #precalc


def genericpad(c,p2cord, allpaths, mat, start = 'A'):
    current = p2cord[start]
    options = []
    for i in c:
        target = p2cord[i]
        
        paths = allpaths[(*current, *target)] if current!=target else [['A']]
        #print("going from ", current, "(",mat[current[0]][current[1]],") to ", target, "(",mat[target[0]][target[1]],") path ", paths)
        response = []
        if len(options) ==0:
            response = []+paths
        else:
            for o in options:
                for p in paths:
                    response.append(o+p)
        options = response        
        current = target
    m = min([len(o) for o in options])
    return ["".join(o) for o in options if len(o)==m]
def numpad(c):
    #print("numapd",c)
    return genericpad(c, pad2cord, padpaths, pad)

def dirpad(c, start):
    r = []
    for x in c:
        #print("dirpad", x)
        r.extend(genericpad(x, dpad2cord, dpadpaths, dpad, start))
    m = min(len(x) for x in r )
    return [x for x in r if len(x)==m]
@cache
def dp(c,d):
    response = 0
    c = 'A'+c
    for i in range(1, len(c)):
        paths = genericpad(c[i], dpad2cord, dpadpaths, dpad, c[i-1])
        if d ==0:
            response += min([len(path) for path in paths])
        else:
            response += min(dp(path, d-1)  for path in paths)
    return response
            
def solve(c):
    #print(options)
    return min([dp(x,24) for x in numpad(c)])



l = [l.strip() for l in sys.stdin]

resp = 0
for c in l:
    numeric = int(c.replace('A', ''))
    size = solve(c)
    print(size, numeric)
    resp+= size*numeric
print(resp)
    
