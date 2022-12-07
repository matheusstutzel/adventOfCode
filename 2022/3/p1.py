import sys


def value(c):
    print("value of " + c )
    v = ord(c)
    if(v>90):
        return v - ord('a') + 1 
    else:
        return v - ord('A') + 27

c = set()
v = set()
t = 0

# reading input
for line in sys.stdin:
    l = line.rstrip()
    size = len(l)
    for i in range(size//2):
        c.add(l[i])
    for i in range(size//2, size):
        if(l[i] in c and l[i] not in v):
            v.add(l[i])
            t = t + value(l[i])
    c = set()
    v = set()
    print("")

print(t)
