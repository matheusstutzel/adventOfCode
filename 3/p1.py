import sys

c = []
t = 0

# reading input
for line in sys.stdin:
    l = line.rstrip()
    if c == []:
        c = [0]*len(l)
    for i, x in enumerate(l):
        c[i] = c[i] + (1 if x == '1' else 0)
    t = t + 1

k = 1
g = 0
e = 0
c.reverse()
for b in c:
    if b>t/2:
        g=g+k
    else:
        e=e+k
    k=k*2


print(e*g)
