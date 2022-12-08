import sys


def dfs(node, out):
    if isinstance(node, int):
        return node
    size = sum ( dfs(k, out) for k in node.values())
    out.append(size)
    return size

root = {"/":{}}

c = [root]

for line in sys.stdin:
    l = line.rstrip().split(" ")
    if(l[0]=="$"):
        if(l[1] == "cd"):
            if(l[2]==".."):
                c.pop()
            else:
                c.append(c[-1][l[2]])
        elif(l[1] == "ls"):
            continue
    else:
        if(l[0]=="dir"):
            c[-1][l[1]]={}
        else:
            c[-1][l[1]]=int(l[0])


sizes = []
totalSize = dfs(root["/"], sizes)


total = 3e7-(7e7 - totalSize)

p1 = sum([i for i in sizes if i<=1e5])
p2 = min([i for i in sizes if i>=total])
print("p1: ",p1, " p2:",p2)
