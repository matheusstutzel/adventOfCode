import sys
from collections import deque

def isComplete(x):
    r = x
    for i in x:
        r = r.intersection(edges[i])
    return len(r)==len(x)

def back(opt, x=set()):
    #print("back",x,opt)
    if len(opt) == 0:
        if isComplete(x):
            return x
        else:
            return set()
    local = opt.copy()
    hd = set([local.pop()])

    consider = back(local,x.union(hd))
    discard = back(local,x)
    if len(consider)>len(discard):
        return consider
    return discard
    
edges={}

for l in sys.stdin:
    a,b = l.strip().split("-")
    if a not in edges:
        edges[a]=set([a])
    edges[a].add(b)
    
    if b not in edges:
        edges[b]=set([b])
    edges[b].add(a)

selected = set()
for i in edges:
    current = back(edges[i])
    if len(current)>len(selected):
        selected = current
    print(i)


print(sorted(selected))
print(max([len(edges[i]) for i in edges]))
