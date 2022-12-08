import sys

def process(i,j,mat,a,b):
    c = 0
    s = len(mat)
    for k in range(1,s ):
        ni = i+ (a*k)
        nj = j + (b*k)
        if((ni)>=s or nj>=s or ni<0 or nj<0):
            break
        c = c +1
        if(mat[ni][nj]['v']>=mat[i][j]['v']):
            break
    return c 
mat = []
for line in sys.stdin:
    mat.append([{'v':int(i)} for i in line.rstrip()])

for i in range(len(mat)):
    for j in range(len(mat)): # assuming square matrix
        #down
        a = process(i,j,mat, 1,0)
        #up
        b = process(i,j,mat, -1,0)
        #right
        c = process(i,j,mat, 0,1)
        #left
        d = process(i,j,mat, 0,-1)      
        mat[i][j]['k'] = a*b*c*d


mmax = 0
for i in range(len(mat)):
    for j in range(len(mat)):
        print(mat[i][j]['v'], mat[i][j]['k'], end=" ")
        mmax = max(mmax,  mat[i][j]['k'])
    print("")

print(mmax)