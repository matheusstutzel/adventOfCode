import sys

a=[]
b=[]
for l in sys.stdin:
    l = l.rstrip()
    x,y = l.split()
    a.append(int(x))
    b.append(int(y))
a.sort()
b.sort()
sum=0
for x,y in zip(a,b):
    sum = sum + abs(x-y)
print(sum)
