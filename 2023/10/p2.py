import sys
from math import ceil
from collections import deque

mat = [[*l.strip()] for l in sys.stdin]

dir = {
    '|':[(-1,0), (1,0)],
    '-':[(0,-1), (0,1)],
    'L':[(-1,0), (0,1)],
    'J':[(-1,0), (0,-1)],
    '7':[(1,0), (0,-1)],
    'F':[(1,0), (0,1)],
    'S':[(-1,0),(0,-1),(0,1),(1,0)],
    '.':[],
}

def neighbors(x,y, flood = False):
    opt = dir[mat[x][y]] if not flood else dir['S']
    for i,j in opt:
        a = i + x
        b = j + y
        if a<0 or a>=len(mat):
            continue
        if b<0 or b>=len(mat[a]):
            continue
        dot = mat[a][b] == '.'
        if flood != dot:
            continue
        yield (a,b)


def flood(start):
    q = deque([start]) #queue
    round = 0
    s = set() #seen
    while q:    
        for _ in range(len(q)): #all in this depth
            p = q.popleft()
            
            if mat[p[0]][p[1]] != '.':
                continue
            mat[p[0]][p[1]] = '@'

            for u in neighbors(*p, True):
                if u not in s:
                    s.add(u)
                    q.append(u)
        round = round+1 
    return round
def next (c,p):
    for n in neighbors(*c):
        if c == p and c not in neighbors(*n):
            # start and we are not sure what direction to take
            continue
        if n == p:
            continue
        return n

start = (0,0)
for i, l in enumerate(mat):
    for j, c in enumerate(l):
        if c == 'S':
            start = (i,j)


cycle = set()
c = start
prev = start
depth = 0
while c == prev or c!=start:
    cycle.add(c)
    n = next(c,prev)
    #print(c, prev, n)
    prev, c = c, n
    depth = depth + 1

# clear junk
for i, l in enumerate(mat):
    for j, c in enumerate(l):
        if (i,j) in cycle:
            continue
        mat[i][j] = '.'
    #print(''.join(l))
#print("")


for i in range(len(mat)):
    flood((i,0))
    flood((i, len(mat[i])-1))

'''
for i, l in enumerate(mat):        
    print(''.join(l))

print("")
'''

count = 0
for i, l in enumerate(mat): 
    out = True
    semi = ''
    for j, c in enumerate(l):       
        if not out and c == '.':
            count= count +1 
            mat[i][j]='$'
        if c == '|' or (c == semi or (len(semi)>0 and c =='S')):
            out = not out
        if c == 'L':
            semi = '7'
        elif c == 'F':
            semi = 'J'            
        elif c != '-':
            semi = ''
        q = (2 if out else 0) + (1 if len(semi)>0 else 0)
        #print(c, q, end = '')
    #print("")
     
'''
for i, l in enumerate(mat):        
    print(''.join(l))

'''
print(count)