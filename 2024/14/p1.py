import sys

def parse(x):
    p,v = x.strip().split()
    px,py = p.split("=")[1].split(",")
    vx,vy = v.split("=")[1].split(",")
    return ((int(px),int(py)), (int(vx), int(vy)))

r = [parse(l) for l in sys.stdin]

rounds = 100
size=(101,103)
mx = size[0]//2
my = size[1]//2

tl = 0
tr = 0 
bl = 0
br = 0
for p,v in r:
    nx = (p[0] +v[0]*rounds)%size[0]
    ny = (p[1] +v[1]*rounds)%size[1]
    if nx<mx and ny<my:
            tl+=1
    if nx<mx and ny>my:
            tr+=1
    if nx>mx and ny<my:
            bl+=1
    if nx>mx and ny>my:
            br+=1
print(tl,tr,bl,br)
print(tl*tr*bl*br)            
