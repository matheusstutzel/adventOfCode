import sys

def printAll(rope):
    for i in range(27):
        for j in range(27):
            c = '.'
            for k, r in enumerate(rope):
                if( (i,j)==r and c == '.'):
                    c = str(k)
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

rope = [(0,0) for i in range(10)]

pos.add(rope[0])

for l in sys.stdin:
    d,k = l.split(" ")
    for i in range(int(k)):
        rope[0] = (rope[0][0]+mov[d][0], rope[0][1]+mov[d][1])
        for r in range(1,len(rope)):
            rope[r] = update(rope[r-1], rope[r])
        #printAll(rope)
        pos.add(rope[-1])
print(len(pos))