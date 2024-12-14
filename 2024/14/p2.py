import sys
import math

def parse(x):
    p,v = x.strip().split()
    px,py = p.split("=")[1].split(",")
    vx,vy = v.split("=")[1].split(",")
    return ((int(px),int(py)), (int(vx), int(vy)))

r = [parse(l) for l in sys.stdin]

size=(101,103)
mx = size[0]//2
my = size[1]//2

sfmin=math.inf
sfmax=0
resp = 0
for i in range(size[0]*size[1]):
    tl = 0
    tr = 0 
    bl = 0
    br = 0
    for p,v in r:
        nx = (p[0] +v[0]*i)%size[0]
        ny = (p[1] +v[1]*i)%size[1]
        if nx<mx and ny<my:
                tl+=1
        if nx<mx and ny>my:
                tr+=1
        if nx>mx and ny<my:
                bl+=1
        if nx>mx and ny>my:
                br+=1
    sf = tl*tr*bl*br
    #print(i,sf)
    sfmax=max(sfmax,sf)
    if sf<sfmin:
        print(i, sf)
        sfmin=sf
        resp = i
print(resp)
            
    
