import sys

t = 0

# reading input
for line in sys.stdin:
    l = line.rstrip()
    a,b = l.split(",")
    a1,a2 = a.split("-")
    b1,b2 = b.split("-")

    a1 = int(a1)
    a2 = int(a2)
    b1 = int(b1)
    b2 = int(b2)
    
    #make sure a<b
    if((a2-a1)>(b2-b1)):
        a1,a2,b1,b2=b1,b2,a1,a2

    if((a1>=b1 and a1<=b2) or (a2>=b1 and a2<=b2)):
        t = t+1

print(t)