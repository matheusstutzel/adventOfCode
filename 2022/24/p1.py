import sys
from collections import defaultdict, deque

STAY = (0,0)
RIGHT = (0,1)
DOWN = (1,0)
LEFT = (0,-1)
UP = (-1,0)
moves = [STAY, RIGHT, DOWN, LEFT, UP]
movesChar = {
                RIGHT:'>',
                DOWN:'v', 
                LEFT: '<',
                UP: '^'
            }

def move(px, py, mx, my):
    return (px+mx, py+my)

def movements(pos):
    for m in moves:
        yield move(*pos, *m)

def valid(x,y, next=[]):
    p = (x,y)
    if p in next:
        return False

    if p==start or p==target:
        return True

    return x>0 and x<rows-1 and y>0 and y<cols-1

def moveBlizzard(px,py,mx,my):
    nx,ny = move(px,py,mx,my)
    while not valid(nx,ny):
        nx,ny = move(nx,ny,mx,my)
        nx = nx%rows
        ny = ny%cols
    return (nx,ny)

def tick(blizzard):
    n = defaultdict(list)
    for k,v in blizzard.items():
        for m in v:
            n[moveBlizzard(*k,*m)].append(m)
    return n

def bfs(start, target, blizzard): #graph, value, targets
    q = deque([start]) #queue
    round = 0
    while q:
        blizzard = tick(blizzard)
        s = set() #seen
        for _ in range(len(q)): #all in this round
            p = q.popleft()
            if p == target:
                return round
            for u in movements(p):
                va = valid(*u, blizzard)
                #print("testando ",p,u,va)
                if va and u not in s:
                    s.add(u)
                    q.append(u)
        #printa(blizzard, q)
        round = round+1 
    return round

def printa(blizzards, q):
    print("-"*cols)
    for i in range(rows) :
        for j in range(cols):
            c = '.'
            p = (i,j)
            if p in q:
                c='E'
            elif i==0 or j==0 or i==rows-1 or j==cols-1:
                c='#'
            elif p in blizzards:
                matches = blizzards[p]
                c = movesChar[matches[0]] if len(matches)==1 else str(len(matches))
            print(c,end="")
        print("")
l = [l.strip() for l in sys.stdin]

rows = len(l)
cols = len(l[0])

start = (0,1)
target = (rows-1, cols-2)

blizzard = defaultdict(list)
for i in range(rows):
    for j in range(cols):
        c = l[i][j]
        p = (i,j)
        if c == '>':
            blizzard[p].append(RIGHT)
        if c == '<':
            blizzard[p].append(LEFT)
        if c == '^':
            blizzard[p].append(UP)
        if c == 'v':
            blizzard[p].append(DOWN)

result = bfs(start, target, blizzard)    
print(result)








