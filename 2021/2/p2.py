import sys


d = 0
h = 0
a = 0
for line in sys.stdin:
    c, x = line.rstrip().split(" ")
    x = int(x)
    if c == "forward":
        h = h + x
        d = d+(a*x)
    elif c == "up":
        a = a-x
    elif c == "down":
        a = a+x
    else:
        print("somthing is wrong")
    #print(" test a%d h%d d%d c%s x%s"%(a,h,d,c,x))

print(d*h)
