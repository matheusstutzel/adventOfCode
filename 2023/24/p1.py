import sys


def valid (a,b, minV, maxV):
    #print("comparing",a,b)
    sx1,sy1,sz1 = a[0]
    dx1,dy1,dz1 = a[1]

    sx2,sy2,sz2 = b[0]
    dx2,dy2,dz2 = b[1]

    num = dx1*dx2*(sy2-sy1)+ (dx2*sx1*dy1) - (dx1*sx2*dy2)

    div = dx2*dy1 - dx1*dy2
    if div==0:
        #print("parallel")
        return False
    x = num / div
    t1 = (x-sx1)/dx1
    t2 = (x-sx2)/dx2
    y = sy1+dy1*t1
    if t1<0 and t2<0:
        #print("in the past for both")
        return False
    if t1<0:
        #print("in the past for A")
        return False
    if t2<0:
        #print("in the past for B")
        return False
    
    #print(x,y)
    return x>=minV and x<=maxV and y>=minV and y<=maxV

entries = []
for l in sys.stdin:
    a, b = l.strip().split(" @ ")
    convert = lambda x: [ int(y) for y in x.replace(",", "").split()]
    entries.append((convert(a), convert(b)))

#print(entries)
count = 0 
for i in range(len(entries)):
    for j in range(i+1, len(entries)):
        if i == j:
            continue
        cross = valid(entries[i],entries[j],200000000000000,400000000000000)
        if(cross):
            count+=1
        #print(cross)
        #print(" ")
print(count)