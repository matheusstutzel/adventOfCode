import math
from sys import stdin


n= [int(x) for x in stdin.readline().split(",")]

n.sort()
l = len(n)
a = math.ceil(l/2)
b = math.floor(l/2)

dest = (n[a]+n[b])/2

r = sum([abs(x-dest) for x in n])
print(r)