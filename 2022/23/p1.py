import sys
from math import inf
from collections import defaultdict

def printa():
    minX = minY = inf
    maxX = maxY = -inf
    for e in elves:
        x,y = e
        minX = min(minX,x)
        minY = min(minY,y)
        maxX = max(maxX,x)
        maxY = max(maxY,y)
    print("________")
    for i in range(minX, maxX+1):
        for j in range(minY, maxY+1):
            c = '#' if (i,j) in elves else '.'
            print(c, end='')
        print("")
    print("________")
    return (maxX-minX+1)*(maxY-minY+1) - len(elves)


elves = set()

for i,l in enumerate(sys.stdin):
    for j,v in enumerate(l):
        if(v=='#'):
            elves.add((i,j))
printa()

checks = [
    lambda x,y: (x-1, y) if( (x-1,y-1) not in elves and (x-1,y) not in elves and (x-1,y+1) not in elves) else None, #north
    lambda x,y: (x+1, y) if( (x+1,y-1) not in elves and (x+1,y) not in elves and (x+1,y+1) not in elves) else None, #south
    lambda x,y: (x, y-1) if( (x-1,y-1) not in elves and (x,y-1) not in elves and (x+1,y-1) not in elves) else None, #west
    lambda x,y: (x, y+1) if( (x-1,y+1) not in elves and (x,y+1) not in elves and (x+1,y+1) not in elves) else None,  #east
    lambda x,y: any([ (i,j)!=(0,0) and (x+i,y+j) in elves for i in range(-1,2) for j in range(-1,2)]) # is there any elve around?
]

check = 0
for i in range(10):
    newElves = defaultdict(set)
    for e in elves:
        if(not checks[4](*e)):
            newElves[e].add(e)
            continue
        for k in range(4):
            mov = checks[(check+k)%4](*e)
            if mov:
                newElves[mov].add(e)
                break
        else:
            newElves[e].add(e)
    aux = set()
    for ne, v in newElves.items():
        if(len(v)==1):
            aux.add(ne)
        else:
            aux = aux | v
    elves = aux
    check= check+1
        
result = printa()
print(result, check)