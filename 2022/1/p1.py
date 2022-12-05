import sys

## elfs
l =[0]
## max
m = 0

## index 
i=0

for line in sys.stdin:
    line = line.rstrip()
    if(line == ""):
        i = i + 1
        l.append(0)
    else:
        l[i] = l[i] + int(line)
        m = max(m, l[i])
print(m)
