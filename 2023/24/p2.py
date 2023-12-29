import sys
#https://semath.info/src/inverse-cofactor-ex4.html

def createMat(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def createSub(mat, ignoreI, ignoreJ):
    #ideally this would not copy the data 🤷
    nmat = []
    for i in range(len(mat)):
        if i == ignoreI:
            continue
        nmat.append([])
        for j in range(len(mat[i])):
            if j == ignoreJ:
                continue
            nmat[-1].append(mat[i][j])
    return nmat


def scalarProd(factor, mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat[i][j]*=factor
    return mat

def det(mat):
    #assuming it is sizeXsize
    size = len(mat)
    if size == 2:
        return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]

    factor = 1
    result =0 
    for i in range(size):
        result+= factor * mat[i][0] * det(createSub(mat, i,0))
        factor*=-1
    return result

def adjugate(mat):
    size = len(mat)
    result = createMat(size,size)
    for i in range(size):
        for j in range(size):
            factor = 1 if (i+j)%2==0 else -1
            #this is not a typo, for Aij = factor * det(Mji)
            result[i][j] = factor * det(createSub(mat, j,i))
    return result
    
def inverse(mat):
    #https://semath.info/src/inverse-cofactor-ex4.html
    d = det(mat)
    #print(d)
    factor = 1/d
    #print(factor)
    adj = adjugate(mat)
    #printa(adj)
    return scalarProd(factor, adj)

def prod(a,b):
    if(len(a[0])!=len(b)):
        raise Exception("cannot multiply mat %dX%d with mat %dX%d"%(len(a),len(a[0]), len(b), len(b[0])))
    rows = len(a)
    cols = len(b[0])
    c = createMat(rows, cols)
    common = len(b)
    for i in range(rows):
        for j in range(cols):
            for k in range(common):
                c[i][j]+=a[i][k]*b[k][j]
    return c


entries = []
for l in sys.stdin:
    a, b = l.strip().split(" @ ")
    convert = lambda x: [ int(y) for y in x.replace(",", "").split()]
    # sx,sy,sz | dx,dy,dz 
    entries.append((convert(a), convert(b)))

# consider that each hailstone is going towards the desired point
# so each sx,sy,sz | dx,dy,dz  becomes sx-a,sy-b,sz-c | dx-d,dy-e,dz-f
# since we know that at some point they should colide, we can use x=0, y=0, z=0 to create some equations
#  (sx-a) + (dx-d)T = 0
#  (sy-b) + (dy-e)T = 0
#  (sz-c) + (dz-f)T = 0  => can be ignored 
# using the first two we have:
# (sx-a)/(dx-d) = (sy-b)/(dy-e)   => (sx-a)(dy-e) -(dx-d)*(sy-b) = 0  (I)
# Choose two entries (sx1,sy1,sz1 | dx1,dy1,dz1) and (sx2,sy2,sz2 | dx2,dy2,dz2)
# and do (I1)-(I2) and after some manipulation you get:
# (dy2 - dy1)*a + (dx1-dx2)*b + (sy1-sy2)*d + (sx2-sx1)*e = (dx1*sy1 - dx2*sy2 + sx2*dy2 -sx1*dy1)
# so... α*a + β*b + γ*d + δ*e = ε
# using 4 equations like this (4 combinations of entries) we can have:
# so... [[α0,β0,γ0,δ0],[α1,β1,γ1,δ1],[α2,β2,γ2,δ2],[α3,β3,γ3,δ3]] * [[a],[b],[d],[e]] = [[ε0],[ε1],[ε2],[ε3]]
# we can write it as A*x=b   => x = A^-1 *B

A = []
B = []

for j in range(1,5) :
    [[sx1,sy1,sz1],[dx1,dy1,dz1 ]] = entries[0]
    [[sx2,sy2,sz2],[dx2,dy2,dz2 ]] = entries[j]

    A.append([(dy2-dy1), (dx1-dx2), (sy1-sy2), (sx2-sx1)])
    B.append([(dx1*sy1 - dx2*sy2 + sx2*dy2 -sx1*dy1)])
AI = inverse(A)
X = prod(AI, B)
[[a],[b],[d],[e]] = X

[[sx1,sy1,sz1],[dx1,dy1,dz1 ]] = entries[0]
[[sx2,sy2,sz2],[dx2,dy2,dz2 ]] = entries[1]

t1 = (a - sx1) / (dx1 - d)
t2 = (a - sx2) / (dx2 - d)

f = ((sz1 - sz2) + t1 * dz1 - t2 * dz2) / (t1 - t2)
c = sz1 + t1 * (dz1 - f)

print(a + b + c)