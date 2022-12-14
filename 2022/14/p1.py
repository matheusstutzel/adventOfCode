import sys


def check(pos, i,j):
    i = i + pos[0]
    j = j + pos[1]
    return i>=0 and j>=0 and i<len(mat) and j<len(mat[0]) and mat[i][j]=='.' 


def simulate():
    pos = [500,-1]
    while True:
        if check(pos,0,1):
            pos = [pos[0], pos[1]+1]
        elif check(pos,-1,1):
            pos = [pos[0]-1, pos[1]+1]
        elif check(pos,1,1):
            pos = [pos[0]+1, pos[1]+1]
        else:
            return pos

    

def drop():
    if(mat[500][0]=='o'):
        return
    pos = simulate()
    if(pos[1]>maxY):
        return False
    mat[pos[0]][pos[1]]='o'
    return True

def printa():
    print("")
    minX = len(mat)
    maxX = 0

    minY = len(mat[0])
    maxY = 0

    for j in range(len(mat[0])-1):
        for i in range(len(mat)):
            if mat[i][j]!='.':
                minX = min (minX, i)
                maxX = max (maxX, i)


                minY = min (minY, j)                
                maxY = max (maxY, j)
    for j in range(minY, maxY+1):
        for i in range(minX, maxX+1):
            print(mat[i][j], end="")
        print("")

lines = [[ [int(j) for j in i.strip().split(",")] for i in l.split("->")] for l in sys.stdin]

maxY = max([max(k, key= lambda y: y[1])[1] for k in lines])

mat = []
for i in range(2000):
    mat.append(['.']*(maxY+3))

printa()

for line in lines:
    src = line[0]
    for i in range(1, len(line)):
        dest = line[i]

        deltaX = dest[0]-src[0]
        deltaY = dest[1]-src[1]
        mov = [0 if deltaX ==0 else  deltaX//abs(deltaX), 0 if deltaY ==0 else deltaY//abs(deltaY)]
        while src != dest:
            mat[src[0]][src[1]] = '#'
            src = [src[0]+mov[0], src[1]+mov[1]]
        mat[src[0]][src[1]] = '#'

printa()

c = 0
while drop():
    c = c+1
    if(c%1000==0):
        print(c)
        printa()
printa()
print(c)