import sys
from collections import deque
lines = [[*l.strip()] for l in sys.stdin]

RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
UP = (-1, 0)

movement = [RIGHT, DOWN, LEFT, UP]


def bfs(g,v,m): #graph, value
    s = {v} #seen
    q = deque([v]) #queue
    while q:
        p = q.popleft()
        x,y,d = p
        if not(x<0 or y<0 or x>=(len(g)) or y>=(len(g[x]))):
            m[x][y]=m[x][y]+1
        a = x + d[0]
        b = y + d[1]
        if a<0 or b<0 or a>=(len(g)) or b>=(len(g[a])):
            continue
        c = g[a][b]
        u = []
        if c == '.':
             u.append((a,b,d))
        if c == '|': 
            if d == DOWN or d == UP:
                u.append((a,b,d))
            else:
                u.append((a,b,DOWN))
                u.append((a,b,UP))
        if c == '-': 
            if d == DOWN or d == UP:
                u.append((a,b,LEFT))
                u.append((a,b,RIGHT))
            else:
                u.append((a,b,d))
        if c == '\\':
            if d == DOWN:
                u.append((a,b,RIGHT))
            if d == LEFT:
                u.append((a,b,UP))
            if d == UP:
                u.append((a,b,LEFT))
            if d == RIGHT:
                u.append((a,b,DOWN))
        if c == '/':
            if d == DOWN:
                u.append((a,b,LEFT))
            if d == LEFT:
                u.append((a,b,DOWN))
            if d == UP:
                u.append((a,b,RIGHT))
            if d == RIGHT:
                u.append((a,b,UP))
                
        for t in u:
            if t not in s:
                s.add(t)                
                q.append(t)


def count(lines, start):
    m = []
    for i in range(len(lines)):
        k = []
        m.append(k)
        for _ in range(len(lines[i])):
            k.append(0)
    bfs(lines, start, m)
    total = 0
    for i in m:
        total = total + sum([min(k,1) for k in i])
    #    for c in i:
    #        print(c, end="")
    #    print("")
    #print(total)
    return total
result =0
end = len(lines)
for i in range(end):
    result = max(result,count(lines, (i,-1, RIGHT)))
    result = max(result,count(lines, (i,end, LEFT)))
    result = max(result,count(lines, (-1,i, DOWN)))
    result = max(result,count(lines, (end,i, UP)))
print(result)