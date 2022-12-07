import sys
from collections import deque as dq


#[S] [J] [S] [T] [T] [M] [D] [B] [H]
# 1   2   3   4   5   6   7   8   9
# 1   5   9   13  17  21  25  29  33 (chart at... => i)
# crane[i//4 +1]

def readCranes(cranes, l):
    for i, c in enumerate(l):
        if(c >= 'A' and c <= 'Z'):
            cranes[i//4 + 1].appendleft(c)


def readMoves(cranes, l):
    p = l.split(" ")
    i = int(p[1])
    f = int(p[3])
    t = int(p[5])
    for k in range(i):
        cranes[t].append(cranes[f].pop())


cranes = []
for i in range(10):
    cranes.append(dq())

mode = 0
# reading input
for line in sys.stdin:
    # reading cranes
    l = line.rstrip()
    if(mode == 1):
        mode = 2
        continue
    if(l[1] == '1'):
        mode = 1
        continue
    if mode == 0:
        readCranes(cranes, l)
    else:
        readMoves(cranes, l)

print(cranes)
for c in cranes:
    print(c[-1] if c else '')
