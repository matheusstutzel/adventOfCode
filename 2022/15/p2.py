import sys

def convert(l):
    l = l.strip()
    p = l.split(" ")
    x1 = int(p[2].split("=")[1].split(",")[0])
    y1 = int(p[3].split("=")[1].split(":")[0])


    x2 = int(p[8].split("=")[1].split(",")[0])
    y2 = int(p[9].split("=")[1])

    return [(x1,y1), (x2,y2), abs(x1-x2) + abs(y1-y2)]
lines = [convert(l) for l in sys.stdin]
#Sensor at x=2, y=18: closest beacon is at x=-2, y=15


maxTarget = 4000000

rx = 0 
ry = 0 
for target in range(maxTarget):
    segments = []
    for l in lines:
        s,_,dist = l 
        x,y = s 
        a = dist - abs(target-y)
        if(a>=0):
            seg = (max(0,x-a),min(maxTarget,x+a))
            segments.append(seg)
    segments = sorted(segments)
    total = 0 
    s,e = segments[0]
    for i in range(1, len(segments)):
        ns,ne = segments[i]
        if(ns>e): #different segment
            s,e = ns,ne
            ry = target
            rx=ns-1

            break
        else:
            e = max(e,ne)
    else:
        continue
    break


print(rx,ry,ry+ rx*4000000)
"""
real    0m23,415s
user    0m23,382s
sys     0m0,014s
"""