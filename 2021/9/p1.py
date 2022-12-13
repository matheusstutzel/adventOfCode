import sys

def edges(i,j):
    e = []
    #top
    if(i>0):
        e.append((i-1,j))
    #left
    if(j>0):
        e.append((i,j-1))
    #down
    if(i+1<rows):
        e.append((i+1, j))
    #right
    if(j+1<cols):
        e.append((i, j+1))
    return e


def check(a,b):
    return a<b
l = [[int(t) for t in l.strip()] for l in sys.stdin]

rows = len(l)
cols = len(l[0])

sum = 0 

for i in range(rows):
    for j in range(cols):
        v = l[i][j]
        if all([v < l[p[0]][p[1]] for p in edges(i,j)]):
            sum = sum + 1 + int(v)        
print(sum)

