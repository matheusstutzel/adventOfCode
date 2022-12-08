import sys

def process(i,j,mat,ref):
    mat[i][j]["visible"] = mat[i][j]["visible"] or mat[i][j]['v']>ref
    return max(mat[i][j]['v'],ref)

mat = []
for line in sys.stdin:
    mat.append([{'v':int(i), 'visible':False} for i in line.rstrip()])

for i in range(len(mat)):
    a=b=c=d=-1
    for j in range(len(mat)): # assuming square matrix
        # left right
        a = process(i,j,mat,a)
        # right left
        b = process(i,-j-1,mat,b)        
        # top down
        c = process(j,i,mat,c)        
        # bottom up 
        d = process(-j-1,i,mat,d)

count = 0
for i in range(len(mat)):
    for j in range(len(mat)):
        print(mat[i][j]['v'], "t" if mat[i][j]['visible'] else "f", end=" ")
        count = count + (1 if mat[i][j]['visible'] else 0)
    print("")

print(count)