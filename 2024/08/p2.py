import sys


def valid(x, mat):
    return x[0]>=0 and x[0]<len(mat) and x[1]>=0 and x[1]<len(mat[x[0]])
mat=[l.strip() for l in sys.stdin]


antennas={}
for i in range(len(mat)):
    for j in range(len(mat[i])):
        v = mat[i][j]
        if v!='.':
            if v not in antennas:
                antennas[v]=[]
            antennas[v].append((i,j))
antinodes=set()
for k,v in antennas.items():
    for a in v:
        for b in v:
            if a==b:
                continue
            dx=a[0]-b[0]
            dy=a[1]-b[1]

            nx=b[0]
            ny=b[1]
            while valid((nx,ny),mat):
                antinodes.add((nx,ny))            
                nx=nx-dx
                ny=ny-dy
                
print(len(antinodes))
