import sys

mat = [[*l.strip()] for l in sys.stdin]

for i, l in enumerate(mat):
    print(i,l)
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
print("")
total = 0
for i, l in enumerate(mat):
    p = len(l)-i
    print(p,l)
    for c in l:
        if c == 'O':
            total = total + p
print(total)