import sys

def outboundLen(g,s, v):
    return len(g[v]-s)
def outboundEdges(g,s):
    total = 0
    for v in s:
        total+= outboundLen(g,s,v)
    return total
def maxOutboundConnected(g,s):
    resp = next(iter(s))
    for i in s:
        if outboundLen(g,s,i)>outboundLen(g,s,resp):
            resp = i
    return resp

g ={}
for l in sys.stdin:
    v,e = l.split(':')
    e = set(e.split())
    for i in e:
        if i not in g:
            g[i] = set()
        g[i].add(v)
        if v not in g:
            g[v] = set()
        g[v].add(i)

s = set(g)
while outboundEdges(g, s) != 3:
    s.remove(maxOutboundConnected(g,s))
print(len(s) * len(set(g)-s))