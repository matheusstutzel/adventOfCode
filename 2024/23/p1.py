import sys

def containsT(i,j,k):
    return i.startswith('t') or j.startswith('t') or k.startswith('t')
edges={}

for l in sys.stdin:
    a,b = l.strip().split("-")
    if a not in edges:
        edges[a]=set()
    edges[a].add(b)
    
    if b not in edges:
        edges[b]=set()
    edges[b].add(a)

three = set()

for i in edges:
    for j in edges[i]:
        for k in edges[j]:
            if k in edges[i] and containsT(i,j,k):
                three.add(tuple(sorted([i,j,k])))
print(len(three))        
