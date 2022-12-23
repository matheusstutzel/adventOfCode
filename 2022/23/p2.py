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
            c = elves[(i,j)] if (i,j) in elves else '.'
            print(c, end='')
        print("")
    print("________")
    return (maxX-minX+1)*(maxY-minY+1) - len(elves)


elves = dict()

for i,l in enumerate(sys.stdin):
    for j,v in enumerate(l):
        if(v=='#'):
            elves[(i,j)]= chr(len(elves)+ ord('A'))


checks = [
    lambda x,y: (x-1, y) if( (x-1,y-1) not in elves and (x-1,y) not in elves and (x-1,y+1) not in elves) else (x,y), #north
    lambda x,y: (x+1, y) if( (x+1,y-1) not in elves and (x+1,y) not in elves and (x+1,y+1) not in elves) else (x,y), #south
    lambda x,y: (x, y-1) if( (x-1,y-1) not in elves and (x,y-1) not in elves and (x+1,y-1) not in elves) else (x,y), #west
    lambda x,y: (x, y+1) if( (x-1,y+1) not in elves and (x,y+1) not in elves and (x+1,y+1) not in elves) else (x,y)  #east
]

check = 0
while True:
    newElves = defaultdict(list)
    for e in elves:
        movs = []
        for k in range(4):
            mov = checks[(check+k)%4](*e)
            if(mov != e):
                movs.append(mov)
        if(len(movs)==4 or len(movs)==0):
            #print("using none", e)
            newElves[e].append(e)
        else:
            newElves[movs[0]].append(e)
    aux = dict()
    for ne, v in newElves.items():
        if(len(v)==1):
            aux[ne]=elves[v[0]]
        else:
            for k in v:
                aux[k]=elves[k]
    if(len(aux)!=len(elves)):
        print(aux,"\n", elves)
        raise RuntimeError(":/")
    check= check+1
    
    if(elves == aux):
        break
    elves = aux
    
        
result = printa()
print(result, check)