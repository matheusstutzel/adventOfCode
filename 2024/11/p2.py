import sys
import math

l = [[int(x) for x in l.strip().split()] for l in sys.stdin][0]

def calc(mem, x, l):
    if l == 0:
        return 1
    if x in mem[l]:
        return mem[l][x]
    if x == 0:
        mem[l][x]=calc(mem,1,l-1)
    elif (int(math.log10(x))+1)%2==0:
        s = str(x)
        mem[l][x] = calc(mem, int(s[:len(s)//2]), l-1) + calc(mem, int(s[len(s)//2:]), l-1)
    else:
        mem[l][x]=calc(mem, x*2024, l-1)
    return mem[l][x]

limit = 76

mem = [{} for i in range(limit)]

for i in range(limit):
    print(sum([calc(mem,x,i) for x in l]))
