import sys

input = [l.strip() for l in sys.stdin]

ins = input[0]

graph = {}

for i in input[2:]:
    source, aux = i.split(" = ")
    l,r = aux[1:-1].split(", ")
    graph[source] = (l,r)

node = 'AAA'
i = 0 
count = 0 
while node != 'ZZZ':
    node = graph[node][0 if ins[i]=='L' else 1]
    i = (i +1)%len(ins)
    count = count +1
print(count)