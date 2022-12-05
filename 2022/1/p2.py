import heapq as hq
import sys

## elfs
l =[0]
## max
m = 0

k = 3 
minHeap = []
## index 
i=0

for line in sys.stdin:
    line = line.rstrip()
    if(line == ""):
        hq.heappush(minHeap, l[i])
        if(i>=k):
            hq.heappop(minHeap)
        i = i + 1
        l.append(0)
    else:
        l[i] = l[i] + int(line)

hq.heappush(minHeap, l[i])
if(i>=k):
    hq.heappop(minHeap)

sum = 0
for v in minHeap:
    sum = sum + v
print(sum)
