import sys
from collections import deque


def extractNode(l):
    #Valve JJ has flow rate=21; tunnel leads to valve II
    s = l.split(" ")
    id = s[1]
    rate = int(s[4].split("=")[1][:-1])
    links = [i.strip() for i in " ".join(s[9:]).split(",")]
    return id,rate,links

def bfs(g,v,t): #graph, value, targets
    d = {v:0} #dist
    s = {v} #seen
    q = deque([v]) #queue
    while q and any(k not in d for k in t):
        p = q.popleft()
        for u in g[p]:
            if u not in s:
                s.add(u)
                d[u] = d[p]+1
                q.append(u)
    return d


def dfs(v, dist, rates, time, p = []):
    p = p+[v]
    if(time<=0 or len(p)==len(rates)):
        return 0
    tot = 0
    for n,d in dist[v].items():
        if d>time-2 or n in p:
            continue
        nt = time-d-1
        tot = max(tot, dfs(n,dist, rates, nt, p)+rates[n]*(nt))
    return tot

def find_paths(dist, rates, t): # dist, rates, max time
    pressures = []
    paths = []
    stack = [(t, 0, ['AA'])] #current time, pressure, path
    while stack:
        t, p, path = stack.pop()
        cur = path[-1]
        new = [] #new paths from here
        for n, d in dist[cur].items(): #neighbor, distance
            if d > t - 2 or n in path: # can I reach? or Did I pass there already? 
                continue
            tt = t - d - 1 #total time = time - distance -1 (turn the valve on)
            pp = p + rates[n] * tt #pressure = current pressure + preasure release by n valve
            s = tt, pp, path + [n] # include n into path 
            new.append(s) # and this new  to new paths
        if new:
            stack.extend(new)
        else:
            pressures.append(p)
            # paths always start at AA, so no need to keep first location
            paths.append(path[1:])
    return pressures, paths


rates = {}
links = {}
for l in sys.stdin:
    id, rate, link = extractNode(l)
    if(rate>0):
        rates[id]= rate
    links[id] = link

dist = {}
for v in ('AA', *rates):
    dist[v]={}
    d = bfs(links, v, rates)
    for r in rates:
        if r!= v and r in d:
            dist[v][r]=d[r]
print(dist)

p, _ = find_paths(dist, rates, 30)
print(max(p))





print(dfs("AA",dist, rates, 30))