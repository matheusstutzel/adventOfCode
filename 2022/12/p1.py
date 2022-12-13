import sys

def convert(x):
    if x == "S":
        return "a"
    if x == "E":
        return "z"
    return x
def check(a,b):
    a = ord(convert(a))
    b = ord(convert(b))
    return b<=(a+1)
def dijkstra(start, mat, cost):
    q = []
    cost[start] = 0 
    q.append((start, 0))
    while len(q)>0:
        n,c = q.pop() #node, cost
        if cost[n] != c:
            continue #already found a better path for n
        for v in mat[n]:
            if(cost[v] > (c+1)):
                cost[v]=c+1
                q.append((v,c+1))




l = [l.rstrip() for l in sys.stdin]

lines = len(l)
cols = len(l[0])


mat = []
for i in range(lines):
    for j in range(cols):
        pos = j + i*cols
        v = l[i][j]
        if(v=="S"):
            start = pos
        if(l[i][j]=="E"):
            end = pos
        adj = []
        #top
        if(i>0 and check(v, l[i-1][j])):
            adj.append(j + (i-1)*cols)
        #left
        if(j>0 and check(v, l[i][j-1])):
            adj.append(j-1+i*cols)
        #down
        if(i+1<lines and check(v, l[i+1][j])):
            adj.append(j+(i+1)*cols)
        #right
        if(j+1<cols and check(v, l[i][j+1])):
            adj.append(j+1+i*cols)

        mat.append(adj)

cost = [999] * (lines * cols)
dijkstra(start, mat, cost)

#for i in range(lines):
#    for j in range(cols):
#        print("%03d%s"%(cost[ j + i*cols], l[i][j]), end=" ")
#    print("") 
print(cost[end])
