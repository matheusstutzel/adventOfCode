import sys

def sides(x, y, z):
    yield (x + 1, y, z)
    yield (x - 1, y, z)
    yield (x, y + 1, z)
    yield (x, y - 1, z)
    yield (x, y, z + 1)
    yield (x, y, z - 1)

p = [tuple([int(k) for k in l.strip().split(",")]) for l in sys.stdin]
size = 30
total = 0 
for pt in p:
    for side in sides(*pt):
        if(side not in p):
            total = total+1
print(total)
                