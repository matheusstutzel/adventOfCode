import sys
import math

lines = [l.split(":")[1].strip() for l in sys.stdin]
time = [int(x) for x in lines[0].split()]
distance = [int(x) for x in lines[1].split()]

result = 1
for i in range(len(time)):
    b = time[i]
    c = distance[i]
    
    delta = math.sqrt(b*b -4*c)

    minR = math.floor(((b-delta)/2) +1)
    maxR = math.ceil(((b+delta)/2)-1)
    diff = maxR-minR+1
    #print(b,c,delta, minR, maxR, diff)
    result = result * diff
print(result)