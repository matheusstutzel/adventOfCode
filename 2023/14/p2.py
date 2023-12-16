import sys

def points(mat, rowSize):
    total = 0
    for i in range(rowSize):
        p = rowSize-i
        for j in range(rowSize):
            c = mat[i*rowSize + j]
            if c == 'O':
                total = total + p
    return total

def tiltV(mat, dx):
    if dx>0:
        mat.reverse()
    for i, l in enumerate(mat):
        for j, c in enumerate(l):
            if c == 'O':
                k = i-1 
                while k>=0:
                    w = mat[k][j]
                    if w == '#' or w =='O':
                        k = k +1
                        break
                    k = k-1
                k = max(k,0)
                mat[i][j]='.'
                mat[k][j]='O'
    
    if dx>0:
        mat.reverse()
    return mat

def tiltH(mat, dy):
    for i, l in enumerate(mat):
        if dy>0:
            l.reverse()
        for j, c in enumerate(l):
            if c == 'O':
                k = j-1 
                while k>=0:
                    w = mat[i][k]
                    if w == '#' or w =='O':
                        k = k +1
                        break
                    k = k-1
                k = max(k,0)
                mat[i][j]='.'
                mat[i][k]='O'
        if dy>0:
            l.reverse()
    return mat
def cycle(mat):
    mat = tiltV(mat, -1)
    mat = tiltH(mat, -1)
    mat = tiltV(mat, 1)
    mat = tiltH(mat, 1)
    return mat

def process(mat, target):
    hist = []
    i = 0
    while i < target:
        i = i +1 
        mat = cycle(mat)

        mnow = "".join(["".join(q) for q in mat])
        if(mnow in hist):
            first = hist.index(mnow)
            c = i-first
            f = (target - first)%c+first
            return hist[f-1]
        hist.append(mnow)
    return "".join(["".join(q) for q in mat])

mat = [[*l.strip()] for l in sys.stdin]
rowSize = len(mat)
mat = process(mat, 1000000000)
total = points(mat, rowSize)
print(total)