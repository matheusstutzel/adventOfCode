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

def look(i,j,mat, delta, wish):
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
    return look(i+delta[0], j+delta[1], mat, delta, wish[1:])

def test(i,j,mat):
    count=0
    for d in alternatives:
        if look(i,j,mat,d, ['X','M','A','S']):
            count+=1
    return count


mat = [l.strip() for l in sys.stdin]
print(mat)
count = 0
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j]=='X':
            count+=test(i,j,mat)
print(count)
            
