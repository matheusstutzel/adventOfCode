from sys import stdin


def offer(a, b, c):
    aux = a.split(",")
    x1 = int(aux[0])
    y1 = int(aux[1])

    aux = b.split(",")
    x2 = int(aux[0])
    y2 = int(aux[1])

    if x1 == x2:
        for i in range(min(y1, y2), max(y1,y2)+1):
            print(x1, i, "x")
            c[x1][i] = c[x1][i] + 1

    if y1 == y2:
        for i in range(min(x1, x2), max(x1,x2)+1):
            print(i, y1, "y")
            c[i][y1] = c[i][y1] + 1

size=1000
c = [[0 for x in range(size)] for y in range(size)] 

for line in stdin:
    n = line.rstrip().split(" -> ")
    offer(n[0], n[1], c)
    print(n)

r =0 
for l in c:
    for d in l:
        print(d,",", end="")
        if d>=2:
            r=r+1
    print("")

print(r)