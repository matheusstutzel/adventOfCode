import sys

l =[]
c = 0

for line in sys.stdin:
    l.append(int(line.rstrip()))
    if len(l) == 4:
        if l[0] < l[3]:
            c = c+1
        l.pop(0)
print(c)
