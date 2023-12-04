import sys

def neighbors(x,y):
    for i in [-1,0,1]:
        a = x+i
        if a<0 or a>=len(mat):
            continue
        for j in [-1,0,1]:
            b = y+j
            if b<0 or b>=len(mat[a]):
                continue
            if i == 0 and j == 0:
                continue
            yield mat[a][b]
def isValidChar(c):
    return c!='.' and (ord(c)-ord('0')<0 or ord(c)-ord('9')>0)

def isValidPos(old, i,j):
    if old:
        return old
    return any([isValidChar(c) for c in neighbors(i,j)])

mat = [l.strip() for l in sys.stdin]
#print(mat)

num = False
valid = False

acc = []
den = []

current = 0
for i, l in enumerate(mat):
    for j, c in enumerate(l):
        if num:
            if c.isnumeric():
                current = current*10 + int(c) 
                valid = isValidPos(valid, i, j)
            else:
                if valid:
                    acc.append(current)
                else:
                    den.append(current)
                num = False
                valid = False
        else:
            if c.isnumeric():
                num = True
                current = int(c)
                valid = isValidPos(valid, i, j)
        #print(i, l, j, c)
print(sum(acc))
#print(den)