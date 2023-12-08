import sys
from  math import lcm

input = [l.strip() for l in sys.stdin]

ins = input[0]

graph = {}

nodes = set()
for i in input[2:]:
    source, aux = i.split(" = ")
    l,r = aux[1:-1].split(", ")
    graph[source] = (l,r)
    if source.endswith('A'):
        nodes.add(source)


def size(node):
    i = 0 
    count = 0 
    while not node.endswith('Z'):
        node = graph[node][0 if ins[i]=='L' else 1]
        i = (i +1)%len(ins)
        count = count +1
    return count


cycles = []
for n in nodes:
    print(n)
    cycles.append(size(n))
    print(cycles)
print(lcm(*cycles))