import sys
from collections import deque


cases = [l.strip().split() for l in sys.stdin]

def valid(line, expected):
    current =0 
    actual = []
    for c in line:
        if (c == '.' or c == '?') and current>0:
            actual.append(current)
            current = 0
        if c == '#':
            current = current +1 
    if current>0:
        actual.append(current)
    return actual ==expected

def back(line, expected):
    if '?' not in line:
        return 1 if valid(line, expected) else 0
    i = line.index('?')
    line[i] = '#'
    a = back(line, expected)
    line[i] = '.'
    b = back(line, expected)    
    line[i] = '?'
    return a+b

    

result = 0 
for i in cases:
    line = [*i[0]]
    expected = [ int(x) for x in i[1].split(',')]
    count = back(line, expected)
    #print(line, expected, count)
    result = result +  count
print(result)
