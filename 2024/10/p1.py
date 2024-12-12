import sys

alternatives={
    (-1,0),
    (0,1),
    (1,0),
    (0,-1)
}

def dfs(mat, i,j,t, prev=-1):
    #print("dfs", i,j,prev)
    if i<0 or i>=len(mat) or j<0 or j>=len(mat[i]):
        return set()
    v = mat[i][j]
    if v!= prev+1:
        return set()
    if v == t:
        return {(i,j)}
    r = set()
    for a in alternatives:
       r=r.union(dfs(mat,i+a[0], j+a[1], t,v))
    return r

mat = [[int(x) for x in l.strip()] for l in sys.stdin]
#print(mat)
s = 0
for i in range(len(mat)):
    for j in range(len(mat[i])):
        if mat[i][j]==0:
            #print("call ",i,j)
            r=dfs(mat, i,j,9)    
            #print("r",r)
            s+=len(r)
print(s)
