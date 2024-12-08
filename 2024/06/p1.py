import sys

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

step = 0 
for i in map:
    for j in i:
        if j=="X":
            step+=1
print(step)
