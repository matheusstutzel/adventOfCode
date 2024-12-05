import sys


alternatives = [
    (-1,-1),
    (-1,0),
    (-1,1),
    (0,-1),
    (0,1),
    (1,0),
    (1,-1),
    (1,1)
]

def look(i,j,mat,wish):
    #print("look", i,j,delta, wish)
    if len(wish)==0:
        #print("true len")
        return True
    if i<0 or i>=len(mat):
        #print('i')
        return False
    if j<0 or j>=len(mat[i]):
        #print('j')
        return False
    if mat[i][j]!=wish[0]:
        #print('wish', wish, mat[i][j])
        return False
    return True

def diag(i,j,a,b,mat):
    return look(i+a[0], j+a[1], mat, "M") and look(i+b[0], j+b[1], mat, "S")

def test(i,j,mat):
    if (diag(i,j,(-1,-1),(+1,+1), mat) or diag(i,j,(+1,+1),(-1,-1),mat)) and (diag(i,j,(-1,+1), (+1,-1), mat) or diag(i,j, (+1,-1), (-1,+1),mat)):
        return 1
    return 0

mat = [l.strip() for l in sys.stdin]
#print(mat)
count = 0
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j]=='A':
            count+=test(i,j,mat)
print(count)
            
