import sys
from collections import deque
from math import prod
def maxPos(current, times):
    x = current
    y = current+times
    return y*(y-1)/2 - x*(x-1)/2
def convert(l):
    p = l.split(" ")
    id = int(p[1][:-1])
    oreOreCost= int(p[6])
    clayOreCost= int(p[12])
    obOreCost= int(p[18])
    obClayCost= int(p[21])
    GeodeOreCost= int(p[27])
    GeodeObCost= int(p[30])
    return (id, oreOreCost, clayOreCost, obOreCost, obClayCost, GeodeOreCost, GeodeObCost)

def process(id, oreOreCost, clayOreCost, obOreCost, obClayCost, GeodeOreCost, GeodeObCost, MAX):
    types = [       
            [oreOreCost, 0,0,0],
            [clayOreCost, 0,0,0],
            [obOreCost, obClayCost,0,0],
            [GeodeOreCost,0,GeodeObCost,0]        
    ]
    limit = [   max([types[k][i] for k in range(4)])*2 for i in range(4)]
    limit[3]=999999999999

    resource = (0,0,0,0) #ore, clay,ob,geode
    robot = (1,0,0,0) #ore, clay,ob,geode
    result = 0

    seen = set((resource, robot))
    q = deque([(resource,robot)])
    round = 0
    while q:
        for _ in range(len(q)):
            p = q.popleft()
            resource, robot = p
            result = max(result, resource[3])

            if(result > resource[3] + maxPos(robot[3], MAX-round)):
                continue
            #if(len(q) %100000 < 10 or round>=MAX):
            #    print(id, len(q), round, len(seen), p)
            
            if round >= MAX:
                continue

            newResource = tuple([r + robot[idx] for idx,r in enumerate(resource)])
            if(all([resource[i]>=types[3][i] for i in range(4)])):
                nnR = tuple([newResource[i] - types[3][i] for i in range(4)])
                nR = tuple([robot[i] +(+1 if 3==i else 0) for i in range(4)])
                v = (nnR, nR)
                if v not in seen:
                    seen.add(v)
                    q.append(v)
            else:
                v = (newResource,robot)
                if(v not in seen):
                    seen.add(v)
                    q.append(v)
                for idx,cost in enumerate(types):
                    canCreate = all([resource[i]>=cost[i] for i in range(4)])
                    if not canCreate or idx==3:
                        continue
                    if(robot[idx]>limit[idx]):
                        continue
                    nnR = tuple([min(limit[i], newResource[i] - cost[i]) for i in range(4)])
                    nR = tuple([robot[i] +(1 if idx==i else 0) for i in range(4)])
                    v = (nnR,nR)
                    if(v not in seen):
                        seen.add(v)
                        q.append(v)
        round = round +1
    return result

MAX = 24

bp = [convert(l.strip()) for l in sys.stdin]
result = ([process(*b, MAX) for b in bp])
print(result)
print(sum([r*(idx+1) for idx,r in enumerate(result)]))