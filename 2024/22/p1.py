import sys

def calc(x, r):
    for i in range(r):
        x = (x^(x*64)) %16777216
        x = (x^(x//32))%16777216
        x = (x^(x*2048)) %16777216        
    return x
l =[int(l.strip()) for l in sys.stdin]

r = 0
for x in l:
    y = calc(x, 2000)
    print(x,y)
    r+=y
print(r)
