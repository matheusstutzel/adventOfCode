import sys

def printAll(h,t):
    for i in range(6):
        for j in range(5):
            c = ''
            if( (i,j)==h):
                c = "H"
            elif (i,j)==t:
                c="T"
            else:
                c="."
            print(c, end=" ")
        print("")
    print(" ----- ")


def update(h,t):
    i1, j1 = h
    i2,j2 = t
    if(abs(i1-i2)<2 and abs(j1-j2)<2): #touch->don't move
        return t
    if((abs(i1-i2)>0) ^ (abs(j1-j2)>0)): #move along X or Y -> move torwards H
        return ((i1+i2)/2, (j1+j2)/2)
    a = 1 if i1>i2 else -1
    b = 1 if j1>j2 else -1
    return (i2+a, j2+b)


mov = {
    "R":(0,+1),
    "L":(0,-1),
    "D":(-1,0),
    "U":(1,0)
    }

pos = set()

h = (0,0)
t = (0,0)

pos.add(t)

for l in sys.stdin:
    d,k = l.split(" ")
    for i in range(int(k)):
        h = (h[0]+mov[d][0], h[1]+mov[d][1])
        t = update(h,t)
        #printAll(h,t)
        pos.add(t)
print(len(pos))