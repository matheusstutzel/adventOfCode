import sys

d={
    "<":(0,-1),
    "^":(-1,0),
    ">":(0,1),
    "v":(1,0)
}

def printa(c,mat):
    if 1>0:
        return
    print(c)
    for l in mat:
        print("".join(l))

def apply(mat,p, c):
    move=False
    delta = d[c]
    nx = p[0]+delta[0]
    ny = p[1]+delta[1]

    bx = nx
    by = ny
    box = False

    while mat[bx][by] == 'O':
        box=True
        bx = bx+delta[0]
        by = by+delta[1]
    if box and mat[bx][by]=='.':
        mat[bx][by]='O'
        move = True
    if mat[nx][ny]=='.':
        move=True
    
    if move:
        mat[p[0]][p[1]] = '.'
        mat[nx][ny]='@'
        return (nx,ny)
    return p

mat = []

for l in sys.stdin:
    if len(l.strip())==0:
        break
    mat.append(list(l.strip()))

printa(0,mat)
commands = "".join([l.strip() for l in sys.stdin])
#print(commands)

s = (0,0)
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j]=='@':
            s = (i,j)
for c in commands:
    s=apply(mat,s,c)
    printa(c,mat)
result = 0 
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j]=='O':
            result+= 100*i+j
print(result)
