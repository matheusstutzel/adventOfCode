import sys
from collections import deque

alternatives = [
    (-1,0),
    (0,-1),
    (1,0),
    (0,1)
]
direction = {"^":((0,-1), (0,1)), ">":((1,0), (-1,0)), "v":((0,1), (0,-1)), "<":((-1,0), (1,0))}
sym = {
    (-1,0): '^',
    (0,-1): '<',
    (1,0): 'v',
    (0,1): '>'

    
}

def invalid(x,y,mat):
    return not (x>=0 and x<len(mat) and y>=0 and y<len(mat[x]))

def walkBorder(e):
    s = 0
    for k in e:
        # k = ^>v<
        x = e[k]
        a,b = direction[k]
        while len(x)>0:
            p = x.pop()
            #walk into a removing
            k = (p[0]+a[0], p[1]+a[1])
            while k in x:
                x.remove(k)
                k = (k[0]+a[0], k[1]+a[1])

            #walk into b removing
            k = (p[0]+b[0], p[1]+b[1])
            while k in x:
                x.remove(k)
                k = (k[0]+b[0], k[1]+b[1])
            s+=1
    return s   
            

def flood(mat, start, visit):
    v = mat[start[0]][start[1]]
    a = 0
    p = 0
    e = {}
    for k in sym.values():
        e[k]=set()
    q = deque([start])
    while q:
        d = q.popleft()
        if d in visit:
            continue
        visit.add(d)
        a+=1
        for u in alternatives:
            x = d[0]+u[0]
            y = d[1]+u[1]
            if invalid(x,y,mat):
                p+=1
                e[sym[u]].add(d)
            elif mat[x][y]!=v:
                p+=1
                e[sym[u]].add(d)
            else:
                q.append((x,y))
    return a,p,e

mat = [l.strip() for l in sys.stdin]

visited = set()

resp = 0
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if (i,j) in visited:
            continue
        a,p,e = flood(mat, (i, j), visited)
        print("region of ", mat[i][j], " area ",a, " perimeter ",p)
        #print("external ",e)
        # i,j is a top-left corner
        s = walkBorder(e)
        print("slices ", s)
        resp += a*s
print(resp)
