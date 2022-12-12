import sys

prints = False

size = 300
cycle = [1]*size
i = 1

for l in [i.rstrip() for i in sys.stdin]:
    i=i+1
    cycle[i]=cycle[i-1]
    if(l[0] == 'a'):
        i=i+1
        cycle[i] = cycle[i-1] + int(l.split(" ")[1])
    if prints:
        print(l.split(" ")[0], cycle[max(0,i-5):i+1], i )

for t in range(i+1, size):
    cycle[t]=cycle[t-1]

r = 0
for i in range(6):
    r = r + cycle[20+ 40*i]*(20+40*i)
print(r)