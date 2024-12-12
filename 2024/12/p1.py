import sys
from collections import deque

alternatives = [
    (-1,0),
    (0,-1),
    (1,0),
    (0,1)
]

def invalid(x,y,mat):
    return not (x>=0 and x<len(mat) and y>=0 and y<len(mat[x]))

def flood(mat, start, visit):
    v = mat[start[0]][start[1]]
    a = 0
    p = 0
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
            elif mat[x][y]!=v:
                p+=1
            else:
                q.append((x,y))
    return a,p

mat = [l.strip() for l in sys.stdin]

visited = set()

resp = 0
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if (i,j) in visited:
            continue
        a,p = flood(mat, (i, j), visited)
        print("region of ", mat[i][j], " area ",a, " perimeter ",p)
        resp += a*p
print(resp)
