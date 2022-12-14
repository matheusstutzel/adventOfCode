import sys


def check(pos, mov):
    i,j = mov
    i = i + pos[0]
    j = j + pos[1]
    resp = i>=0 and j>=0 and i<(maxX*2) and j<=maxY+2 and mat[i][j]=='.' 
    #print("check ", pos, mov, i,j, maxX, maxY,resp, mat[i][j])
    return resp


def simulate():
    pos = [500,-1]
    while True:
        if check(pos,[0,1]):
            pos = [pos[0], pos[1]+1]
        elif check(pos,[-1,1]):
            pos = [pos[0]-1, pos[1]+1]
        elif check(pos,[1,1]):
            pos = [pos[0]+1, pos[1]+1]
        else:
            return pos

    

def drop():
    pos = simulate()
    if(pos[1]>=maxY+2 or pos == [500,-1]):
        print("caiu fora", pos, maxY)
        return False
    mat[pos[0]][pos[1]]='o'
    return True

def printa():
    print("")
    minX = len(mat)
    maxX = 0

    minY = len(mat)
    maxY = 0

    for j in range(len(mat[0])-1):
        for i in range(len(mat)):
            if mat[i][j]!='.':
                minX = min (minX, i)
                maxX = max (maxX, i)


                minY = min (minY, j)                
                maxY = max (maxY, j)
    for j in range(minY, maxY):
        for i in range(minX, maxX):
            print(mat[i][j], end="")
        print("")
lines = [[ [int(j) for j in i.strip().split(",")] for i in l.split("->")] for l in sys.stdin]

maxX = max([max(k, key= lambda y: y[0])[0] for k in lines])
maxY = max([max(k, key= lambda y: y[1])[1] for k in lines])

minX = min([min(k, key= lambda y: y[0])[0] for k in lines])
minY = min([min(k, key= lambda y: y[1])[1] for k in lines])

# at this point I could simulate everything from (0,0) to (maxX+1, maxY+1)
# but I prefer to translate everything (-minX+1, -minY+1)

mat = []
for i in range((maxX*2)):
    mat.append(['.']*(maxY+3))

printa()

for line in lines:
    src = line[0]
    for i in range(1, len(line)):
        dest = line[i]

        deltaX = dest[0]-src[0]
        deltaY = dest[1]-src[1]
        mov = [0 if deltaX ==0 else  deltaX//abs(deltaX), 0 if deltaY ==0 else deltaY//abs(deltaY)]
        print("making line from ", [src[0],src[1]], "to", [dest[0],dest[1]])
        while src != dest:
            print(src, dest, mov, minX, minY, maxX, maxY, len(mat), len(mat[0]))
            mat[src[0]][src[1]] = '#'
            src = [src[0]+mov[0], src[1]+mov[1]]
        mat[src[0]][src[1]] = '#'
for i in range(len(mat)):
    mat[i][maxY+2] = '#'
printa()

c = 0 
while drop():
    c = c+1
    print(c)
    if(c%100==0):
        printa()
    if(mat[500][0]=='o'):
        break
printa()
print(c)