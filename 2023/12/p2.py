import sys
from collections import deque


cases = [l.strip().split() for l in sys.stdin]

def points(line):
    current =0 
    actual = []
    for c in line:
        if c == '.' and current>0:
            actual.append(current)
            current = 0
        if c == '#':
            current = current +1 
    if current>0:
        actual.append(current)
    return actual

def simplify(line):
    
    ## .....#.... == .#.  
    # #....# == #.#
    s = []
    prev = ''
    for i,c in enumerate(line):
        skip = c =='.' and prev == '.'
        prev = c
        if skip:
            continue            
        s.append(c)
    return s


mem={}
def back(l, k):
    l = simplify(l)
    s = "".join(l)
    if s not in mem:
        mem[s] = doBack(l,k)
    return mem[s]



def doBack(line, expected):
    if '?' not in line:
        p = points(line)
        if p == expected:
            #print("right", "".join(line), expected)
            return 1
        else:
            return 0
        
    i = line.index('?')
    p = points(line[:i])

    if p[:-1] != expected[:max(0,len(p)-1)] or (len(p)>0 and p[-1]> expected[min(max(len(p)-1, 0), len(expected)-1)]):
        #print("prune", "".join(line), "\n",p[:-1], expected[:max(0,len(p)-1)])
        return 0
    line[i] = '#'
    a = back(simplify(line), expected)
    line[i] = '.'
    b = back(simplify(line), expected)    
    line[i] = '?'
    return a+b

    

result = 0 
for idx, i in enumerate(cases):
    mem = {}
    line = [*'?'.join([i[0]]*5)]
    expected = [ int(x) for x in i[1].split(',')]*5
    #print("".join(line), expected)
    count = back(line, expected)
    #print("".join(line), expected, count)
    result = result +  count
    
print(result)
