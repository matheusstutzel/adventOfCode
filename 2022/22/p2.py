import sys

'''
 12
 3
45
6
'''
bounds = [
    (0, 50, 50, 100),
    (0, 100, 50, 150),
    (50, 50, 100, 100),
    (100, 0, 150, 50),
    (100, 50, 150, 100),
    (150, 0, 200, 50)
]

RIGHT = (0, 1)
DOWN = (1, 0)
LEFT = (0, -1)
UP = (-1, 0)

movement = [RIGHT, DOWN, LEFT, UP]

def SAME(x, y): return (x, y)

boundMovements = [
    {
        RIGHT: (SAME, RIGHT, 1),  # 1 to 2
        DOWN: (SAME, DOWN, 2),  # 1 to 3
        LEFT: (lambda x, y: (49-x+100, 0), RIGHT, 3),  # 1 to 4
        UP: (lambda x, y: (150 + y-50, 0), RIGHT, 5),  # 1 to 6
    },
    {
        RIGHT: (lambda x, y: ((49-x)+100, y-51), LEFT, 4),  # 2 to 5
        DOWN: (lambda x, y: (y-50, 99), LEFT, 2),  # 2 to 3
        LEFT: (SAME, LEFT, 0),  # 2 to 1
        UP: (lambda x, y: (199, y-100), UP, 5),  # 2 to 6
    },
    {
        RIGHT: (lambda x, y: (49, x+50), UP, 1),  # 3 to 2
        DOWN: (SAME, DOWN, 4),  # 3 to 5
        LEFT: (lambda x, y: (100, x-50), DOWN, 3),  # 3 to 4
        UP: (SAME, UP, 0),  # 3 to 1
    },
    {
        RIGHT: (SAME, RIGHT, 4),  # 4 to 5
        DOWN: (SAME, DOWN, 5),  # 4 to 6
        LEFT: (lambda x, y: ((149-x), 50), RIGHT, 0),  # 4 to 1
        UP: (lambda x, y: (y+50, 50), RIGHT, 2),  # 4 to 3
    },
    {
        RIGHT: (lambda x, y: (149-x, 149), LEFT, 1),  # 5 to 2
        DOWN: (lambda x, y: (y-50+150, 49), LEFT, 5),  # 5 to 6
        LEFT: (SAME, RIGHT, 3),  # 5 to 4
        UP: (SAME, UP, 2),  # 5 to 3
    },
    {
        RIGHT: (lambda x, y: (149, x-150+50), UP, 4),  # 6 to 5
        DOWN: (lambda x, y: (0, y+100), DOWN, 1),  # 6 to 2
        LEFT: (lambda x, y: (0, x-150+50), DOWN, 0),  # 6 to 1
        UP: (SAME, UP, 3),  # 6 to 4
    },
]

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
    x, y, z, f = point
    if not isinstance(ins, int):
        increment = 1 if ins == 'R' else -1
        return (x, y, (z+increment) % 4, f)

    for _ in range(ins):
        x2, y2, z2, f2 = move((x, y, z, f))
        if(x == x2 and y == y2):
            break
        x, y, z, f = x2, y2, z2, f2
    return (x, y, z, f)


def move(point):
    x, y, z, f = point
    minX, minY, maxX, maxY = bounds[f]

    dx, dy = movement[z]
    nx = x+dx
    ny = y+dy
    nz = z
    nf = f
    if nx < minX or nx >= maxX or ny < minY or ny >= maxY:
        op, nz, nf = boundMovements[f][movement[z]]
        nz = movement.index(nz)
        nx, ny = op(nx, ny)

    v = mat[nx][ny]
    if v == '.':
        return nx, ny, nz, nf
    elif v == '#':
        return x, y, z, f
    else:
        raise IndexError


mat = [l.replace("\n", "") for l in sys.stdin]

path = mat[-1:][0]
mat = mat[:-2]

rows = len(mat)
cols = len(mat[0])

# find starting point
for i in range(rows):
    for j in range(cols):
        if(mat[i][j] == '.'):
            x = i
            y = j
            break
    else:
        continue
    break

point = (x, y, 0, 0)  # x,y, movement index/ RIGHT, face

for ins in instructions():
    point = apply(point, ins)

x, y, z, face = point

print(1000*(x+1) + 4*(y+1) + z)

'''
for j in range(6):
    for i in range(50):
        minX, minY, maxX,maxY = bounds[j]


        #RIGHT
        p = (minX+i, maxY-1, 0, j)
        np = move(p)
        print("RIGHT",p,np)

        #DOWN
        p = (maxX-1, minY+i, 1, j)
        np = move(p)
        print("DOWN", p,np, end="")

        #LEFT
        p = (minX+i, minY, 2, j)
        np = move(p)
        print("LEFT",p,np, end="")
        
        #UP
        p = (minX, minY+i, 3, j)
        np = move(p)
        print("UP", p,np, end="")
'''