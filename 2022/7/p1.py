import sys

root = {"/":{}}

c = [root]

mode = 0
for line in sys.stdin:
    l = line.rstrip().split(" ")
    if(l[0]=="$"):
        if(l[1] == "cd"):
            if(l[2]==".."):
                c.pop()
            else:
                c.append(c[-1][l[2]])
            print("cd",c)
        elif(l[1] == "ls"):
            print("ls")
            continue
    else:
        if(l[0]=="dir"):
            c[-1][l[1]]={}
            print("add dir", c)
        else:
            c[-1][l[1]]=int(l[0])
            print("add file", c)
    print("")

count = 0

def size(node):
    global count
    local = 0
    for k in node:
        print("k:",k, node[k], "is", isinstance(node[k],int))
        if(isinstance(node[k], int)):
            local = local + node[k]
        else:
            local = local + size(node[k])
    if(local<100000):
        count = count + local
    return local
print(root)
size(root["/"])
print(count)