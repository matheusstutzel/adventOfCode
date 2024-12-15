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
    print()

def check(mat, delta, opts):
    nopts = set()
    for ox,oy in opts:
        v = mat[ox+delta][oy]
        if v == '.':
            continue
        if v =='#':
            return 0
        nopts.add((ox+delta,oy))
        nopts.add((ox+delta,oy + (1 if v=='[' else -1)))
    if len(nopts) == 0:
        return 1
    r = check(mat, delta, nopts)
    if r == 0:
        return 0
    return r+1
        
def edit(mat, delta, opts, fit):
    if fit<0:
        return
    nopts = set()
    maybeDelete = set() 
    for ox,oy,nv in opts:
        v = mat[ox+delta][oy]
        if v in '[]':
            nopts.add((ox+delta, oy, v))
            ny = oy +(1 if v=='[' else -1)
            nopts.add((ox+delta, ny, '['if v==']'else']'))
            maybeDelete.add((ox, ny))
        mat[ox+delta][oy]=nv
    for x,y,_ in opts:
        maybeDelete.discard((x,y))
    for x, y in maybeDelete:
        mat[x+delta][y]='.'
    edit(mat, delta, nopts, fit-1)

def moveh(mat,p,c):
    delta = d[c]
    nx = p[0]+delta[0]
    ny = p[1]+delta[1]

    bx,by = nx,ny
    while mat[bx][by] in "[]":
        bx = bx+delta[0]
        by = by+delta[1]
    if mat[bx][by]=='#':
        return p    
    
    mat[p[0]][p[1]]='.'
    mat[nx][ny] = '@'
    box ="[]"
    b=0 if c=='>' else 1
    for i in range(abs(ny-by)):
        mat[bx][ny+((i+1)*delta[1])]=box[(b+i)%2]
        i+=1
    return (nx,ny)

def movev(mat,p,c):
    delta = d[c]
    nx = p[0]+delta[0]
    ny = p[1]+delta[1]

    v = mat[nx][ny]

    if v=='.':
        mat[p[0]][p[1]]='.'
        mat[nx][ny] = '@'
        return (nx,ny)
    if v=='#':
        return p

    #found box, check if fit
    fit = check(mat, delta[0], [(nx,ny), (nx,ny + (1 if v=='[' else -1))])

    if fit == 0 :
        return p

    #fit has the n# of rows will be edited 
    mat[p[0]][p[1]]='.'
    edit(mat, delta[0], [(*p, '@')], fit)
    return (nx,ny)
    
def apply(mat,p, c):
    if c in "<>":
        return moveh(mat, p,c)
    else:
        return movev(mat,p,c)

mat = []

for l in sys.stdin:
    if len(l.strip())==0:
        break
    l = list(l.strip())
    x=[]
    for c in l:
        if c=='@':
            x.append('@')
            x.append('.')
        elif c=='O':
            x.append('[')
            x.append(']')
        else:
            x.append(c)
            x.append(c)
    mat.append(x)

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
        if mat[i][j]=='[':
            result+= 100*i+j
print(result)
