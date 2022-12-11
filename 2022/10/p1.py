import sys
size = 300
cycle = [1]*size


input = [i.rstrip() for i in sys.stdin]

i = 1

for l in input:
    if(l[0] == 'n'):
        i=i+1
        cycle[i]=cycle[i-1]
    else:
        i=i+2
        cycle[i-1] = cycle[i-2]
        cycle[i] = cycle[i-1] + int(l.split(" ")[1])
    print(l.split(" ")[0], cycle[max(0,i-5):i+1], i )
for t in range(i+1, size):
    cycle[t]=cycle[t-1]

print(cycle[:21])
r = 0
for i in range(6):
    r = r + cycle[20+ 40*i]*(20+40*i)
print(r)