import math
from sys import stdin

def msum(n):
    return (n*(n+1))/2
n= [int(x) for x in stdin.readline().split(",")]

n.sort()
l = len(n)

# workaround... example should use ceil, input should use floor 
dest = math.floor((sum(n))/l)

r = sum([msum(abs(x-dest)) for x in n])
print(dest, r)