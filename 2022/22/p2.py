import sys

'''
 12
 3
45
6
'''


def notAlowed():
    raise RuntimeError()


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

calcMovement = {
    RIGHT: {
        RIGHT: lambda x, y: (0, 0),
        DOWN:  lambda x, y: notAlowed(),
        LEFT:  lambda x, y: notAlowed(),
        UP:    lambda x,y: notAlowed()
        },
    DOWN: {
        RIGHT: lambda x, y: notAlowed,
        DOWN:  lambda x, y: (0, 0),
        LEFT:  lambda x, y: notAlowed(),
        UP:    lambda x,y: notAlowed()
        },
    LEFT: {
        RIGHT: lambda x, y: notAlowed(),
        DOWN:  lambda x, y: notAlowed(),
        LEFT:  lambda x, y: (0, 0),
        UP:    lambda x,y: notAlowed()
        },
    UP: {
        RIGHT: lambda x, y: notAlowed(),
        DOWN:  lambda x, y: notAlowed(),
        LEFT:  lambda x, y: notAlowed(),
        UP:    lambda x,y: (0, 0)
        }
}

# From bound X (index) to RIGHT,DOWN, LEFT, UP
# it should add this displacement, and this is the new dir
boundMovements = [
    {
        RIGHT: ((0, 0), RIGHT),  # 1 to 2
        DOWN: ((0, 0), DOWN),  # 1 to 3
        LEFT: ((-49, 100), RIGHT),  # 1 to 4
        UP: ((151, -50), RIGHT),  # 1 to 6
    },
    {
        RIGHT: ((100, -101), LEFT),  # 2 to 5
        DOWN: ((0, -50), LEFT),  # 2 to 3
        LEFT: ((0, 0), LEFT),  # 2 to 1
        UP: ((151, -100), UP),  # 2 to 6
    },
    {
        RIGHT: ((-49, 0), UP),  # 3 to 2
        DOWN: ((0, 0), DOWN),  # 3 to 5
        LEFT: ((50, 0), DOWN),  # 3 to 4
        UP: ((151, -50), RIGHT),  # 3 to 6
    },
    {
        RIGHT: ((-49, 0), UP),  # 4 to 4
        DOWN: ((0, 0), DOWN),  # 4 to 3
        LEFT: ((0, 0), RIGHT),  # 4 to 2
        UP: ((151, -50), RIGHT),  # 4 to 6
    },
    {
        RIGHT: ((0, 0), RIGHT),  # 5 to 2
        DOWN: ((0, 0), DOWN),  # 5 to 3
        LEFT: ((-49, 100), RIGHT),  # 5 to 4
        UP: ((151, -50), RIGHT),  # 5 to 6
    },
    {
        RIGHT: ((0, 0), RIGHT),  # 6 to 2
        DOWN: ((0, 0), DOWN),  # 6 to 3
        LEFT: ((-49, 100), RIGHT),  # 6 to 4
        UP: ((151, -50), RIGHT),  # 6 to 6
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
    if not isinstance(ins, int):
        increment = 1 if ins == 'R' else -1
        return (point[0], point[1], (point[2]+increment) % 4)
    x, y, z = point
    mov = movement[z]
    for _ in range(ins):
        x2, y2 = move(x, y, *mov)
        if(x == x2 and y == y2):
            break
        x = x2
        y = y2
    return (x, y, z)


def move(x, y, dx, dy):
    nx = x
    ny = y
    while True:
        nx = (nx+dx) % rows
        ny = (ny+dy) % cols
        if(ny >= len(mat[nx])):
            continue
        v = mat[nx][ny]
        if v == '.':
            return nx, ny
        elif v == '#':
            return x, y


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

point = (x, y, 0)  # x,y, movement index/ RIGHT

for ins in instructions():
    point = apply(point, ins)

print(point)
x, y, z = point

print(1000*(x+1) + 4*(y+1) + z)
