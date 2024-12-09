import sys

def test(map, pos, dir,options, ob):
#    print("testing", ob)
    visit=set()
    
    while (pos[0]>=0 and pos[0]<len(map)) and (pos[1]>=0 and pos[1]<len(map[pos[0]])):
        visit.add((pos[0], pos[1], dir))
        (nextDir, delta) = options[dir]
        ni = pos[0]+delta[0]
        nj = pos[1]+delta[1]
        if (ni,nj, dir) in visit:
            #print(map)
            return True
            
        if ni<0 or ni>=len(map) or nj<0 or nj>=len(map[ni]):
            pos=(ni,nj)
            continue
        if map[ni][nj]=="#" or (ni,nj)==ob:
            #print((ni,nj)==ob, ob)
            dir=nextDir
            continue
        pos=(ni, nj)
    return False
    

map = [l.strip() for l in sys.stdin]

options = {"^":(">", (-1,0)), ">":("v", (0,1)), "v":("<", (1,0)), "<":("^", (0,-1))}


pos=(0,0)
dir = ">"
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] in options:
            pos=(i,j)
            dir=map[i][j]
            break

initpos= pos
initdir = dir
while (pos[0]>=0 and pos[0]<len(map)) and (pos[1]>=0 and pos[1]<len(map[pos[0]])):
    line = map[pos[0]]
    line = line[:pos[1]]+"X"+line[pos[1]+1:]
    map[pos[0]]=line
    (nextDir, delta) = options[dir]
    ni = pos[0]+delta[0]
    nj = pos[1]+delta[1]

    if ni<0 or ni>=len(map) or nj<0 or nj>=len(map[ni]):
        pos=(ni,nj)
        continue
    if map[ni][nj]=="#":
        dir=nextDir
        continue
    pos=(ni, nj)

ob = [] 
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j]=="X":
            ob.append((i,j))
print(len(ob))

count=0
for x in ob:
    if test(map, initpos,initdir,options, x):
        #print(x)
        count+=1
print(count)
