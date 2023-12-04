import sys
import math

def neighbors(x,y):
    for i in [-1,0,1]:
        a = x+i
        if a<0 or a>=len(mat):
            continue
        for j in [-1,0,1]:
            b = y+j
            if b<0 or b>=len(mat[a]):
                continue
            if i == 0 and j == 0:
                continue
            yield (mat[a][b], a,b)


def findStar(stars, i,j):
    for n, i2,j2 in neighbors(i,j):
        if n=='*':
            stars.add((i2,j2))
    return stars
mat = [l.strip() for l in sys.stdin]
#print(mat)

num = False

stars = set()
acc = []
den = []
result = {}

current = 0
for i, l in enumerate(mat):
    for j, c in enumerate(l):
        if num:
            if c.isnumeric():
                current = current*10 + int(c) 
                stars = findStar(stars, i, j)
            else:
                for x,y in stars:
                    if x not in result:
                        result[x]={}
                    if y not in result[x]:
                        result[x][y]=[]
                    result[x][y].append(current)
                num = False
                stars = set()
        else:
            if c.isnumeric():
                num = True
                current = int(c)
                stars = findStar(stars, i, j)
finalResult=0
for i in result:
    for j in result[i]:
        v = result[i][j]
        size = len(v)
        if size==2:
            finalResult = finalResult + math.prod(v)
print(finalResult)