import sys

l =[]
c = 0

for line in sys.stdin:
    l.append(int(line.rstrip()))
    if len(l) == 2:
        if l[0] < l[1]:
            c = c+1
        l.pop(0)
print(c)
