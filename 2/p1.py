import sys


d=0
h=0
for line in sys.stdin:
    c,v = line.rstrip().split(" ")
    if c == "forward":
        h = h +int(v)
    elif c=="up":
        d=d-int(v)
    elif c=="down":
        d=d+int(v)
    else:
        print("somthing is wrong")

print(d*h)
