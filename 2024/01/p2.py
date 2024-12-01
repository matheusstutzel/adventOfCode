import sys

a=[]
b={}
for l in sys.stdin:
    l = l.rstrip()
    x,y = l.split()
    a.append(int(x))
    y=int(y)
    b[y]=1 if y not in b else 1+b[y]

sum=0
for x in a:
    sum = sum + (x * (b[x] if x in b else 0))
print(sum)
