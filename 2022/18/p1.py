import sys

p = [[int(k) for k in l.strip().split(",")] for l in sys.stdin]

m=[]
size = 100
for i in range(size):
    m.append([])
    for j in range(size):
        m[i].append([False]*size)
        

for pt in p:
    x,y,z = pt
    m[x][y][z]=True

sides = [
    [0,0,-1], #up
    [0,0,1], #down
    [-1,0,0], #left
    [1,0,0],
    [0,1,0],
    [0,-1,0]
]
total = 0 
for pt in p:
    x,y,z = pt
    for side in sides:
        mx,my,mz = side
        if(not m[x+mx][y+my][z+mz]):
            total = total+1
print(total)
                