import sys

def instructions():
    aux = ""
    for i in path:
        if i == 'R' or i == 'L':
            yield int(aux) 
            aux = ""
            yield i
        else:
            aux = aux + i
    yield int(aux)

def apply(point, ins):
    if not isinstance(ins, int):
        increment = 1 if ins == 'R' else -1
        return (point[0], point[1], (point[2]+increment)%4)
    x,y,z = point
    mov = movement[z]
    for _ in range(ins):
        x2,y2 = move(x,y,*mov)
        if(x == x2 and y==y2):
            break
        x = x2
        y = y2
    return (x,y,z)
def move(x,y, dx,dy):
    nx = x 
    ny = y
    while True:
        nx = (nx+dx)%rows
        ny = (ny+dy)%cols 
        if(ny>= len(mat[nx])):
            continue
        v = mat[nx][ny]
        if v == '.':
            return nx,ny
        elif v == '#':
            return x,y

mat = [l.replace("\n","") for l in sys.stdin]

path = mat[-1:][0]

mat = mat[:-2]

rows = len(mat)
cols = len(mat[0])

# find starting point
for i in range(rows):
    for j in range(cols):
        if(mat[i][j]=='.'):
            x = i
            y = j
            break
    else:
        continue
    break

RIGHT = (0,1)
DOWN = (1,0)
LEFT = (0,-1)
UP = (-1,0)

movement = [RIGHT,DOWN, LEFT, UP]
point = (x,y,0) #x,y, movement index/ RIGHT

for ins in instructions():
    point = apply(point, ins)

print(point)
x,y,z = point

print( 1000*(x+1) + 4*(y+1) + z) 